from django.conf.urls import url
from apps.Investigador.views import ActualizarInves,RegistroUsuario,ListUsuario,UpdateInvestigador
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^actualizarInvestigador$',login_required(ActualizarInves), name="actualizar"),
    url(r'^registrar', login_required(RegistroUsuario.as_view()), name="registrar"),
    url(r'^listar', login_required(ListUsuario.as_view()), name="listar"),
    url(r'^actualizar/(?P<pk>\d+)/$',login_required(UpdateInvestigador.as_view()), name="update"),

]