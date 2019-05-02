from Models.perro import Perro
from jinja import JINJA_ENVIRONMENT
from google.appengine.api import users
import webapp2


class ShowallHandler(webapp2.RequestHandler):
    def get(self):
        self.user = users.get_current_user()
        self.razas = list()
        if self.user:
            self.perros = Perro.query()

            template_values = {
                'usuario': self.user.nickname(),
                'desconect': users.create_logout_url('/'),
                'es_admin': users.is_current_user_admin(),
                'perros': self.perros,
                'numPerros': self.perros.count()
            }

            template = JINJA_ENVIRONMENT.get_template("/Templates/showall.html")
            self.response.write(template.render(template_values))
        else:
            template = JINJA_ENVIRONMENT.get_template("/Templates/index_logout.html")
            self.response.write(template.render())
