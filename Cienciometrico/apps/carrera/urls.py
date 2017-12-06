from django.conf.urls import url
from apps.carrera.models import carrera
from apps.carrera.views import CreateCarrera,ListCarrera,UpdateCarrera,DeleteCarrera

urlpatterns = [

    url(r'^CrearCarrera$',CreateCarrera.as_view(), name="create_Carrera"),
   url(r'^ListarCarrera',ListCarrera.as_view(queryset=carrera.objects.all().order_by('id')), name="lista_Carrera"),
   url(r'^UpdateCarrera/(?P<pk>\d+)/$',UpdateCarrera.as_view(), name="update_Carrera"),
   url(r'^DeleteCarrera/(?P<pk>\d+)/$',DeleteCarrera.as_view(), name="delete_Carrera"),

]