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
    vocal="Vocal"
    consiliario="Consiliario"
    cargosop=(('Consiliario', consiliario),(presidenta, 'Presidenta'),(vicepresidenta, 'Vicepresidenta'),(presidentahonoraria, 'Presidenta Honoraria'),(secretaria, 'Secretaria'),(vicesecretaria, 'Vicesecretaria'),(tesorera, 'Tesorera'),(vicetesorera, 'Vicetesorera'),(vocal, 'Vocal'))
    cargos=models.CharField(max_length=20, choices=cargosop)
    def __unicode__ (self):
        return str(self.cargos)


class Junta (models.Model):
    miembro=models.ManyToManyField(Miembros)


class HistoriaAs (models.Model):

    imagen1=models.ImageField(blank=True)
    imagen2=models.ImageField(blank=True)
    imagen3=models.ImageField(blank=True)
    historia=models.TextField(blank=True, max_length=1500)
    historia2=models.TextField(blank=True, max_length=1500)
    historia3=models.TextField(blank=True, max_length=1500)
    def __unicode__(self):
        return (self.historia)


class HistoriaVirgen (models.Model):
    desarrollo=models.TextField(blank=True, max_length=2500)
    desarrollo2=models.TextField(blank=True, max_length=2500)
    desarrollo3=models.TextField(blank=True, max_length=2500)
    desarrollo4=models.TextField(blank=True, max_length=2500)
    imagen1=models.ImageField(blank=True)
    imagen2=models.ImageField(blank=True)
    imagen3=models.ImageField(blank=True)
    def __unicode__ (self):
        return (self.desarrollo)

class Noticia (models.Model):
    titulo=models.CharField(max_length=200)
    intro=models.CharField(max_length=200)
    portada=models.ImageField(blank=True)
    imagen1=models.ImageField(blank=True)
    imagen2=models.ImageField(blank=True)
    cuerpo=models.TextField(blank=True, max_length=1500)
    cuerpo2=models.TextField(blank=True, max_length=1500)
    cuerpo3=models.TextField(blank=True, max_length=1500)
    fecha=models.DateTimeField(default=datetime.now)
    autor=models.ForeignKey(User)

    def __unicode__ (self):
        return (self.titulo)


class Sede(models.Model):
    imagen=models.ImageField(blank=True)
    imagen2=models.ImageField(blank=True)
    imagen3=models.ImageField(blank=True)
    lugar=models.CharField(max_length=100)
    historia=models.TextField(blank=True, max_length=2000)
    historia2=models.TextField(blank=True, max_length=2000)
    historia3=models.TextField(blank=True, max_length=2000)

    def __unicode__ (self):
        return (self.lugar)

class Cultos (models.Model):

    novena="Novena"
    serenata="Serenata"
    verbena="Verbena"
    presentacion="Presentacion"
    cultos=((novena,'Novena'),(serenata,'Serenata'),(verbena, 'Verbena'),(presentacion, 'Presentacion a la Virgen'))
    culto=models.CharField(max_length=50, choices=cultos)
    imagen=models.ImageField(blank=True)
    imagen2=models.ImageField(blank=True)
    fecha=models.CharField(max_length=100)
    desarrollo=models.TextField(blank=True, max_length=2000)
    desarrollo2=models.TextField(blank=True, max_length=2000)
    desarrollo3=models.TextField(blank=True, max_length=2000)

    def __unicode__ (self):
        return (self.culto)

class Tesoreria (models.Model):
    texto=models.TextField(blank=True, max_length=1000)

    def __unicode__ (self):
        return (self.texto)

class Album(models.Model):

    titulo=models.CharField(max_length=60)
    owner = models.CharField(blank=True, max_length=60)
    portada=models.ImageField(blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return (self.titulo)

class AlbumEspecifico(models.Model):

    titulo=models.CharField(max_length=60)
    owner = models.CharField(max_length=60)
    portada=models.ImageField(blank=True)
    album=models.ForeignKey(Album)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return (self.titulo)

class AlbumImagen(models.Model):
    titulo=models.CharField(max_length=60)
    album = models.ForeignKey(AlbumEspecifico, related_name='image')
    imagen = models.ImageField(blank=True)
    pie=models.CharField(blank=True, max_length=60)

    def __unicode__(self):
        return (self.titulo)
