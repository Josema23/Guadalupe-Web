from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from GuadalupeApp import views
from GuadalupeApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='principal.html'), name='base'),
    url(r'^JuntaDirectiva/', listarMiembros.as_view(), name='Listar miembros'),
    url(r'^nuevoMiembro/', crearMiembro.as_view(), name='Anyadir miembro'),
    url(r'^Cultos/', listarCultos.as_view(), name='Listar cultos'),
    url(r'^nuevoCulto/', crearCulto.as_view(), name='Anyadir culto'),
    url(r'^HistoriaVirgen/', verHistoriaVirgen.as_view(), name='Ver Historia Virgen'),
    url(r'^HistoriaAsociacion/', verHistoriaAsociacion.as_view(), name='Ver Historia Asociacion'),
    url(r'^Sede/', verSede.as_view(), name='Ver Sede Asociacion'),
    url(r'^Tesoreria/', verTesoreria.as_view(), name='Ver Tesoreria Asociacion'),
    url(r'^Noticias/', views.listarNoticias, name='Listar Noticias'),
    url(r'^Noticia/(?P<noticia_id>\d+)$', views.verNoticia, name='Ver Noticia'),
    url(r'^culto/(?P<culto_id>\d+)$', views.verCulto, name='Ver Culto'),
    url(r'^Galeria/', views.Galeria, name='Galeria'),
    url(r'^albums/(?P<alb_id>\d+)', views.AlbumGeneral, name='listar albums'),
    url(r'^album/(?P<album_id>\d+)', views.verAlbum, name='Ver album'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
