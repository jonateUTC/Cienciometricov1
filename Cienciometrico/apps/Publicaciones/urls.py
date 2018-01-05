from django.conf.urls import url
from apps.Publicaciones.models import publicaciones
from apps.Publicaciones.views import CreatePublicaciones,ListPublicaciones,UpdatePublicaciones,DeletePublicaciones

urlpatterns = [

    url(r'^CrearPublicaciones$',CreatePublicaciones, name="create_Publicaciones"),
   url(r'^ListarPublicaciones',ListPublicaciones.as_view(queryset=publicaciones.objects.all().order_by('id')), name="lista_Publicaciones"),
   url(r'^UpdatePublicaciones/(?P<id_publicaciones>\d+)/$',UpdatePublicaciones, name="update_Publicaciones"),
   url(r'^DeletePublicaciones/(?P<pk>\d+)/$',DeletePublicaciones.as_view(), name="delete_Publicaciones"),

]