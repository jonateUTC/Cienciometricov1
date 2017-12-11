from django.conf.urls import url
from apps.Proyectos.models import proyecto
from apps.Proyectos.views import Proyectoscrear,ListProyectos,ProyectosEdit,DeleteProyectos

urlpatterns = [

    url(r'^CrearProyectos$',Proyectoscrear, name="create_Proyectos"),
   url(r'^ListarProyectos',ListProyectos.as_view(queryset=proyecto.objects.all().order_by('id')), name="lista_Proyectos"),
   url(r'^UpdateProyectos/(?P<id_Proyectos>\d+)/$',ProyectosEdit, name="update_Proyectos"),
   url(r'^DeleteProyectos/(?P<id_Proyectos>\d+)/$',DeleteProyectos.as_view(), name="delete_Proyectos"),

]