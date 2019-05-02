from google.appengine.ext import ndb
import webapp2
import time


class AdoptHandler(webapp2.RequestHandler):
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
        perro.adoptado = "Si"
        perro.put()

        time.sleep(1)
        self.redirect("/showcurrent?id={}".format(id))

