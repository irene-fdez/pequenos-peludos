
from Models.perro import Perro
from Handlers.login import LoginHandler
from Handlers.add import RegisterHandler
from Handlers.showall import ShowallHandler
from Handlers.edit import EditHandler
from Handlers.showcurrent import ShowcurrentHandler
from Handlers.error import ErrorHandler
from Handlers.image import ImageHandler
from Handlers.delete import DeleteHandler
from Handlers.adopt import AdoptHandler
from Handlers.search import SearchHandler

from jinja import JINJA_ENVIRONMENT
from google.appengine.api import users
import webapp2


class MainHandler(webapp2.RequestHandler):
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


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ("/login", LoginHandler),
    ("/add", RegisterHandler),
    ("/showall", ShowallHandler),
    ("/edit", EditHandler),
    ("/showcurrent", ShowcurrentHandler),
    ("/error", ErrorHandler),
    ("/image", ImageHandler),
    ("/delete", DeleteHandler),
    ("/adopt", AdoptHandler),
    ("/search", SearchHandler)
], debug=True)
