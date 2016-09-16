import webapp2
from handlers import base
from model.user_account import UserAccount

# DB for Web App
from model.admin_account import RouteDistance, CurrentRoute, ProposedRoute


class User_Data(base.BaseHandler):
    def get(self):

        email = self.session.get("email")
        # User Records display in /compare_data.html
        user_accounts = UserAccount.check_if_exists(email)

        print('user_accounts'), user_accounts
        user_id = user_accounts.email

        # Profile Records display in /admin1
        user_profile = UserAccount.check_if_exists(email)

        # Retrieved History of User_Id
        user_routes_data = RouteDistance.query(RouteDistance.user_id == user_id).order(
                                                                                -RouteDistance.created_date).fetch()

        template_values = {
            'email': email,
            'user_profile': user_profile,
            'user_routes_data': user_routes_data,
        }

        if email:
            # ws_key = self.session.get("ws_key")
            self.render("/compare/compare_data.html", **template_values)
        else:
            self.render("/login/login.html", register_error="Please login!")

class User_Data_list(base.BaseHandler):
    def get(self):

        email = self.session.get("email")
        compare_id = self.request.get("compare_id")

        web_current = CurrentRoute.query(CurrentRoute.compare_id == compare_id).order(
            CurrentRoute.vehicle_id,
            CurrentRoute.order_id).fetch()

        web_proposed = ProposedRoute.query(ProposedRoute.compare_id == compare_id).order(
            ProposedRoute.vehicle_id,
            ProposedRoute.order_id).fetch()

        web_routes = RouteDistance.query(RouteDistance.compare_id == compare_id).order(
            -RouteDistance.created_date).fetch()

        template_values = {
            'email': email,
            'web_current': web_current,
            'web_proposed': web_proposed,
            'web_routes': web_routes,
        }

        if email:
            self.render("/compare/compare_data_list.html", **template_values)
        else:
            self.render("/login/login.html", register_error="Please login!")