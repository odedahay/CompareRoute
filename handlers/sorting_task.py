# Date and time
from datetime import datetime
from handlers import base
from model.admin_account import ProposedRoute
from model.admin_account import CurrentRoute
from model.admin_account import RouteDistance

from model.admin_account import postalRecordDB, PostalRecordDB_alert, Truck_capacity_details
import json

import sorting
import itertools
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

        proposedPostlal = self.request.get('proposedPostlal')
        currentdPostlal = self.request.get('currentdPostlal')

        proposed_order_grp = self.request.get('proposed_order_grp')
        current_order_grp = self.request.get('current_order_grp')

        proposed_cargo_grp = self.request.get('proposed_cargo_grp')
        current_cargo_grp = self.request.get('current_cargo_grp')

        priority_capacity = self.request.get('priority_capacity')
        sort_company = self.request.get('sort_company')

        grp_truck_name = self.request.get('grp_truck_name')

        origin_destination = sorting.startingpoint_latlong(starting_address)

        # two function for proposed and current route storing data
        proposed_total_dist = self.task_proposed_Route(compare_id, starting_address, proposedPostlal, origin_destination, email, proposed_order_grp, proposed_cargo_grp)
        current_total_dist = self.task_current_Route(compare_id, starting_address, currentdPostlal, origin_destination, current_order_grp, current_cargo_grp)

        # Counting the number of postal code:
        actual_vehicle_postal = proposedPostlal.split("_")
        postal_count_arr = []

        for vehicle_postal in actual_vehicle_postal:
            vehicle_postal = vehicle_postal.split(", ")

            for current_post in vehicle_postal:
                postal_count_arr.append(current_post)

        postal_count = len(postal_count_arr)

        # indicator for type of optimize route
        type_optimise = ""

        if priority_capacity == "true":
            # Name will appear at /compare-data
            type_optimise = "Maximizing Truck Capacity"

            # customise event-handler truck capacity
            optimise_id = 2

            # name of the truck:
            grp_truck_name = grp_truck_name.split(", ")
            actual_vehicle_postal = proposedPostlal.split("_")

            truck_count = 0
            for truck_name, countList in itertools.izip(grp_truck_name, actual_vehicle_postal):
                count_item = countList.split(", ")
                delivery_routes = len(count_item)

                # counting the number of truck
                truck_count += 1

                # store the truck details
                Truck_capacity_details.add_truck_details(compare_id, int(truck_count), truck_name, delivery_routes)

        elif sort_company == "true":

            # Name will appear at /compare-data
            type_optimise = "Consolidated Delivery for Multiple Companies"

            # customise event-handler truck capacity
            optimise_id = 3

        else:

            # Name will appear at /compare-data
            type_optimise = "Multiple Trucks"

            # Customise event-handler Multiple Trucks
            optimise_id = 1

            truck_count = 0
            for countList in actual_vehicle_postal:

                count_item = countList.split(", ")
                delivery_routes = len(count_item)

                # counting the number of truck
                truck_count += 1
                truck_name = "None"

                # store the truck details
                Truck_capacity_details.add_truck_details(compare_id, int(truck_count), truck_name, delivery_routes)

        # Indicator for Returning vehicle
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

        RouteDistance.add_new_route(compare_id, email, starting_address,
                                    origin_destination,
                                    int(num_of_vehicle),
                                    vehicle_capacity,
                                    float(current_total_dist),
                                    float(proposed_total_dist),
                                    round(percentage_savings, 2),
                                    int(postal_count),
                                    return_vehicle,
                                    int(user_count),
                                    type_optimise, optimise_id)

    def task_proposed_Route(self, compare_id, starting_address, proposedPostlal, origin_destination, email, proposed_order_grp, proposed_cargo_grp):

        actual_vehicle_postal = proposedPostlal.split("_")
        proposed_order_array = proposed_order_grp.split("_")
        proposed_cargo_grp = proposed_cargo_grp.split("_")

        origin_postcode = starting_address
        origin_destination = origin_destination

        vehicle_count = 0
        proposed_total_dist = 0

        for vehicle_postal, order_array, cargo_array in itertools.izip(actual_vehicle_postal, proposed_order_array, proposed_cargo_grp):

            print "vehicle_postal", vehicle_postal

            vehicle_count += 1

            vehicle_postal = vehicle_postal.split(", ")
            order_array = order_array.split(", ")
            cargo_array = cargo_array.split(", ")

            postal_rank = 0

            for proposed_post, order_id, cargo_unit in itertools.izip(vehicle_postal, order_array, cargo_array):

                postal_rank += 1

                destinations, latval, longval = self.postalcode_latlong(proposed_post, compare_id, email)

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

                    ProposedRoute.add_new_proposed_route(compare_id, starting_address, proposed_post, int(vehicle_count), longval, latval, url_id, round(float(distance_km), 2), int(postal_rank), order_id, cargo_unit)
                else:
                    ProposedRoute.add_new_proposed_route(compare_id, origin_postcode, proposed_post, int(vehicle_count), longval, latval, url_id, round(float(distance_km), 2), int(postal_rank), order_id, cargo_unit)

                origin_postcode = proposed_post

        return proposed_total_dist

    def task_current_Route(self, compare_id, starting_address, currentdPostlal, origin_destination, current_order_grp, current_cargo_grp):

        current_vehicle_postal = currentdPostlal.split("_")
        current_order_array = current_order_grp.split("_")
        current_cargo_array = current_cargo_grp.split("_")

        origin_postcode = starting_address
        origin_destination1 = origin_destination

        vehicle_count = 0
        current_total_dist = 0

        for vehicle_postal, order_array, cargo_array in itertools.izip(current_vehicle_postal, current_order_array, current_cargo_array):
            vehicle_count += 1

            vehicle_postal = vehicle_postal.split(", ")
            order_array = order_array.split(", ")
            cargo_array = cargo_array.split(", ")

            postal_rank = 0

            for current_post, order_id, cargo_unit in itertools.izip(vehicle_postal, order_array, cargo_array):

                postal_rank += 1

                # Convert to Lat-Long the postal code
                destinations, latval, longval = self.postalcode_latlong_current(current_post)

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

                # Storing data for Current Route
                if (postal_rank == 1):

                    CurrentRoute.add_new_current_route(compare_id, starting_address, current_post, int(vehicle_count), latval, longval, url_id, round(float(distance_km2), 2), int(postal_rank), order_id, cargo_unit)
                else:
                    CurrentRoute.add_new_current_route(compare_id, origin_postcode, current_post, int(vehicle_count), latval, longval, url_id, round(float(distance_km2), 2), int(postal_rank), order_id, cargo_unit)

                origin_postcode = current_post

        return current_total_dist

    # To check weather the Postal Code is exits:
    def postalcode_latlong(self, current_post, compare_id, email):

        # Time recording only
        currentDateTime = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        counter_no = 0

        # Validation for Task Q
        compare_postal = postalRecordDB.check_if_exists(current_post)

        if compare_postal == None:

            counter_no += 1

            if current_post[0] == "0":
                current_post = current_post.lstrip("0")
                compare_postal = postalRecordDB.check_if_exists(current_post)

            else:
                print('No Postal Code Record')

                print "current_post", current_post

                PostalRecordDB_alert.add_new_postal_records(compare_id, current_post, email, currentDateTime, int(counter_no))

                nearestPostalCode = postalRecordDB.query().filter(postalRecordDB.postal_code >= current_post).get(keys_only=True)
                compare_postal = nearestPostalCode.id()

        latlong = postalRecordDB.get_by_id(compare_postal)


        print "destinations", latlong

        laglongSource = []
        laglongSource.append(latlong.lat)
        laglongSource.append(',')
        laglongSource.append(latlong.long)
        destinations = ''.join(laglongSource)

        latval = latlong.lat
        longval = latlong.long

        return destinations, latval, longval

    def postalcode_latlong_current(self, current_post):

        # Validation for Task Q
        compare_postal = postalRecordDB.check_if_exists(current_post)

        if compare_postal == None:

            if current_post[0] == "0":
                current_post = current_post.lstrip("0")
                compare_postal = postalRecordDB.check_if_exists(current_post)

            else:
                print('No Postal Code Record')

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