from django.conf.urls import url
from apps.Articulos_Cientificos.models import articulos_cientificos
from apps.Articulos_Cientificos.views import articulocreate,articuloUpdate,articuloList,articuloDelete
urlpatterns = [

    url(r'^CrearArticulo$',articulocreate.as_view(), name="articulos"),
    url(r'^ListarArticulos',articuloList.as_view(queryset=articulos_cientificos.objects.all().order_by('id')), name="ListaArticulo"),
    url(r'^UpdateArticulos/(?P<pk>\d+)/$',articuloUpdate.as_view(), name="update_articulo"),
    url(r'^DeleteArticulos/(?P<pk>\d+)/$',articuloDelete.as_view(), name="delete_articulo"),

]