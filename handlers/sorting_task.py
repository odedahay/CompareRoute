# Date and time
from datetime import datetime

import webapp2

from handlers import base
from model.admin_account import ProposedRoute
from model.admin_account import CurrentRoute
from model.admin_account import RouteDistance
from handlers.postalchecker import postalRecordDB
import urllib
import json

import sorting
import sorting_prep
import urllib
import urllib2
import logging

class TaskRouteHandlerProposed(base.BaseHandler):
    def post(self):

        if not 'X-AppEngine-TaskName' in self.request.headers:
            self.error(403)

        compare_id = self.request.get('compare_id')
        starting_address = self.request.get('starting_address')
        num_of_vehicle = self.request.get('num_of_vehicle')
        vehicle_capacity = self.request.get('vehicle_capacity')
        email = self.request.get('email')
        has_return = self.request.get('has_return')
        num_user_load = self.request.get('num_user_load')
        #num_of_vehicles = self.request.get('num_of_vehicles')

        proposedPostlal = self.request.get('proposedPostlal')
        currentdPostlal = self.request.get('currentdPostlal')

        origin_destination = sorting.startingpoint_latlong(starting_address)

        proposed_total_dist = self.task_proposed_Route(compare_id, starting_address, proposedPostlal, origin_destination)
        current_total_dist = self.task_current_Route(compare_id, starting_address, currentdPostlal, origin_destination)

        # Counting the number of postal code:
        actual_vehicle_postal = proposedPostlal.split("_")
        postal_count_arr = []

        for vehicle_postal in actual_vehicle_postal:
            vehicle_postal = vehicle_postal.split(", ")

            for current_post in vehicle_postal:
                postal_count_arr.append(current_post)

        postal_count = len(postal_count_arr)

        # Return vehicle
        if has_return == "true":
            return_vehicle = "Yes"
        else:
            return_vehicle = "No"

        user_count = 0

        # Counter Sign
        if num_user_load == "true":
            user_count += 1

        # Total Percentage Saving
        difference_total = current_total_dist - proposed_total_dist
        percentage_savings = (difference_total / current_total_dist) * 100

        RouteDistance.add_new_route(compare_id, email, starting_address, origin_destination, int(num_of_vehicle),
                                    vehicle_capacity, float(current_total_dist),
                                    float(proposed_total_dist), round(percentage_savings, 2),
                                    int(postal_count), return_vehicle, int(user_count))

    def task_proposed_Route(self, compare_id, starting_address, proposedPostlal, origin_destination):

        actual_vehicle_postal = proposedPostlal.split("_")

        origin_postcode = starting_address
        origin_destination = origin_destination

        vehicle_count = 0
        proposed_total_dist = 0

        for vehicle_postal in actual_vehicle_postal:
            vehicle_count = vehicle_count + 1

            vehicle_postal = vehicle_postal.split(", ")
            postal_rank = 0

            for current_post in vehicle_postal:
                postal_rank = postal_rank + 1

                destinations, latval, longval = self.postalcode_latlong(current_post)

                distance1 = "http://dev.logistics.lol:5000/viaroute?loc=" + origin_destination + "&loc=" + destinations

                # Url Link each postal code
                url_id = distance1

                dist_val = urllib.urlopen(distance1)
                wjson = dist_val.read()
                distance2 = json.loads(wjson)
                distance3 = distance2['route_summary']['total_distance']
                distance_km = float(distance3) / 1000

                proposed_total_dist = proposed_total_dist + distance_km

                origin_destination = destinations

                # Storing the data in Proposed Route
                if (postal_rank == 1):

                    ProposedRoute.add_new_proposed_route(compare_id, starting_address, current_post, int(vehicle_count), longval, latval, url_id, round(float(distance_km), 2), int(postal_rank))
                else:
                    ProposedRoute.add_new_proposed_route(compare_id, origin_postcode, current_post, int(vehicle_count), longval, latval, url_id, round(float(distance_km), 2), int(postal_rank))

                origin_postcode = current_post

        return proposed_total_dist

    def task_current_Route(self, compare_id, starting_address, currentdPostlal, origin_destination):

        current_vehicle_postal = currentdPostlal.split("_")

        origin_postcode = starting_address
        origin_destination1 = origin_destination
        vehicle_count = 0
        current_total_dist = 0

        for vehicle_postal in current_vehicle_postal:

            vehicle_count = vehicle_count + 1
            vehicle_postal = vehicle_postal.split(", ")
            postal_rank = 0

            for current_post in vehicle_postal:
                postal_rank = postal_rank + 1

                # Convert to Lat-Long the postal code
                destinations, latval, longval = self.postalcode_latlong(current_post)

                distance1 = "http://dev.logistics.lol:5000/viaroute?loc=" + origin_destination1 + "&loc=" + destinations

                # Url Link each postal code
                url_id = distance1

                dist_val = urllib.urlopen(distance1)
                wjson = dist_val.read()
                distance2 = json.loads(wjson)
                distance3 = distance2['route_summary']['total_distance']
                distance_km2 = float(distance3) / 1000

                current_total_dist = current_total_dist + distance_km2

                origin_destination1 = destinations

                # # Storing data for Current Route
                if (postal_rank == 1):

                    CurrentRoute.add_new_current_route(compare_id, starting_address, current_post, int(vehicle_count), latval, longval, url_id, round(float(distance_km2), 2), int(postal_rank))
                else:
                    CurrentRoute.add_new_current_route(compare_id, origin_postcode, current_post, int(vehicle_count), latval, longval, url_id, round(float(distance_km2), 2), int(postal_rank))

                origin_postcode = current_post

        return current_total_dist

    def postalcode_latlong(self, current_post):

        # Validation for Task Q
        compare_postal = postalRecordDB.check_if_exists(current_post)

        if compare_postal == None:

            if current_post[0] == "0":
                current_post = current_post.lstrip("0")
                compare_postal = postalRecordDB.check_if_exists(current_post)

            else:
                print('Ooops-load')
                nearestPostalCode = postalRecordDB.query().filter(postalRecordDB.postal_code >= current_post).get(keys_only=True)
                compare_postal = nearestPostalCode.id()

        latlong = postalRecordDB.get_by_id(compare_postal)

        laglongSource = []
        laglongSource.append(latlong.lat)
        laglongSource.append(',')
        laglongSource.append(latlong.long)
        destinations = ''.join(laglongSource)

        latval = latlong.lat
        longval = latlong.long

        return destinations, latval, longval

# - - - - - - - - summary total - - - - - - - #
# class summaryTotal_500(base.BaseHandler):
#
#     def post(self):
#
#         if not 'X-AppEngine-TaskName' in self.request.headers:
#             self.error(403)
#
#         origin_destination = self.request.get('origin_destination')
#         result_str = self.request.get('result_str')
#
#         response = {}
#         errors = []
#
#         # - - - Format the result_str - - - #
#
#         result_str = result_str.strip()
#         result_str_split = result_str.split(",")
#
#         # Chunk it
#         result_str_chunk = sorting.chunkIt(result_str_split, 2)
#
#         # Assign per batch
#         batch_1 = result_str_chunk[0]
#         batch_2 = result_str_chunk[1]
#
#         # Get the last item of 1st Batch
#         last_item = batch_1[-1]
#
#         # Insert the 'lastItemB' in the index of next list
#         # To continue the route distance
#         batch_2.insert(0, last_item)
#
#         # - - - - - Get value of list object- - - - - - #
#         batch_1_val = latlong_summary_starting_tq(batch_1, origin_destination)
#         batch_2_val = latlong_summary_tq(batch_2)
#
#         # Sum up all batches
#         route_distance_add = batch_1_val + batch_2_val
#         route_distance = float(route_distance_add) / 1000
#
#         return route_distance
#
#         # print "Result-1111", route_distance
#         #
#         # propose_route_value = route_distance
#         # current_route_value = route_distance
#         #
#         # # Converting the total percentage saving of distance
#         # difference_total = current_route_value - propose_route_value
#         # percentage_savings = (difference_total / current_route_value) * 100
#         #
#         # # Converting JSON
#         # response['status'] = 'ok'
#         # response['data_result'] = [
#         #     {
#         #         "total_summary_saving": {
#         #             "propose_distance": propose_route_value,
#         #             "current_distance": current_route_value,
#         #             "total_savings": percentage_savings
#         #         }
#         #     }
#         # ]
#         #
#         # logging.info(response)
#         # self.response.out.headers['Content-Type'] = 'application/json; charset=utf-8'
#         # self.response.out.write(json.dumps(response, indent=2))
#
#
# # - - -  function for conversion below - - - -#
# def latlong_summary_tq(list):
#
#     url_disc = "http://dev.logistics.lol:5000/viaroute?"
#     proposed_latlong = ""
#
#     for current_post in list:
#         current_post = current_post.strip()
#
#         # Convert to Lat-Long the postal code
#         destinations = sorting_prep.postalcode_latlong(current_post)
#
#         if not destinations:
#             proposed_latlong += str(destinations)
#         else:
#             proposed_latlong += "&loc=" + str(destinations)
#
#     proposed_result = proposed_latlong
#     proposed_api = url_disc + proposed_result
#     dist_val = urllib2.urlopen(proposed_api)
#     wjson = dist_val.read()
#     distance2 = json.loads(wjson)
#
#     distance_val = distance2['route_summary']['total_distance']
#
#     return distance_val
#
# def latlong_summary_starting_tq(list, origin_destination):
#
#     url_disc = "http://dev.logistics.lol:5000/viaroute?loc="
#     proposed_latlong = ""
#
#     for current_post in list:
#         current_post = current_post.strip()
#
#         # Convert to Lat-Long the postal code
#         destinations = sorting_prep.postalcode_latlong(current_post)
#         # print "postal_code : ", current_post
#
#         if not destinations:
#             proposed_latlong += str(destinations)
#         else:
#             proposed_latlong += "&loc=" + str(destinations)
#
#     proposed_result = origin_destination + proposed_latlong
#     proposed_api = url_disc + proposed_result
#     # print ('OSRM Link'), proposed_api
#
#     dist_val = urllib2.urlopen(proposed_api)
#     wjson = dist_val.read()
#     distance2 = json.loads(wjson)
#     distance_val = distance2['route_summary']['total_distance']
#
#     return distance_val
#
#
# app = webapp2.WSGIApplication(routes=[
#     (r'/sorting-summary', summaryTotal_500)
# ], config=base.sessionConfig, debug=True)