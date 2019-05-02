from jinja import JINJA_ENVIRONMENT
from google.appengine.ext import ndb
import webapp2
import time


class DeleteHandler(webapp2.RequestHandler):
    def get(self):
        try:
            id = self.request.GET['id']
        except:
            id = None

        if id is None:
            self.redirect("/error?msg=No se ha encontrado el perro")
            return
        try:
            perro = ndb.Key(urlsafe=id).get()
        except:
            self.redirect("/error?msg=La clave no existe")
            return

        template_values = {
            'perro': perro
        }

        template = JINJA_ENVIRONMENT.get_template("/Templates/delete.html")
        self.response.write(template.render(template_values))

    def post(self):
        try:
            id = self.request.GET['id']
        except:
            id = None

        if id is None:
            self.redirect("/error?msg=No se ha encontrado el perro")
            return
        try:
            perro = ndb.Key(urlsafe=id).get()
        except:
            self.redirect("/error?msg=La clave no existe")
            return

        perro.key.delete()

        time.sleep(1)
        self.redirect("/showall")
