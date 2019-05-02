import webapp2
from jinja import JINJA_ENVIRONMENT
from google.appengine.api import users


class ErrorHandler(webapp2.RequestHandler):

    def get(self):
        self.user = users.get_current_user()

        if self.user:
            try:
                msg = self.request.GET['msg']
            except KeyError:
                msg = None

            if not msg:
                msg = "CRITICAL - contact development team"

            template_values = {
                'usuario': self.user.nickname(),
                'desconect': users.create_logout_url('/'),
                "error_msg": msg
            }

            template = JINJA_ENVIRONMENT.get_template("/Templates/error.html")
            self.response.write(template.render(template_values))
        else:
            template = JINJA_ENVIRONMENT.get_template("/Templates/index_logout.html")
            self.response.write(template.render())
