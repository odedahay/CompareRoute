from handlers import base
from model.admin_account_api import ProposedRoute_api, CurrentRoute_api, RouteDistance_api
from handlers.postalchecker import postalRecordDB
import urllib
import json
import sorting


class TaskRouteHandlerProposed_api(base.BaseHandler):
    def post(self):

        if not 'X-AppEngine-TaskName' in self.request.headers:
            self.error(403)

        compare_id = self.request.get('compare_id')
        starting_address = self.request.get('starting_address')
        #origin_destination = self.request.get('origin_destination')
        num_of_vehicle = self.request.get('num_of_vehicle')
        vehicle_capacity = self.request.get('vehicle_capacity')
        email = self.request.get('email')
        has_return = self.request.get('has_return')
        num_user_load = self.request.get('num_user_load')

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
        # Counter Sign ##
        if num_user_load == "true":
            user_count += 1

        # Total Percentage Saving
        difference_total = current_total_dist - proposed_total_dist
        percentage_savings = (difference_total / current_total_dist) * 100

        RouteDistance_api.add_new_route_api(compare_id, email,
                                            starting_address,
                                            origin_destination,
                                            int(num_of_vehicle),
                                            vehicle_capacity,
                                            float(current_total_dist),
                                            float(proposed_total_dist),
                                            round(percentage_savings, 2), int(postal_count), return_vehicle, int(user_count))

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

                    ProposedRoute_api.add_new_proposed_route_api(compare_id, starting_address, current_post, int(vehicle_count), longval, latval, url_id, round(float(distance_km), 2), int(postal_rank))
                else:
                    ProposedRoute_api.add_new_proposed_route_api(compare_id, origin_postcode, current_post, int(vehicle_count), longval, latval, url_id, round(float(distance_km), 2), int(postal_rank))

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

                    CurrentRoute_api.add_new_current_route_api(compare_id, starting_address, current_post, int(vehicle_count), latval, longval, url_id, round(float(distance_km2), 2), int(postal_rank))
                else:
                    CurrentRoute_api.add_new_current_route_api(compare_id, origin_postcode, current_post, int(vehicle_count), latval, longval, url_id, round(float(distance_km2), 2), int(postal_rank))

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
