import webapp2
from model.user_account import UserAccount
from encryption import EncryptionHandler

class RegisterHandler(webapp2.RequestHandler):
    
    def registerUser(self, email, password):
        # Trim out whitespaces
        email = email.lower().strip()
        
        # Status for the registration
        status = []
        success = True # Must be true for my if-else logic
        msg = ""
        
        # Validate the email to ensure it contains one "@" and ends with ".com"
        if email.count("@") != 1 or email[-4:] != ".com":
            success = False
            msg = "Invalid email"
        
        # Validate the password for length of 8
        if len(password) < 6:
            success = False
            if msg:
                msg += "/password"
            else:
                msg = "Invalid password"
        
        # If success is false, return the status
        # Else, check if the user exists
        if success == False:
            status.append(success)
            status.append(msg)
            return status
        else:
            # If there is an existing user with the same email in the DataStore, send an error message
            # Else, register the user
            userRecord = UserAccount.query(UserAccount.email == email).fetch()

            if len(userRecord) != 0:
                success = False
                msg = "Email already exists!"
                status.append(success)
                status.append(msg)
                return status
            else:
                # Generate the password hash and web service Key
                enc = EncryptionHandler()
                password_hash = enc.createPasswordHash(password)
                ws_key = enc.createWebServiceKey(password_hash)
                
                # Create user object and insert into Datastore
                user = UserAccount()
                user.email = email
                user.password = password_hash
                user.ws_key = ws_key
                user.put()
                
                # Return the status
                success = True
                msg = "Registration successful!"
                status.append(success)
                status.append(msg)
                return status