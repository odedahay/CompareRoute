from google.appengine.ext import ndb
from google.appengine.api import search



class RouteDistance_api(ndb.Model):
    compare_id = ndb.StringProperty(required=True)
    user_id = ndb.StringProperty()
    created_date = ndb.DateTimeProperty(auto_now_add=True)
    starting_point = ndb.StringProperty()
    origin_destination = ndb.StringProperty()
    no_vehicle = ndb.IntegerProperty()
    current_total_dist = ndb.FloatProperty()
    proposed_total_dist = ndb.FloatProperty()
    percentage_savings = ndb.FloatProperty()
    postal_count = ndb.IntegerProperty()
    return_vehicle = ndb.StringProperty()
    vehicle_capacity = ndb.StringProperty()
    user_count = ndb.IntegerProperty(default=0)

    @classmethod
    def add_new_route_api(cls, compare_id,
                          user_id,
                          starting_point,
                          origin_destination,
                          no_vehicle,
                          vehicle_capacity,
                          current_total_dist,
                          proposed_total_dist,
                          percentage_savings,
                          postal_count,
                          return_vehicle,
                          user_count):

        route = RouteDistance_api()

        route.compare_id = compare_id
        route.user_id = user_id
        route.starting_point = starting_point
        route.origin_destination = origin_destination
        route.no_vehicle = no_vehicle
        route.vehicle_capacity = vehicle_capacity
        route.current_total_dist = current_total_dist
        route.proposed_total_dist = proposed_total_dist
        route.percentage_savings = percentage_savings
        route.postal_count = postal_count
        route.return_vehicle = return_vehicle
        route.user_count = user_count

        route.put()

        return route.key

def get_counter():
    total = 0
    for counter in RouteDistance_api.query():
        total += counter.count
    return total

class CurrentRoute_api(ndb.Model):
    compare_id = ndb.StringProperty(required=True)
    origin_code = ndb.StringProperty()
    postal_code = ndb.StringProperty()
    vehicle_id = ndb.IntegerProperty()
    latVal = ndb.StringProperty()   #FloatProperty()
    longVal = ndb.StringProperty()
    distance = ndb.FloatProperty()
    order_id = ndb.IntegerProperty()
    url_id = ndb.StringProperty()

    @classmethod
    def add_new_current_route_api(cls, compare_id, origin_code, postal_code, vehicle_id, latVal, longVal, url_id,
                                  distance, order_id):

        current = CurrentRoute_api()

        current.compare_id = compare_id
        current.origin_code = origin_code
        current.postal_code = postal_code
        current.vehicle_id = vehicle_id
        current.latVal = latVal
        current.longVal = longVal
        current.url_id = url_id
        current.distance = distance
        current.order_id = order_id

        current.put()

        return current.key

class ProposedRoute_api(ndb.Model):

    compare_id = ndb.StringProperty(required=True)
    origin_code = ndb.StringProperty()
    postal_code = ndb.StringProperty()
    vehicle_id = ndb.IntegerProperty()
    latVal = ndb.StringProperty()   #FloatProperty()
    longVal = ndb.StringProperty()
    distance = ndb.FloatProperty()
    order_id = ndb.IntegerProperty()
    url_id = ndb.StringProperty()

    @classmethod
    def add_new_proposed_route_api(cls, compare_id, origin_code, postal_code, vehicle_id, latVal, longVal, url_id,
                                   distance, order_id):

        proposed = ProposedRoute_api()

        proposed.compare_id = compare_id
        proposed.origin_code = origin_code
        proposed.postal_code = postal_code
        proposed.vehicle_id = vehicle_id
        proposed.latVal = latVal
        proposed.longVal = longVal
        proposed.url_id = url_id
        proposed.distance = distance
        proposed.order_id = order_id

        proposed.put()

        return proposed.key