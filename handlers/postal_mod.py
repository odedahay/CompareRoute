from framework.request_handler import CompareRouteHandler
from model.admin_account import postalRecordDB


class Add_new_postal(CompareRouteHandler):
    def get(self):
        self.render('admin/postal_new_global.html')

    def post(self):

        # Get the data from form:
        postal_code = self.request.get("postal_code")
        longtitude = self.request.get("longtitude_val")
        latitude = self.request.get("latitude_val")

        print postal_code, longtitude, latitude
        msg =""
        status = []

        if len(postal_code) != 6:
            success = False
            msg = "Invalid Postal Code"

            status.append(success)
            status.append(msg)
            return status
        else:

            # update Postal Code records:
            updateStatus = postalRecordDB.add_new_records(postal_code, longtitude, latitude)
            updateStatus = updateStatus.id()

            print('new_postal_code'), updateStatus
            new_postal_code = postalRecordDB.get_by_id(updateStatus)

            print('new_postal_code'), new_postal_code

            if new_postal_code == None:
                success = False
                msg = "No Postal Code Added"

            else:
                success = True
                msg = "New Postal Code successful added"

        if success == False:
            self.render('admin/postal_new_global.html', postal_update_error=msg)
        else:
            self.render('admin/postal_new_global.html', postal_update_success=msg)


    # def get(self):
    #
    #     postal_code = self.request.get("postal_code")
    #     longtitude = self.request.get("longtitude_val")
    #     latitude = self.request.get("latitude_val")
    #
    #     postal_status_update = self.updating_postal(postal_code, longtitude, latitude)
    #     success = postal_status_update[0]
    #     msg = postal_status_update[1]
    #
    #     if success == False:
    #
    #         self.render('admin/postal_new_global.html', postal_update_error=msg)
    #     else:
    #         self.render('admin/postal_new_global.html', postal_update_success=msg)
    #
    # def updating_postal(self, postal_code, longtitude, latitude):
    #
    #         status = []
    #
    #         if len(postal_code) != 6:
    #             success = False
    #             msg = "Invalid Postal Code"
    #
    #             status.append(success)
    #             status.append(msg)
    #             return status
    #         else:
    #             # Update Postal Code records:
    #             postalRecordDB.add_new_records(postal_code, longtitude, latitude)
    #
    #             success = False
    #             msg = "Successful"
    #
    #             status.append(success)
    #             status.append(msg)
    #             return status



