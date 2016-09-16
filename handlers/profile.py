import webapp2
from model.user_account import UserAccount

class ProfileHandler(webapp2.RequestHandler):
    
    def changePassword(self, email, old_password, new_password, cfm_new_password):
        # Status for change password
        status = []
        success = False
        msg = ""

        userPassword = UserAccount.check_password(email, old_password)

        # If user does not exist, send an error message
        if userPassword == None:
            success = False
            msg = "Wrong old password!"
            status.append(success)
            status.append(msg)

            return status
        else:
            # Else, log the user in
            # Find userRecord:
            userRecord = UserAccount.query(UserAccount.email == email).get()

            # Generate password hash from password input
            newHashed_password = UserAccount.createHashed_password(cfm_new_password)

            # Update the DataStore
            userRecord.password = newHashed_password
            userRecord.put()

            success = True
            msg = "Password changed!"
            status.append(success)
            status.append(msg)
            return status