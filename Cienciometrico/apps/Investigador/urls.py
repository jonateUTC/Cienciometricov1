from django.conf.urls import url
from apps.Investigador.views import ActualizarInves,RegistroUsuario,ListUsuario,UpdateInvestigador
from django.contrib.auth.models import User


urlpatterns = [

    url(r'^actualizarInvestigador$',ActualizarInves, name="actualizar"),
    url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
    url(r'^listar', ListUsuario.as_view(queryset=User.objects.all().order_by('id')), name="listar"),
    url(r'^actualizar/(?P<pk>\d+)/$',UpdateInvestigador.as_view(), name="update"),

]