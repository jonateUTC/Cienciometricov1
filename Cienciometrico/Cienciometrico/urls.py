"""Cienciometrico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pais/', include('apps.pais.urls', namespace="pais")),
    url(r'^zona/', include('apps.zona.urls', namespace="zona")),
    url(r'^provincia/', include('apps.provincia.urls', namespace="provincia")),
    url(r'^canton/', include('apps.canton.urls', namespace="canton")),
    url(r'^universidad/', include('apps.universidad.urls', namespace="universidad")),
    url(r'^Carrera/', include('apps.carrera.urls', namespace="carrera")),
    url(r'^Facultad/', include('apps.facultad.urls', namespace="Facultad")),
    url(r'^campus/', include('apps.campus.urls', namespace="campus")),
    url(r'^investigador/', include('apps.Investigador.urls', namespace="investigador")),
    url(r'^articulo/', include('apps.Articulos_Cientificos.urls', namespace="articulosCientificos")),
    url(r'^investigacion/', include('apps.investigaciones.urls', namespace="investigacion")),
    url(r'^datosprofesionales/', include('apps.datosprofesionales.urls', namespace="datosprofe")),
    url(r'^formacionAcad/', include('apps.Formacion_Academica.urls', namespace="FormacionAcademica")),
    url(r'^formacionComple/', include('apps.Formacion_Complementaria.urls', namespace="FormacionComplementaria")),
    url(r'^Evento/', include('apps.Evento.urls', namespace="evento")),
    url(r'^otrainvestigacion/', include('apps.otrasinvestigaciones.urls', namespace="otrainvestigacion")),
    url(r'^participacioneventos/', include('apps.participacioneventos.urls', namespace="partevento")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
