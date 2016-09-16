from framework.request_handler import CompareRouteHandler


class Home(CompareRouteHandler):
    def get(self):
        self.render('/index.html')


class AboutUs(CompareRouteHandler):
    pass



