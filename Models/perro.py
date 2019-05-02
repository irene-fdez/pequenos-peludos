#Perro

from google.appengine.ext import ndb


class Perro(ndb.Model):
    nombre = ndb.StringProperty(required=True)
    raza = ndb.StringProperty(required=True)
    nacimiento = ndb.DateProperty(required=True)
    tamanho = ndb.StringProperty(required=True)
    sexo = ndb.StringProperty(required=True)
    color = ndb.StringProperty(required=True)
    descripcion = ndb.TextProperty(required=True)
    adoptado = ndb.StringProperty()
    foto = ndb.BlobProperty(required=True)
