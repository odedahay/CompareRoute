import webapp2
from handlers import base
from handlers import login
from handlers import profile
from handlers import resetpass
from handlers import sortingsum
from handlers import postalchecker, postal_mod
from app import search_postal
from handlers import sorting_task
from handlers.postalchecker import Postal_checkerHandler

from itertools import groupby
import urllib
import json
# - - - lib
from model.user_account import UserAccount
# DB for Admin
from model.admin_account import postalRecordDB, PostalRecordDB_alert, PostalRecordDB_history

# DB for Web App
from model.admin_account import RouteDistance, CurrentRoute, ProposedRoute

# DB for API
from model.admin_account_api import ProposedRoute_api, CurrentRoute_api, RouteDistance_api


class MainPage(base.BaseHandler):
    def get(self):

        email = self.session.get("email")

        if email:
            self.render("/compare/compare.html", email=email)
        else:
            self.render("/home/home.html")

class APIHandler(base.BaseHandler):
    def get(self):
        self.render("/api/api.html")

class APIHandler_reg(base.BaseHandler):
    def get(self):

        email = self.session.get("email")
        api_key_for_user = UserAccount.create_api_key(email)

        if email:
            self.render("/api/api2.html", email=email, api_key_for_user=api_key_for_user)
        else:
            self.render("/api/api.html")

class LoginPage(login.LoginHandler, base.BaseHandler):

    def post(self):

        # Obtain login credentials
        email = self.request.get('email')
        password = self.request.get('password')

        # Attempt to validate login credentials
        login_status = self.validateUser(email, password)
        success = login_status[0]
        msg = "Login failed! Check your credentials and try again."

        # If user is not found, send and error message
        # Else, log the user in and save email to the session

        if success == False:

            self.render("login/login.html", register_error=msg)
        else:
            self.session["email"] = email
            ws_key = login_status[0]

            self.session["ws_key"] = ws_key
            self.redirect("/compare")

class Logout(base.BaseHandler):
    def get(self):
        self.clearSession()
        self.redirect('/')

class ProfilePage(profile.ProfileHandler, base.BaseHandler):
    def get(self):

        email = self.session.get("email")
        user_account = UserAccount.check_if_exists(email)

        if email:
            ws_key = self.session.get("ws_key")
            self.render("/account_user/profile.html", email=email, ws_key=ws_key, user_account=user_account)
        else:
            self.render("/login/login.html", register_error="Please login!")

    def post(self):

        email = self.session.get("email")
        ws_key = self.session.get("ws_key")

        user_account = UserAccount.check_if_exists(email)

        # From user input:
        old_password = self.request.get("old_password")
        new_password = self.request.get("new_password")
        cfm_new_password = self.request.get("cfm_new_password")

        # Validate user credentials:
        change_password_status = self.changePassword(email, old_password, new_password, cfm_new_password)

        success = change_password_status[0]
        msg = change_password_status[1]

        #  - - - - - - - - - - - - - - - - - - routing section  - - - - - - - - - - - - - - -
        template_values = {
            'ws_key': ws_key,
            'email': email,
            'user_account': user_account
        }

        if success == False:
            self.render("/account_user/profile.html", change_password_error=msg, **template_values)
        else:
            self.render("/account_user/profile.html", change_password_success=msg, **template_values)

class ResetPassword(resetpass.New_password_Handler, base.BaseHandler):
    def get(self):

        user_id = self.request.get("id")
        user_account = UserAccount.get_by_id(int(user_id))
        email_account = user_account.email

        self.render("/account_user/resetpass.html", email_account=email_account)

    def post(self):

        # From user input:
        new_password = self.request.get("new_password")
        cfm_new_password = self.request.get("cfm_new_password")
        email_add = self.request.get("email_add")

        user_reset_password = self.reset_password(email_add, new_password)

        success = user_reset_password[0]
        msg = user_reset_password[1]
        #  - - - - - - - - - - - - - - - - - - routing section  - - - - - - - - - - - - - - -
        template_values = {
            'reset_status': msg,
            'reset_error': msg,
        }

        if success == False:
            self.render("/account_user/resetpass.html", **template_values)
        else:
            self.render("/login/login.html", login_status="Please login!")

class PostalUpdate(postalchecker.Postal_checker_add_Handler, base.BaseHandler):
    def get(self):

        # email = self.session.get("email")
        # password = self.session.get("password")
        #
        # useracounts = UserAccount.query(UserAccount.password == password).fetch()

        # if email:
        #     ws_key = self.session.get("ws_key")
        #     self.render("/account_user/profile.html", email=email, ws_key=ws_key, useracounts=useracounts)
        # else:
        #     self.render("/login/login.html", login_status="Please login!")

        postalcode = self.request.get("postalcode")

        url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + postalcode

        dist_val = urllib.urlopen(url)
        wjson = dist_val.read()
        latlong = json.loads(wjson)

        latVal = latlong['results'][0]['geometry']['location']['lat']
        lngVal = latlong['results'][0]['geometry']['location']['lng']
        #  - - - - - - - - - - - - - - - - - routing section  - - - - - - - - - - - - - -
        template_values = {
            'postalcode': postalcode,
            'latVal': latVal,
            'lngVal': lngVal,
        }

        self.render("admin/postal_add.html", **template_values)

    def post(self):

        # email = self.request.get("email")
        # ws_key = self.session.get("ws_key")

        # From user input:
        postal_code = self.request.get("postal_code")
        longtitude = self.request.get("longtitude_val")
        latitude = self.request.get("latitude_val")

        postalCheckers = PostalRecordDB_alert.query().order(-PostalRecordDB_alert.postal_code).fetch()

        # Delete the Record in Alert Message:
        compare_id = PostalRecordDB_alert.get_compare_id(postal_code)

        delete_data = PostalRecordDB_alert.delete_postal_records(compare_id)
        delete_data.key.delete()

        # update Postal Code records:
        update_postalcode_error = self.update_postalcode_db(postal_code, longtitude, latitude)

        success = update_postalcode_error[0]
        msg = update_postalcode_error[1]

        #  - - - - - - - - - - - - - - - - - routing section  - - - - - - - - - - - - - -
        template_values = {
            'update_postalcode_error': msg,
            'update_postalcode_success': msg,
            'postalCheckers': postalCheckers
        }

        if success == False:
            self.render('admin/postal_add.html', **template_values)
        else:
            self.render('admin/admin_alert.html', **template_values)

class Postal_add_global(postalchecker.Postal_checker_add_Handler, base.BaseHandler):
    def get(self):

        postalcode = self.request.get("postalcode")

        template_values = {
            'postalcode': postalcode,
        }

        self.render("admin/postal_add_global.html", **template_values)

    # def post(self):
    #     # Need to validate this scripts, below:
    #
    #     # email = self.request.get("email")
    #     # ws_key = self.session.get("ws_key")
    #
    #     # From user input:
    #     postalcode = self.request.get("postal_code")
    #     longtitude = self.request.get("longtitude_val")
    #     latitude = self.request.get("latitude_val")
    #
    #     # print postal_code, longtitude, latitude
    #
    #     # update Postal Code records:
    #     update_postalcode_error = self.update_postalcode_db(postalcode, longtitude, latitude)
    #
    #     results = postalRecordDB.query().order(postalRecordDB.postal_code).fetch(10)
    #     postalCheckers = PostalRecordDB_alert.query().order(-PostalRecordDB_alert.postal_code).fetch()
    #     postalHistory = PostalRecordDB_history.query().order(-PostalRecordDB_history.postal_code).fetch()
    #
    #     success = update_postalcode_error[0]
    #     msg = update_postalcode_error[1]
    #
    #     if success == False:
    #         self.render('admin/postal_add.html', update_postalcode_error=msg)
    #     else:
    #         self.render('admin/uploader.html', update_postalcode_success=msg, results=results,
    #                     postalCheckers=postalCheckers, postalHistory=postalHistory)

class PostalAdded_move(postalchecker.Postal_move_Handler, base.BaseHandler):

    def get(self):

        compare_id = self.request.get("compare_id")
        postalCheckers = PostalRecordDB_alert.query(PostalRecordDB_alert.compare_id==compare_id).fetch(1)

        self.render("admin/postal_move.html", postalCheckers=postalCheckers)

    def post(self):

        # email = self.request.get("email")
        # ws_key = self.session.get("ws_key")

        compare_id = self.request.get("compare_id")
        created_date = self.request.get("created_date")
        user_email = self.request.get("user_email")
        postal_code = self.request.get("postal_code")

        # update Postal Code records:
        update_postalcode = self.move_postalcode_db(compare_id, created_date, user_email, postal_code)

        postalCheckers = PostalRecordDB_alert.query().order(-PostalRecordDB_alert.postal_code).fetch()

        success = update_postalcode[0]
        msg = update_postalcode[1]

        #  - - - - - - - - - - - - - - - - - routing section  - - - - - - - - - - - - - -
        template_values = {
            'update_postalcode_error': msg,
            'update_postalcode_success': msg,
            'postalCheckers': postalCheckers,
        }

        if success == False:
            self.render('admin/postal_move.html', **template_values)
        else:
            self.render('admin/admin_alert.html', **template_values)

class PostalAdded_checker(postalchecker.Postal_checker_Handler, base.BaseHandler):

    def get(self):

        compare_id = self.request.get("compare_id")
        postalCheckers = PostalRecordDB_alert.query(PostalRecordDB_alert.compare_id == compare_id).get()

        template_values = {
            'postalCheckers': postalCheckers
        }
        self.render("admin/postal_checker.html", **template_values)

    def post(self):

        # email = self.request.get("email")
        # ws_key = self.session.get("ws_key")

        #compare_id = self.request.get("compare_id")
        postal_code = self.request.get("postal_code")

        # update Postal Code records:
        update_postalcode, error_postalcode, status = self.check_postalcode(postal_code)

        success = status[0]
        msg = status[1]

        postal_error = error_postalcode[0]

        longtitude = update_postalcode[1]
        latitude = update_postalcode[0]

        postalCheckers = PostalRecordDB_alert.query().order(-PostalRecordDB_alert.postal_code).fetch(1)
        postalHistory = PostalRecordDB_history.query().order(-PostalRecordDB_history.postal_code).fetch()

        template_values1 = {
            'longtitude': longtitude,
            'latitude': latitude,
            'update_postalcode_error': msg,
            'update_postalcode_success': msg,
            'postal_error': postal_error,
            'postalCheckers': postalCheckers,
            'postalHistory': postalHistory
        }

        if success == False:
            self.render('admin/postal_checker.html', **template_values1)
        else:
            self.render('admin/postal_checker.html', **template_values1)


class PostalAdded_arch(postalchecker.Postal_move_Handler, base.BaseHandler):
    def get(self):

        postalHistory = PostalRecordDB_history.query().fetch()

        self.render("admin/admin_archive.html", postalHistory=postalHistory)

class Postal_Search(postalchecker.Postal_move_Handler, base.BaseHandler):
     def get(self):

        postal_key = postalRecordDB.check_if_exists('q')
        postal = postalRecordDB.get_all_postalcode(postal_key)
        #  - - - - - - - - - - - - - - - - - routing section  - - - - - - - - - - - - - -
        tpl_values = {
            'postal': postal
        }
        self.render('admin/admin_search_postal.html', **tpl_values)


class AdminHome_page(base.BaseHandler):
    def get(self):

        email = self.session.get("email")

        web_routes = RouteDistance.query().order(-RouteDistance.created_date).fetch()
        web_temp = []
        for user in web_routes:
            web_user_id = user.user_id
            web_temp.append(str(web_user_id))

        web_id_counts_id = [(k, len(list(g))) for k, g in groupby(sorted(web_temp))]
        #  - - - - - - - - - - - - - - - API Commands  - - - - - - - - - - - - - - - - - - -
        api_routes = RouteDistance_api.query().order(-RouteDistance_api.created_date).fetch()
        api_temp = []
        for user in api_routes:
            user_id = user.user_id
            api_temp.append(str(user_id))

        api_id_counts_id = [(k, len(list(g))) for k, g in groupby(sorted(api_temp))]

        #  - - - - - - - - - - - - - - - - - - routing section  - - - - - - - - - - - - - - -
        template_values = {
            'email': email,
            'web_id_counts_id': web_id_counts_id,
            'api_id_counts_id': api_id_counts_id,
            'web_routes': web_routes,
            'api_routes': api_routes
        }
        self.render("admin/admin.html", **template_values)

# This class is for groupings
class AdminHome_page1(base.BaseHandler):
    def get(self):

        email = self.session.get("email")
        user_id = self.request.get("user_id")

        # Profile Records display in /admin1
        profile = UserAccount.check_if_exists(user_id)

        # User_Id
        web_routes_user_id = RouteDistance.query(RouteDistance.user_id == user_id).order(
            -RouteDistance.created_date).fetch()

        # Counting
        results = RouteDistance.query(RouteDistance.user_id == user_id).order().fetch()
        web_temp =[]
        for x in range(len(results)):
            user_sequence = results[x]
            web_temp.append(user_sequence.user_id)
        web_number_of_usage = len(web_temp)

        #  - - - - - - - - - - - - - - - - - - API Commands  - - - - - - - - - - - - - - - - - - -
        # User_Id

        api_routes_user_id = RouteDistance_api.query(RouteDistance_api.user_id == user_id).order(
            -RouteDistance_api.created_date).fetch()

        # Counting
        api_results = RouteDistance_api.query(RouteDistance_api.user_id == user_id).order().fetch()

        api_temp =[]
        for x in range(len(api_results)):
            user_sequence_api = api_results[x]
            api_temp.append(user_sequence_api.user_id)

        api_number_of_usage = len(api_temp)
        #  - - - - - - - - - - - - - - - - - - routing section  - - - - - - - - - - - - - - - - - - #
        template_values = {
            'email': email,
            'profile': profile,
            'web_routes_user_id': web_routes_user_id,
            'web_number_of_usage': web_number_of_usage,
            'api_routes_user_id': api_routes_user_id,
            'api_number_of_usage': api_number_of_usage,
        }
        self.render("admin/admin1.html", **template_values)

class AdminSummary(base.BaseHandler):
    def get(self):
        compare_id = self.request.get("compare_id")
        email = self.session.get("email")

        web_current = CurrentRoute.query(CurrentRoute.compare_id == compare_id).order(
                                                                                    CurrentRoute.vehicle_id,
                                                                                    CurrentRoute.order_id).fetch()
        web_proposed = ProposedRoute.query(ProposedRoute.compare_id == compare_id).order(
                                                                                    ProposedRoute.vehicle_id,
                                                                                    ProposedRoute.order_id).fetch()
        web_routes = RouteDistance.query(RouteDistance.compare_id == compare_id).order(
                                                                                    -RouteDistance.created_date).fetch()

        # User_Id
        # web_routes_user_id = RouteDistance.query(RouteDistance.compare_id == compare_id).order(
        #     -RouteDistance.created_date).fetch()

        #  - - - - - - - - - - - - - - - - - - routing section  - - - - - - - - - - - - - - - - - - #
        template_values1 = {
            'email': email,
            'web_routes': web_routes,
            'web_proposed': web_proposed,
            'web_current': web_current,
            # 'web_routes_user_id': web_routes_user_id,
        }
        self.render("admin/admin-summary.html", **template_values1)

class AdminSummary_api(base.BaseHandler):
    def get(self):
        compare_id = self.request.get("compare_id")
        email = self.session.get("email")

        # API User
        api_routes = RouteDistance_api.query(RouteDistance_api.compare_id == compare_id).order(
                                                                                        -RouteDistance_api.created_date
                                                                                        ).fetch()
        api_current = CurrentRoute_api.query(CurrentRoute_api.compare_id == compare_id).order(
                                                                                        CurrentRoute_api.vehicle_id,
                                                                                        CurrentRoute_api.order_id
                                                                                        ).fetch()
        api_proposed = ProposedRoute_api.query(ProposedRoute_api.compare_id == compare_id).order(
                                                                                        ProposedRoute_api.vehicle_id,
                                                                                        ProposedRoute_api.order_id
                                                                                        ).fetch()
        #  - - - - - - - - - - - - - - - - - - routing section  - - - - - - - - - - - - - - - - - -
        template_values = {
            'email': email,
            'api_routes': api_routes,
            'api_current': api_current,
            'api_proposed': api_proposed,
        }
        self.render("admin/admin_summary_api.html",  **template_values)

app = webapp2.WSGIApplication([
      ('/', MainPage),
      ("/login", LoginPage),
      ('/reset', ResetPassword),
      ('/register', 'app.register.RegisterHandler'),
      ('/compare', 'app.compare.ComparePage'),
      ('/compare-data', 'handlers.user_data.User_Data'),
      ('/compare-data-list', 'handlers.user_data.User_Data_list'),
      ('/compare-api', APIHandler_reg),
      ('/compare-profile', ProfilePage),
      ("/api", APIHandler),
      ("/recover", 'app.recover_psswrd.PasswordRecover'), # This is for setting for reset password:
      ('/logout', Logout),
      ('/admin-csv', 'app.csv_upload.MainHandler3'),
      ('/admin-csv-load', 'app.csv_upload.UploadHandler'),
      ('/admin/gcsupload', 'app.csv_upload.UploadGCSData'),
      ('/sorting-proposed', 'handlers.sorting_task.TaskRouteHandlerProposed'),
      # ('/summary-result', 'handlers.sorting_task.summaryTotal_500'),
      ('/sorting-proposed-api', 'handlers.sorting_task_api.TaskRouteHandlerProposed_api'),
      ('/account/<user_id:[0-9]+>/confirm/confirmation_code:[a-z0-9]{32}>', 'app.register.ConfirmUser'),
      ('/admin', AdminHome_page),
      ('/admin1', AdminHome_page1),
      ('/admin-summary', AdminSummary),
      ('/admin-summary-api', AdminSummary_api),
      ('/admin-credits', 'app.user_credits.summaryCredits'),
      ('/admin-credits-edit', 'app.user_credits.summaryCredits_edit'),
      ('/summary-details', sortingsum.SummaryBMapHandler),
      ('/admin-csv-taskq', 'app.csv_upload.TaskqHandler'),
      ('/admin-postalcode', 'handlers.postalchecker.Postal_checkerHandler'),
      ('/admin-postalcode-chk', PostalAdded_checker),
      ('/admin-postalcode-add', PostalUpdate),
      ('/admin-postalcode-add/global', Postal_add_global),
      ('/admin-postalcode-gnew', 'handlers.postal_mod.Add_new_postal'),
      ('/admin-postalcode-move', PostalAdded_move),
      ('/admin-postalcode-arch', PostalAdded_arch),
      ('/admin-postalcode-search', Postal_Search),
      ('/admin-search', 'app.search_postal.SearchPostal'),
      ('/admin-search-del', 'app.search_postal.PostalDelete_Handler'),
      ('/admin-search-edit', 'app.search_postal.PostalEdit_Handler')

], config=base.sessionConfig, debug=True)