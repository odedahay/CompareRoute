from framework.request_handler import CompareRouteHandler
from model.admin_account import postalRecordDB, PostalRecordDB_alert, PostalRecordDB_history
from google.appengine.api import search


class SearchPostal(CompareRouteHandler):
    def get(self):

        query = self.request.get('q')
        compare_postal = postalRecordDB.check_if_exists(query)
        msg = ""

        if compare_postal == None:
            # if query != '':
            #     notfound = "Search not found"

            errormsg = "No postal record found"
            self.render('admin/search.html', errormsg=errormsg)
        else:
            # index = search.Index('postal')
            # snippet = 'snippet("%s", latitude, 140)' % query

            # options = search.QueryOptions(
            #         returned_expressions=[
            #             search.FieldExpression(name='snippet', expression=snippet)
            #         ]
            #     )
            # results = index.search(
            #     query=search.Query(
            #         query_string=query,
            #         options=options,
            #     )
            # )

            # noresult
            # docs = []
            # if results:
            #     docs = results.results
            postal_records = postalRecordDB.get_by_id(compare_postal)
            results = postalRecordDB.query(postalRecordDB.postal_code >= postal_records.postal_code).order().fetch(10)
            #  - - - - - - - - - - - - - - - - - - routing section  - - - - - - - - - - - - - - - - - -
            tpl_values = {
                    'query': query,
                    'results': results
                }
            self.render('admin/search.html', **tpl_values)

class PostalDelete_Handler(CompareRouteHandler):

    def get(self):

        postal_code = self.request.get("postal_code")
        results = postalRecordDB.query(postalRecordDB.postal_code == postal_code).order().fetch(1)

        self.render("admin/postal_delete.html", results=results)

    def post(self):

        postal_code = self.request.get("postal_code")

        # long = self.request.get("long_val")
        # lat = self.request.get("lat_val")

        # update Postal Code records:
        del_postalcode = self.postalcode_db(postal_code)

        success = del_postalcode[0]
        msg = del_postalcode[1]

        if success == False:
            self.render('admin/postal_delete.html', update_postalcode_erro=msg)
        else:
            self.redirect("/admin-postalcode-search?title='%s' "%msg)
            # self.render('admin/postal_delete.html', update_postalcode_success=msg)

    def postalcode_db(self, postal_code):

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
            print('postal_code'), postal_code
            # Delete in DB
            # postalRecordDB.add_new_records(postal_code, long, lat)

            # Delete the Postal Code in DB
            delete_data = postalRecordDB.delete_postal_records(postal_code)
            delete_data.key.delete()

            success = True
            msg = "Successful"
            status.append(success)
            status.append(msg)

            return status

class PostalEdit_Handler(CompareRouteHandler):
    def get(self):
        postal_code = self.request.get("postal_code")
        postal_edit = postalRecordDB.query(postalRecordDB.postal_code == postal_code).get()

        self.render("admin/postal_edit.html", postal_edit=postal_edit)

    def post(self):

        postal_code = self.request.get("postal_code")
        lat_val = self.request.get("lat_val")
        long_val = self.request.get("long_val")

        postal_edit = postalRecordDB.query(postalRecordDB.postal_code == postal_code).get()

        postal_edit.postal_code = postal_code
        postal_edit.lat = lat_val
        postal_edit.long = long_val
        postal_edit.put()

        #msg = "Successful"
        #self.render("admin/postal_edit.html", postal_edit=postal_edit)

        self.redirect("/admin-postalcode-search")







