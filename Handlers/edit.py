from jinja import JINJA_ENVIRONMENT
from google.appengine.ext import ndb, db
from google.appengine.api import users
import webapp2
import datetime
import time


class EditHandler(webapp2.RequestHandler):
    def get(self):
        self.user = users.get_current_user()
        if self.user:
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
                'usuario': self.user.nickname(),
                'desconect': users.create_logout_url('/'),
                'es_admin': users.is_current_user_admin(),
                'id_usuario': self.user.user_id(),
                'perro': perro
            }

            template = JINJA_ENVIRONMENT.get_template("/Templates/edit.html")
            self.response.write(template.render(template_values))
        else:
            template = JINJA_ENVIRONMENT.get_template("/Templates/index_logout.html")
            self.response.write(template.render())

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

        perro.nombre = self.request.get("nombre").strip().capitalize()
        perro.raza = self.request.get("raza").strip()
        perro.tamanho = self.request.get("tamanho").strip().capitalize()
        perro.sexo = self.request.get("sexo").strip().capitalize()
        perro.color = self.request.get("color").strip().capitalize()
        perro.descripcion = self.request.get("descripcion").strip()
        perro.adoptado = self.request.get("adoptado").strip().capitalize()

        fecha = self.request.get("nacimiento").strip().split("-")
        perro.nacimiento = datetime.datetime(int(fecha[0]), int(fecha[1]), int(fecha[2]))

        foto = self.request.get("nueva_foto").strip()
        if foto:
           perro.foto = db.Blob(foto)

        perro.put()

        time.sleep(1)
        self.redirect("/showcurrent?id={}".format(id))

