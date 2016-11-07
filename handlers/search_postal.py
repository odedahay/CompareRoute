from framework.request_handler import CompareRouteHandler
from handlers import base
from model.admin_account import postalRecordDB
from model.user_account import UserAccount


class SearchPostal(base.BaseHandler):
    def get(self):

        email = self.session.get("email")
        admin_user = UserAccount.is_admin(email)

        if admin_user:
            query = self.request.get('q')

            compare_postal = postalRecordDB.check_if_exists(query)
            errormsg = ""

            if query == '':
                errormsg += "Search not found"
                self.render('admin/search.html', errormsg=errormsg)

            elif compare_postal == None:

                errormsg += query+" has no Postal Code record"
                self.render('admin/search.html', errormsg=errormsg)

            else:

                postal_records = postalRecordDB.get_by_id(compare_postal)
                results = postalRecordDB.query(postalRecordDB.postal_code >= postal_records.postal_code).order().fetch(10)

                #  - - - - - - - - - - - - - - - - - - routing section  - - - - - - - - - - - - - - - - - -
                tpl_values = {
                        'admin_user': admin_user,
                        'email': email,
                        'query': query,
                        'results': results
                    }
                self.render('admin/search.html', **tpl_values)

        else:

            # if not admin access
            self.redirect("/compare")

class PostalDelete_Handler(base.BaseHandler):

    def get(self):

        email = self.session.get("email")
        admin_user = UserAccount.is_admin(email)

        if admin_user:

            postal_code = self.request.get("postal_code")
            results = postalRecordDB.query(postalRecordDB.postal_code == postal_code).order().fetch(1)

            tpl_values = {
                'admin_user': admin_user,
                'email': email,
                'results': results
            }

            self.render("admin/admin_postal_delete.html", **tpl_values)

        else:

            # if not admin access
            self.redirect("/compare")

    def post(self):

        postal_code = self.request.get("postal_code")

        # long = self.request.get("long_val")
        # lat = self.request.get("lat_val")

        # update Postal Code records:
        del_postalcode = self.postalcode_db(postal_code)

        success = del_postalcode[0]
        msg = del_postalcode[1]

        if success == False:

            self.render('admin/admin_postal_delete.html', update_postalcode_erro=msg)

        else:

            self.redirect("/admin-search?title='%s' "%msg)

    def postalcode_db(self, postal_code):

        # Status of postal code added
        status = []
        success = False
        msg = ""

        if not postal_code:
            success = False
            msg += "Please check the Postal code"
            status.append(success)
            status.append(msg)

            return status

        else:
            print('postal_code'), postal_code
            # Delete in DB
            # postalRecordDB.add_new_records(postal_code, long, lat)

            # Delete the Postal Code in DB
            delete_data = postalRecordDB.delete_postal_records(postal_code)
            delete_data.key.delete()

            success = True
            msg += "Successful"
            status.append(success)
            status.append(msg)

            return status

class PostalEdit_Handler(base.BaseHandler):
    def get(self):

        email = self.session.get("email")
        admin_user = UserAccount.is_admin(email)

        if admin_user:

            postal_code = self.request.get("postal_code")
            postal_edit = postalRecordDB.query(postalRecordDB.postal_code == postal_code).get()

            self.render("admin/admin_postal_edit.html", postal_edit=postal_edit, postal_code=postal_code, email=email, admin_user=admin_user)

        else:

            # if not admin access
            self.redirect("/compare")

    def post(self):

        postal_code = self.request.get("postal_code")
        lat_val = self.request.get("lat_val")
        long_val = self.request.get("long_val")

        postal_edit = postalRecordDB.query(postalRecordDB.postal_code == postal_code).get()

        postal_edit.postal_code = postal_code
        postal_edit.lat = lat_val
        postal_edit.long = long_val
        postal_edit.put()

        # Return to search page:
        self.redirect("/admin-search?q="+postal_code)









