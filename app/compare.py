import webapp2
from handlers import base

class ComparePage(base.BaseHandler):
    def get(self):

        # self.render("/compare/compare.html")

        email = self.session.get("email")

        if email:
            self.render("/compare/compare.html", email=email)
        else:
            self.render("/login/login.html", register_error="Please login!")



