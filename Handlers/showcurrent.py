# -*- encoding: utf-8 -*-
from jinja import JINJA_ENVIRONMENT
from Lib.relativedelta import relativedelta
from google.appengine.api import users
from google.appengine.ext import ndb
from datetime import date
import webapp2


class ShowcurrentHandler(webapp2.RequestHandler):
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

            edad = format_edad(perro.nacimiento)
            tam = format_tam(perro.sexo, perro.tamanho)
            estado = format_estado(perro.adoptado)

            template_values = {
                'usuario': self.user.nickname(),
                'desconect': users.create_logout_url('/'),
                'es_admin': users.is_current_user_admin(),
                'perro': perro,
                'edad': edad,
                'tam': tam,
                'estado': estado
            }

            template = JINJA_ENVIRONMENT.get_template("/Templates/showcurrent.html")
            self.response.write(template.render(template_values))
        else:
            template = JINJA_ENVIRONMENT.get_template("/Templates/index_logout.html")
            self.response.write(template.render())


def format_edad(nac):
    toret = ""
    hoy = date.today()
    dif = relativedelta(hoy, nac)

    if dif.years > 0:
        if dif.years == 1:
            toret += u"{} año ".format(dif.years)
        else:
            toret += u"{} años ".format(dif.years)

    if dif.months > 0:
        if dif.months == 1:
            toret += u"{} mes ".format(dif.months)
        else:
            toret += u"{} meses ".format(dif.months)

    if dif.days > 0:
        if dif.days == 1:
            toret += u"{} dia".format(dif.days)
        else:
            toret += u"{} dias".format(dif.days)

    if dif.years == 0 and dif.months == 0 and dif.days == 0:
        toret = u"Nació hoy"

    return toret


def format_tam(sexo, tam):
    if tam =="Grande":
        tam = "Grande"

    elif tam =="Gigante":
        tam = "Gigante"

    else:
        if sexo =="Hembra" and tam == "Pequena":
            tam = u"Pequeña"
        elif sexo == "Hembra" and tam == "Mediana":
            tam = "Mediana"
        elif sexo =="Macho" and tam =="Pequena":
            tam = u"Pequeño"
        elif sexo == "Macho" and tam == "Mediana":
            tam = "Mediano"
        else:
            tam ="-"

    return tam


def format_estado(adopt):
    if adopt != "Si":
        return u"En adopción"
    else:
        return "Adoptado"
