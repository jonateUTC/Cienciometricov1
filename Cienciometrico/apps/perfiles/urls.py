from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.perfiles.models import User
from apps.perfiles.views import RegistroUsuario,ActualizarUsuario
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^registrar$', RegistroUsuario.as_view(), name="registrar"),
    url(r'^editar/(?P<pk>\d+)/$', ActualizarUsuario.as_view(), name="editar"),
]
