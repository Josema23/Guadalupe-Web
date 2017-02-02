from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Miembros (models.Model):
    nombre=models.CharField(max_length=50)
    presidenta="Presidenta"
    presidentahonoraria="Presidenta Honoraria"
    vicepresidenta="Vicepresidenta"
    secretaria="Secretaria"
    vicesecretaria="Vicesecretaria"
    tesorera="Tesorera"
    vicetesorera="Vicetesorera"
    vocal1="Vocal"
    vocal2="Vocal"
    cargosop=((presidenta, 'Presidenta'),(vicepresidenta, 'Vicepresidenta'),(presidentahonoraria, 'Presidenta Honoraria'),(secretaria, 'Secretaria'),(vicesecretaria, 'Vicesecretaria'),(tesorera, 'Tesorera'),(vicetesorera, 'Vicetesorera'),(vocal1, 'Vocal'),(vocal2, 'Vocal'))
    cargos=models.CharField(max_length=20, choices=cargosop)
    def __unicode__ (self):
        return (self.presidenta)


class Junta (models.Model):
    miembro=models.ManyToManyField(Miembros)

class HistoriaAs (models.Model):
    historia=models.TextField(max_length=1000)
    def __unicode__(self):
        return (self.historia)

class HistoriaVirgen (models.Model):
    desarrollo=models.TextField(max_length=1000)
    imagen1=models.ImageField()
    imagen2=models.ImageField()
    imagen3=models.ImageField()
    def __unicode__ (self):
        return (self.desarrollo)

class Noticia (models.Model):
    titulo=models.CharField(max_length=100)
    intro=models.CharField(max_length=100)
    portada=models.ImageField()
    imagen1=models.ImageField()
    imagen2=models.ImageField()
    cuerpo=models.TextField(max_length=1500)
    cuerpo2=models.TextField(max_length=1500)
    cuerpo3=models.TextField(max_length=1500)
    fecha=models.DateTimeField(default=datetime.now)
    autor=models.ForeignKey(User)

    def __unicode__ (self):
        return (self.titulo)


class Sede(models.Model):
    imagen=models.ImageField()
    lugar=models.CharField(max_length=50)
    historia=models.TextField(max_length=100)

    def __unicode__ (self):
        return (self.lugar)

class Cultos (models.Model):

    novena="Novena"
    serenata="Serenata"
    verbena="Verbena"
    presentacion="Presentacion"
    cultos=((novena,'Novena'),(serenata,'Serenata'),(verbena, 'Verbena'),(presentacion, 'Presentacion a la Virgen'))
    culto=models.CharField(max_length=50, choices=cultos)
    imagen=models.ImageField()
    imagen2=models.ImageField()
    fecha=models.CharField(max_length=50)
    desarrollo=models.TextField(max_length=500)

    def __unicode__ (self):
        return (self.culto)

class Tesoreria (models.Model):
    texto=models.TextField(max_length=500)

    def __unicode__ (self):
        return (self.texto)

class Album(models.Model):

    novena="Novena"
    serenata="Serenata"
    verbena="Verbena"
    presentacion="Presentacion"
    encuentros="Encuentros"
    viajes="Viajes"
    cultos=((viajes, 'Viajes'),(encuentros,'Encuentros'),(novena,'Novena'),(serenata,'Serenata'),(verbena, 'Verbena'),(presentacion, 'Presentacion a la Virgen'))
    titulo=models.CharField(max_length=50, choices=cultos)
    owner = models.CharField(max_length=60)
    portada=models.ImageField()
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return (self.titulo)

class AlbumImagen(models.Model):
    album = models.ForeignKey(Album, related_name='image')
    imagen = models.ImageField()

    def __unicode__(self):
        return str(self.imagen)
