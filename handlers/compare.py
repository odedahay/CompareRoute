from handlers import base
from model.user_account import UserAccount

class ComparePage(base.BaseHandler):
    def get(self):

        # self.render("/compare/compare.html")
        email = self.session.get("email")
        admin_user = UserAccount.is_admin(email)

        if email:
            self.render("/compare/compare.html", email=email, admin_user=admin_user)
        else:
            self.render("/login/login.html", register_error="Please login!")



