from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from GuadalupeApp.models import *

class crearMiembroForm(forms.ModelForm):

    class Meta:

        model=Miembros
        fields="__all__"

class crearCultoForm(forms.ModelForm):

    class Meta:

        model=Cultos
        fields="__all__"


class UploadImageForm(forms.ModelForm):

    class Meta:
        model = AlbumImagen
        fields = ['album', 'imagen']
