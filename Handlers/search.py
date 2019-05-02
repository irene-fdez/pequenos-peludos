from Models.perro import Perro
from jinja import JINJA_ENVIRONMENT
from Lib.relativedelta import relativedelta
from google.appengine.api import users
import webapp2
import datetime


class SearchHandler(webapp2.RequestHandler):
    def post(self):
        self.user = users.get_current_user()
        if self.user:
            self.perros = Perro.query()

            self.perros_search = list()

            self.edad = self.request.get("edad").strip()
            self.tamanho = self.request.get("tamanho").strip().capitalize()
            self.sexo = self.request.get("sexo").strip().capitalize()

            self.buscar()

            template_values = {
                'usuario': self.user.nickname(),
                'desconect': users.create_logout_url('/'),
                'es_admin': users.is_current_user_admin(),
                'perros': self.perros_search,
                'numPerros': len(self.perros_search)
            }

            template = JINJA_ENVIRONMENT.get_template("/Templates/showall.html")
            self.response.write(template.render(template_values))
        else:
            template = JINJA_ENVIRONMENT.get_template("/Templates/index_logout.html")
            self.response.write(template.render())

    def buscar(self):

        if self.tamanho != "":
            self.perros = self.perros.filter(Perro.tamanho == self.tamanho)
        if self.sexo != "":
            self.perros = self.perros.filter(Perro.sexo == self.sexo)
        if self.edad != "":
            self.establece_edad()
        else:
            for perro in self.perros:
                if not self.perros_search.__contains__(perro):
                    self.perros_search.append(perro)

    def establece_edad(self):
        dhoy = datetime.date.today()

        date_c = dhoy + relativedelta(months=-6) #22/10/2018
        date_cA = dhoy + relativedelta(months=-18) #22/10/2017
        date_a = dhoy + relativedelta(years=-7) #22/10/2012

        if self.edad != "":
            if self.edad == "Cachorro":
                for perro in self.perros:
                    if perro.nacimiento >= date_c:
                        self.perros_search.append(perro)

            elif self.edad == "Cachorro_adolescente":
                for perro in self.perros:
                    if (perro.nacimiento < date_c) and (perro.nacimiento >= date_cA):
                        self.perros_search.append(perro)

            elif self.edad == "Adulto":
                for perro in self.perros:
                    if (perro.nacimiento < date_cA) and (perro.nacimiento >= date_a):
                        self.perros_search.append(perro)

            else:
                for perro in self.perros:
                    if perro.nacimiento < date_a:
                        self.perros_search.append(perro)
