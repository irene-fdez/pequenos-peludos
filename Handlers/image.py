from google.appengine.ext import ndb
import webapp2


class ImageHandler(webapp2.RequestHandler):
    def get(self):
        try:
            id = self.request.GET['id']
        except:
            id = None

        if id is None:
            self.redirect("/error?msg=No se encontro el perro")
            return
        try:
            perro = ndb.Key(urlsafe=id).get()
        except:
            self.redirect("/error?msg=La clave no existe")
            return

        if perro.foto:
            self.response.headers['Content-Type'] = "image/png, image/jpg, image/jpeg"
            self.response.out.write(perro.foto)
