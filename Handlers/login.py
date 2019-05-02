from jinja import JINJA_ENVIRONMENT
from google.appengine.api import users
import webapp2


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        self.user = users.get_current_user()

        if self.user:
            templates_values = {
                'usuario': self.user.nickname(),
                'desconect': users.create_logout_url('/'),
                'es_admin': users.is_current_user_admin(),
                'id_usuario': self.user.user_id()
            }
            template = JINJA_ENVIRONMENT.get_template("/Templates/index.html")
            self.response.write(template.render(templates_values))
        else:
            templates_values = {
                'login': users.create_login_url('/')
            }

            template = JINJA_ENVIRONMENT.get_template("/Templates/index_logout.html")
            self.response.write(template.render(templates_values))