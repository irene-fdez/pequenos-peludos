# -*- encoding: utf-8 -*-
from Models.perro import Perro
from jinja import JINJA_ENVIRONMENT
from google.appengine.ext import db
from google.appengine.api import users
import webapp2
import datetime
import time


class RegisterHandler(webapp2.RequestHandler):
    def get(self):
        self.user = users.get_current_user()
        self.admin = users.is_current_user_admin()

        if self.user:
            if self.admin:
                template_values = {
                    'usuario': self.user.nickname(),
                    'desconect': users.create_logout_url('/'),
                    'es_admin': self.admin,
                    'id_usuario': self.user.user_id(),
                    'fecha_hoy': datetime.date.today()
                }

                template = JINJA_ENVIRONMENT.get_template("/Templates/add.html")
                self.response.write(template.render(template_values))
            else:
                template_values = {
                    'usuario': self.user.nickname(),
                    'desconect': users.create_logout_url('/'),
                    'es_admin': self.admin,
                    'id_usuario': self.user.user_id(),
                    'fecha_hoy': datetime.date.today(),
                    'error_msg': u"No tiene permisos para acceder a esta página."
                }
                template = JINJA_ENVIRONMENT.get_template("/Templates/error.html")
                self.response.write(template.render(template_values))
        else:
            template = JINJA_ENVIRONMENT.get_template("/Templates/index_logout.html")
            self.response.write(template.render())

    def post(self):
        perro = Perro()

        perro.nombre = self.request.get("nombre").strip().capitalize()
        perro.raza = self.request.get("raza").strip()
        perro.tamanho = self.request.get("tamanho").strip().capitalize()
        perro.sexo = self.request.get("sexo").strip().capitalize()
        perro.color = self.request.get("color").strip().capitalize()
        perro.descripcion = self.request.get("descripcion").strip()
        perro.adoptado = "No"

        fecha = self.request.get("nacimiento").strip().split("-")
        perro.nacimiento = datetime.datetime(int(fecha[0]), int(fecha[1]), int(fecha[2]))

        foto = self.request.get("foto").strip()
        perro.foto = db.Blob(foto)

        perro.put()

        time.sleep(1)
        self.redirect("/")

