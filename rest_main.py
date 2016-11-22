import webapp2
import mimetypes
import os
import time
from datetime import datetime
import base64
import urlparse
from httplib import HTTPResponse

import logging
import json

import urllib
# ------ sorting -----
from handlers import sorting, sorting_prep

from model.user_account import UserAccount
from model.admin_account import postalRecordDB


'''
{
  "status": "ok",
  "data_result": {
    "has_return": "true",
    "vehicle_priority": {
      "vehicle_num": 2
    },
    "total_summary_saving:": [
      {
        "propose _distance": 139.289,
        "total_savings": 31.76656738644825,
        "current_distance": 204.136
      }
    ],
    "starting_postal": "461051",
    "capacity_priority": {
      "priority_capacity": "false",
      "vehicle_type": "truck_1",
      "vehicle_capacity": "10"
    },
    "postal_sequence": [
      [
        "460102",
        "Order10",
        1
      ],
      [
        "469001",
        "Order01",
        1
      ],
      [
        "408561",
        "Order11",
        2
      ],
      [
        "431011",
        "Order09",
        1
      ],
      [
        "098585",
        "Order05",
        1
      ],
      [
        "109680",
        "Order06",
        1
      ],
      [
        "278986",
        "Order08",
        2
      ],
      [
        "596740",
        "Order04",
        2
      ],
      [
        "596937",
        "Order03",
        2
      ],
      [
        "689575",
        "Order12",
        2
      ],
      [
        "760450",
        "Order02",
        2
      ],
      [
        "560405",
        "Order07",
        3
      ],
      [
        "560405",
        "Order07-B",
        2
      ]
    ]
  }
}

'''

def checkInRequest(field, request):
    # if myconstants.DEBUG:
    #     logging.debug(field)

    if field in request:
        return request[field], []
    else:
        return None, [field + " missing"]

class Truck_capacity_API(webapp2.RequestHandler):
    def post(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
        self.response.headers['Access-Control-Allow-Headers'] = 'Authorization'
        self.response.headers['Access-Control-Allow-Headers'] = 'Cache-Control'
        self.response.headers['Access-Control-Allow-Credentials'] = 'true'
        self.response.headers['Content-Type'] = 'application/json;charset=utf-8'

        email = self.request.get('userId')
        api_key = self.request.get('keyId')

        # Error list for invalid postal codes
        errors = []

        api_user = "false"
        auth_user = UserAccount.check_API_auth(email, api_key)

        # Sorting postal code sequence code
        postal_sequence_list = []
        postal_sequence_current = []

        # Type of Truck
        truck_capacity_grp = []

        # Empty Array for Route By Capacity
        truck_capacity_list = []
        truck_capacity_list_1 = []
        truck_capacity_list_2 = []

        # Error Message
        error_valid_msg_truck = "Not Enough Truck! <br />The minimum balance number for delivery truck "
        error_capacity_msg_truck = " - exceeding capacity"
        error_capacity_num_truck = "Total maximum for 15 Trucks only"
        error_capacity_cargo_unit = "Please check the input cargo unit - Location Details"

        maximum_truck = 15

        if auth_user == None:
            errors.extend(['Incorrect email or API Key'])

        if auth_user == True:
            api_user = "true"

        # Checking for Credit Access
        credits_account = UserAccount.check_credit_usage(email)

        if credits_account == None:
            errors.extend(['Error in Credits Access'])

        response = {}
        request_str = self.request.body
        logging.info(request_str)

        if len(errors) == 0:

            try:
                data = json.loads(request_str)

            except:

                errors.extend(['Error in JSON'])

        if len(errors) == 0:

            starting_postal, error = checkInRequest('starting_postal', data)
            errors.extend(error)

            order_details, error = checkInRequest('order_details', data)
            errors.extend(error)

            type_of_truck, error = checkInRequest('type_of_truck', data)
            errors.extend(error)

            truck_capacity, error = checkInRequest('truck_capacity', data)
            errors.extend(error)

            num_of_truck, error = checkInRequest('num_of_truck', data)
            errors.extend(error)

            # 2nd truck:
            type_of_truck_1, error = checkInRequest('type_of_truck_1', data)
            errors.extend(error)

            truck_capacity_1, error = checkInRequest('truck_capacity_1', data)
            errors.extend(error)

            num_of_truck_1, error = checkInRequest('num_of_truck_1', data)
            errors.extend(error)

            # 3rd truck:
            type_of_truck_2, error = checkInRequest('type_of_truck_2', data)
            errors.extend(error)

            truck_capacity_2, error = checkInRequest('truck_capacity_2', data)
            errors.extend(error)

            num_of_truck_2, error = checkInRequest('num_of_truck_2', data)
            errors.extend(error)

            has_return, error = checkInRequest('has_return', data)
            errors.extend(error)

            priority_capacity, error = checkInRequest('priority_capacity', data)
            errors.extend(error)

            # Counter checking of Postal Code
            num_post_code = 0

            for index in range(0, len(order_details)):
                """ ['760450', 'Order02', '2'] """

                num_post_code += 1
                postal_pair = order_details[index]

                if len(postal_pair) == 1:
                    logging.info(postal_pair)
                    errors.extend([error_capacity_cargo_unit])
                    break

                if len(postal_pair) == 2:
                    logging.info(postal_pair)
                    errors.extend([error_capacity_cargo_unit])
                    break

                # print "postal_pair", postal_pair

                postal_code = str(postal_pair[0])
                order_id = str(postal_pair[1])
                track_capacity = postal_pair[2]

                # Check if the postal code is 5 digit only
                if len(str(postal_code)) == 5:

                    # add "0" in the index of Postal Code
                    postal_code = "0" + postal_code

                # Check if the 3rd column is integer or number
                cargo_unit = RepresentsInt(track_capacity)

                if not cargo_unit:
                    errors.extend([postal_code + ' Error in track_capacity'])
                    break

                # Check if postal code is a valid value i.e. Contains only five or six digits
                if not str.isdigit(postal_code) or len(str(postal_code)) != 6:
                    logging.info('Warning! Postal Code error')
                    errors.extend(['Please check '+postal_code+ ' is not valid it should be 6 digit'])

                # Check the limit of truck capacity limit for num_truck
                if type_of_truck_1 and not type_of_truck_2:

                    if track_capacity > int(truck_capacity_1):
                        logging.info('Warning! '+postal_code + error_capacity_msg_truck)
                        errors.extend(['Warning! '+postal_code + error_capacity_msg_truck])

                elif type_of_truck_2:

                    if track_capacity > int(truck_capacity_2):
                        logging.info('Warning! '+postal_code + error_capacity_msg_truck)
                        errors.extend(['Warning! '+postal_code + error_capacity_msg_truck])
                else:

                    if track_capacity > int(truck_capacity):

                        logging.info('Warning! '+postal_code + error_capacity_msg_truck)
                        errors.extend(['Warning! '+postal_code + error_capacity_msg_truck])

                postal_sequence_current.append(str(postal_code))
                postal_sequence_list.append([str(postal_code), str(order_id), int(track_capacity)])

                # - - - - - - HQ Starting point Lat Long - - - - - #

            # maximum of 3 fields for truck
            # Additional Field of Truck 2
            # type_of_truck_1
            # truck_capacity_1
            # num_of_truck_1

            # Additional Field of Truck 3
            # type_of_truck_2
            # truck_capacity_2
            # num_of_truck_2

            if type_of_truck_1 and not type_of_truck_2:

                # check if the num_of_truck is over to 15 truck
                if int(num_of_truck) + int(num_of_truck_1) > maximum_truck:
                    errors.extend([error_capacity_num_truck])

                truck_capacity_list.extend([str(type_of_truck), int(truck_capacity), int(num_of_truck)])
                truck_capacity_list_1.extend([str(type_of_truck_1), int(truck_capacity_1), int(num_of_truck_1)])
                truck_capacity_grp.extend([truck_capacity_list, truck_capacity_list_1])

            elif type_of_truck_2:

                # check if the num_of_truck is over to 15 truck
                if int(num_of_truck) + int(num_of_truck_1) + int(num_of_truck_2) > maximum_truck:
                    errors.extend([error_capacity_num_truck])

                truck_capacity_list.extend([str(type_of_truck), int(truck_capacity), int(num_of_truck)])

                # Append all value for truck 2
                truck_capacity_list_1.extend([str(type_of_truck_1), int(truck_capacity_1), int(num_of_truck_1)])
                truck_capacity_list_2.extend([str(type_of_truck_2), int(truck_capacity_2), int(num_of_truck_2)])

                # grp all list truck
                truck_capacity_grp.extend([truck_capacity_list, truck_capacity_list_1, truck_capacity_list_2])

            else:

                # check if the num_of_truck is over to 15 truck
                if int(num_of_truck) > maximum_truck:
                    errors.extend([error_capacity_num_truck])

                truck_capacity_list.extend([str(type_of_truck), int(truck_capacity), int(num_of_truck)])
                truck_capacity_grp.extend([truck_capacity_list])

            # For Non Multi Truck
            options_truck = "false"
            priority_capacity_comp = "false"
            sort_company = "false"
            vehicle_quantity = 0

            if len(errors) == 0:

                origin_destination, postal_result, current_result, vehicle_postal_list_new_seq, grp_truck = sorting.sort_by_postals_chunck(
                    int(starting_postal),
                    postal_sequence_list,
                    int(vehicle_quantity),
                    email, has_return,
                    priority_capacity,
                    priority_capacity_comp,
                    api_user, sort_company, truck_capacity_grp, options_truck)

                # Vehicle Result base of the priority:
                result_num_truck = len(postal_result)

                # Checking if truck is enough
                if len(truck_capacity_grp) == 1:

                    if int(result_num_truck) > int(num_of_truck):
                        errors.extend([error_valid_msg_truck + type_of_truck + " is " + str(result_num_truck)])

                elif len(truck_capacity_grp) == 2:

                    if int(result_num_truck) > int(num_of_truck) + int(num_of_truck_1):
                        errors.extend([error_valid_msg_truck,  type_of_truck_1, " is ", int(result_num_truck) - int(num_of_truck)])

                elif len(truck_capacity_grp) == 3:

                    if int(result_num_truck) > int(num_of_truck) + int(num_of_truck_1) + int(num_of_truck_2):
                        errors.extend([error_valid_msg_truck, type_of_truck_2, " is ", int(result_num_truck) - (int(num_of_truck) + int(num_of_truck_1))])

                    '''['postal_result', 'order_id', 'capacity']'''

                # Converting HQ to lat & long value
                # origin_destination = self.convert_hq(str(starting_postal))
                current_distance = sorting_prep.result_distance_latlng(current_result, origin_destination, num_post_code)
                proposed_distance = sorting_prep.result_distance_latlng(postal_result, origin_destination, num_post_code)

                # GeoCode Map
                latlng_array = map_visible(postal_result)

                # Converting the total percentage saving of distance
                difference_total = current_distance - proposed_distance
                percentage_savings = (difference_total / current_distance) * 100

                # Converting JSON
                response['status'] = 'ok'
                response['data_result'] = [
                        {
                            "required_fields": {
                                "starting_postal": starting_postal,
                                "propose_result": vehicle_postal_list_new_seq,
                                # "postal_sequence": vehicle_postal_list_new_seq,
                                "has_return": has_return
                                },
                            "geo_code_latlng": {
                                "latlng_array": latlng_array
                            },
                            "capacity_priority": {
                                "priority_capacity": priority_capacity,
                                "grp_truck": grp_truck
                                },
                            "total_summary_saving": {
                                "propose_distance": proposed_distance,
                                "current_distance": current_distance,
                                "total_savings": percentage_savings
                                }
                        }
                    ]

            else:
                errors.extend(['Error in Process'])

        if len(errors) > 0:
            response['status'] = 'error'
            response['errors'] = errors

        logging.info(response)
        self.response.out.write(json.dumps(response, indent=3))


class Multi_truck_API(webapp2.RequestHandler):

    def post(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
        self.response.headers['Access-Control-Allow-Headers'] = 'Authorization'
        self.response.headers['Access-Control-Allow-Headers'] = 'Cache-Control'
        self.response.headers['Access-Control-Allow-Credentials'] = 'true'
        self.response.headers['Content-Type'] = 'application/json;charset=utf-8'

        # api_key = self.request.authorization

        email = self.request.get('userId')
        api_key = self.request.get('keyId')

        # Error list for invalid postal codes
        errors = []

        api_user = "false"
        auth_user = UserAccount.check_API_auth(email, api_key)

        if auth_user == None:
            errors.extend(['Incorrect email or API Key'])

        if auth_user == True:
            api_user = "true"

        # Checking for Credit Access
        credits_account = UserAccount.check_credit_usage(email)

        if credits_account == None:
            errors.extend(['Error in Credits Access <br />'])

        response = {}
        request_str = self.request.body
        logging.info(request_str)

        if len(errors) == 0:

            try:
                data = json.loads(request_str)

            except:

                errors.extend(['Error in JSON'])

        if len(errors) == 0:

            starting_postal, error = checkInRequest('starting_postal', data)
            errors.extend(error)

            order_details, error = checkInRequest('order_details', data)
            errors.extend(error)

            number_of_vehicle, error = checkInRequest('number_of_vehicle', data)
            errors.extend(error)

            has_return, error = checkInRequest('has_return', data)
            errors.extend(error)

            options_truck, error = checkInRequest('options_truck', data)
            errors.extend(error)

            # priority_capacity, error = checkInRequest('priority_capacity', data)
            # errors.extend(error)
            #
            # vehicle_type, error = checkInRequest('vehicle_type', data)
            # errors.extend(error)

            # vehicle_capacity, error = checkInRequest('vehicle_capacity', data)
            # errors.extend(error)

            # sort_company, error = checkInRequest('sort_company', data)
            # errors.extend(error)

            # num_comp_val, error = checkInRequest('num_comp_val', data)
            # errors.extend(error)

            # Sorting postal code sequence code
            postal_sequence_list = []
            postal_sequence_current = []

            # For empty order id and capacity
            forEmp_OrderID_Cap = ['0', '0']
            forEmp_Capt = ['0']

            # Validation for Vehicle
            if not number_of_vehicle:
                errors.extend(["number_of_vehicle" + " is empty"])

            # starting point 5 digit
            if len(str(starting_postal)) == 5:
                    starting_postal = "0" + starting_postal

            # if below 5 digit
            if len(starting_postal) != 6:
                logging.info('Warning! '+starting_postal+ ' error')
                errors.extend(['Starting Postal code is not valid, '+starting_postal+ ' it should be 6 digit'])

            # Counter checking of Postal Code
            num_post_code = 0

            for index in range(0, len(order_details)):
                num_post_code += 1
                postal_pair = order_details[index]

                """ [u'760450', u'Order02'] """

                if len(postal_pair) == 1:
                    logging.info(postal_pair)
                    postal_pair.extend(forEmp_OrderID_Cap)

                if len(postal_pair) == 2:
                    logging.info(postal_pair)
                    postal_pair.extend(forEmp_Capt)

                postal_code = str(postal_pair[0])
                order_id = str(postal_pair[1])
                track_capacity = int(postal_pair[2])

                if len(str(postal_code)) == 5:
                    postal_code = "0" + postal_code

                # Check if postal code is a valid value i.e. Contains only five or six digits
                if not str.isdigit(postal_code) or len(str(postal_code)) != 6:
                    logging.info('Warning! Postal Code error')
                    errors.extend(['Please check '+postal_code+ ' is not valid it should be 6 digit'])

                postal_sequence_current.append(str(postal_code))
                postal_sequence_list.append([str(postal_code), str(order_id), int(track_capacity)])

            # - - - - - - HQ Starting point Lat Long - - - - - #

            # For Non Multi Truck
            priority_capacity = "false"
            priority_capacity_comp = "false"
            sort_company = "false"

            truck_capacity_grp = []

            if len(errors) == 0:

                origin_destination, postal_result, current_result, vehicle_postal_list_new_seq, grp_truck = sorting.sort_by_postals_chunck(
                    int(starting_postal),
                    postal_sequence_list,
                    int(number_of_vehicle),
                    email, has_return,
                    priority_capacity,
                    priority_capacity_comp,
                    api_user, sort_company, truck_capacity_grp, options_truck)

                '''['postal_result', 'order_id', 'capacity']'''

                # Converting HQ to lat & long value
                # origin_destination = self.convert_hq(str(starting_postal))
                current_distance = sorting_prep.result_distance_latlng(current_result, origin_destination, num_post_code)
                proposed_distance = sorting_prep.result_distance_latlng(postal_result, origin_destination, num_post_code)

                # GeoCode Map
                latlng_array = map_visible(postal_result)

                # Converting the total percentage saving of distance
                difference_total = current_distance - proposed_distance
                percentage_savings = (difference_total / current_distance) * 100

                # Converting JSON
                response['status'] = 'ok'
                response['data_result'] = [
                        {
                            "required_fields": {
                                "starting_postal": starting_postal,
                                "propose_result": vehicle_postal_list_new_seq,
                                "has_return": has_return
                                },
                            "geo_code_latlng": {
                                "latlng_array": latlng_array
                            },
                            "vehicle_priority": {
                                "vehicle_num": number_of_vehicle
                                },

                            "total_summary_saving": {
                                "proposed_distance": proposed_distance,
                                "current_distance": current_distance,
                                "total_savings": percentage_savings
                                }
                        }
                    ]

            else:
                errors.extend(['Error in Process'])

        if len(errors) > 0:
            response['status'] = 'error'
            response['errors'] = errors

        logging.info(response)
        self.response.out.write(json.dumps(response, indent=3))

def RepresentsInt(num):

    try:
        int(num)
        return True

    except ValueError:

        return False


# GeoCode Latlng MAP - single company
def map_visible(propose_result):
    latlng_array = []

    for vehicle_postal in propose_result:
        lat_long_Source = []

        for current_post in vehicle_postal:
            # Convert to Lat-Long the postal code
            destinations = postalcode_latlong(current_post)

            # For Geo-Code MAP
            lat_long_value_map = str(destinations)
            lat_long_value_map = lat_long_value_map.split(",")
            lat_long_Source.append(lat_long_value_map)

        # - - -  for lat & long value with vehicle number- - - #
        latlng_array.append(lat_long_Source)

    return latlng_array

def postalcode_latlong(postal):

        # Validation for Task Q
        compare_postal = postalRecordDB.check_if_exists(postal)

        if compare_postal == None:

            if postal[0] == "0":
                current_post = postal.lstrip("0")
                compare_postal = postalRecordDB.check_if_exists(current_post)
            else:
                print('load')
                nearestPostalCode = postalRecordDB.query().filter(postalRecordDB.postal_code >= postal).get(keys_only=True)
                compare_postal = nearestPostalCode.id()

        latlong = postalRecordDB.get_by_id(compare_postal)

        laglongSource = []
        laglongSource.append(latlong.lat)
        laglongSource.append(',')
        laglongSource.append(latlong.long)
        destinations = ''.join(laglongSource)

        return destinations

app = webapp2.WSGIApplication([
    # ('/api/v1(.*)', SortingHandler),
    ('/api/multi_truck/v1', Multi_truck_API),
    ('/api/truck_capacity/v1', Truck_capacity_API)
], debug=True)