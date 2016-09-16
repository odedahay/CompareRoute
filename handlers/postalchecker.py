from framework.request_handler import CompareRouteHandler
from model.admin_account import postalRecordDB, PostalRecordDB_alert, PostalRecordDB_history
import urllib2
import urlparse
import hmac
import base64
import hashlib
import json
import logging
from google.appengine import runtime
from google.appengine.ext import ndb
import csv


class Postal_checkerHandler(CompareRouteHandler):
    def get(self):

        results = postalRecordDB.query().order(postalRecordDB.postal_code).fetch(10)
        postalCheckers = PostalRecordDB_alert.query().order(-PostalRecordDB_alert.postal_code).fetch()
        postalHistory = PostalRecordDB_history.query().order(-PostalRecordDB_history.postal_code).fetch()

        # If same postal code == show only 1
        # Count how many time they use
        # Fix the bugs if to delete

        new_alert_values = {
            'results': results,
            'postalCheckers': postalCheckers,
            'postalHistory': postalHistory
        }

        self.render('admin/admin_alert.html', **new_alert_values)

class Postal_checker_add_Handler(CompareRouteHandler):

    def update_postalcode_db(self, postal_code, longtitude, latitude):

        # Status of postal code added
        status = []
        success = False
        msg = ""

        if not postal_code:
            success = False
            msg = "Please check the Postal code"
            status.append(success)
            status.append(msg)

            return status
        else:
            postalRecordDB.add_new_records(postal_code, longtitude, latitude)

            success = True
            msg = "Postal Code added, please refresh your browser"
            status.append(success)
            status.append(msg)

            return status

class Postal_move_Handler(CompareRouteHandler):
    # def post(self):
    #
    #     postalCheckers = PostalRecordDB_alert.query().order(-PostalRecordDB_alert.postal_code).fetch()

    def move_postalcode_db(self,compare_id, created_date, user_email, postal_code):

        # Status of postal code added
        status = []
        success = False
        msg = ""

        if not postal_code:
            success = False
            msg = "Please check the Postal code"
            status.append(success)
            status.append(msg)

            return status

        else:
            # Add to History
            PostalRecordDB_history.add_new_postal_records(compare_id, postal_code, user_email, created_date)

            # Delete the postal code
            delete_data = PostalRecordDB_alert.delete_postal_records(compare_id)
            delete_data.key.delete()

            success = True
            msg = "Successful"
            status.append(success)
            status.append(msg)

            return status

class Postal_checker_Handler(CompareRouteHandler):

    def check_postalcode(self, postal_code):

        # Status of postal code added
        status = []
        laglongSource_orig = []
        update_postalcode = []
        error_postalcode = []
        success = False
        error = "Z"
        msg = ""

        check_postal_alert = "https://maps.googleapis.com/maps/api/geocode/json?address=" + postal_code

        print('check_postal_alert'), check_postal_alert

        latlong = urllib2.urlopen(check_postal_alert)

        wjson = latlong.read()
        latLng = json.loads(wjson)

        postal_check = latLng['status'][0]

        if postal_check == error:
            print ('Error on this')

            success = False

            laglongSource_orig.append(success)
            laglongSource_orig.append(success)

            error_postalcode.append(postal_code)

            msg = "No Postal Record"
            status.append(success)
            status.append(msg)

            return laglongSource_orig, error_postalcode, status

        else:

            latValorg = latLng['results'][0]['geometry']['location']['lat']
            lngValorg = latLng['results'][0]['geometry']['location']['lng']

            # Combining the the Lat and Long in order to compute the Distance

            laglongSource_orig.append(latValorg)
            laglongSource_orig.append(lngValorg)

            # origin_destination = ''.join(laglongSource_orig)

            success = True
            msg = "Successful"
            status.append(success)
            status.append(msg)

            return laglongSource_orig, status

def signUrl(my_url):
    my_url = my_url + "&client=gme-republicpolytechnic"
    url = urlparse.urlparse(my_url)

    privateKey = "nJxJLqiWuL68EBCc_nPpepmGmKE="

    # We only need to sign the path+query part of the string
    urlToSign = url.path + "?" + url.query

    # Decode the private key into its binary format
    decodedKey = base64.urlsafe_b64decode(privateKey)

    # Create a signature using the private key and the URL-encoded
    # string using HMAC SHA1. This signature will be binary.
    signature = hmac.new(decodedKey, urlToSign, hashlib.sha1)

    # Encode the binary signature into base64 for use within a URL
    encodedSignature = base64.urlsafe_b64encode(signature.digest())
    originalUrl = url.scheme + "://" + url.netloc + url.path + "?" + url.query
    #print("Full URL: " + originalUrl + "&signature=" + encodedSignature)
    return originalUrl + "&signature=" + encodedSignature





