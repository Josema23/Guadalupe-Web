from django.shortcuts import render, redirect, get_object_or_404
from GuadalupeApp.models import *
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UploadImageForm
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


class crearMiembro(CreateView):

    model= Miembros
    fields="__all__"
    template_name='crearMiembro.html'
    success_url="/JuntaDirectiva/"


class listarMiembros(ListView):
    model=Miembros
    template_name='listarMiembros.html'


class crearCulto(CreateView):

    model= Cultos
    fields="__all__"
    template_name='crearCulto.html'
    success_url="/"

class listarCultos(ListView):
    model=Cultos
    template_name='listarCultos.html'


def verCulto(request, culto_id):
	culto = Cultos.objects.get(pk = culto_id)
	contexto = {'culto':culto}
	return render(request,'verCulto.html',contexto)


class verHistoriaVirgen (ListView):

    model= HistoriaVirgen
    template_name='historiaVirgen.html'


class verHistoriaAsociacion (ListView):

    model= HistoriaAs
    template_name='historiaAsociacion.html'


class verSede (ListView):

    model= Sede
    template_name='sede.html'


class verTesoreria (ListView):

    model= Tesoreria
    template_name='tesoreria.html'


def listarNoticias(request):
    noticias = Noticia.objects.all().order_by('-fecha')

    paginador = Paginator(noticias,3)
    pagina = request.GET.get('page')
    try:
        noticias = paginador.page(pagina)
    except PageNotAnInteger:
        noticias = paginador.page(1)
    except EmptyPage:
        noticias = paginador.page(paginador.num_pages)

    contexto = {'noticias':noticias}
    return render(request,'listarNoticias.html',contexto)


def verNoticia(request, noticia_id):
	noticia = Noticia.objects.get(pk = noticia_id)
	contexto = {'noticia':noticia}
	return render(request,'verNoticia.html',contexto)


def Galeria(request):
    galeria=Album.objects.all()
    contexto = {'galeria':galeria}
    return render(request,'Galeria.html',contexto)


def AlbumGeneral(request, alb_id):
    album = Album.objects.get(pk=alb_id)
    gal=AlbumEspecifico.objects.filter(album=alb_id)
    contexto = {'album':album, 'gal':gal}
    return render(request,'AlbumEspecifico.html',contexto)


def verAlbum(request, album_id):
    album = AlbumEspecifico.objects.get(pk = album_id)
    imagenes= AlbumImagen.objects.filter(album=album_id)
    contexto = {'album':album, 'imagenes':imagenes}
    return render(request,'Fotos.html',contexto)
