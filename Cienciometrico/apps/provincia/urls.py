from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.provincia.models import provincia
from apps.provincia.views import ProvinciaCreate,ProvinciaList,ProvinciaDelete,ProvinciaUpdate
urlpatterns = [
    url(r'^nuevo',ProvinciaCreate.as_view(), name='provincia_crear'),
    url(r'^listar',ProvinciaList.as_view(queryset= provincia.objects.all().order_by('id')), name='provincia_listar'),
    url(r'^editar/(?P<pk>\d+)/$',ProvinciaUpdate.as_view(), name='provincia_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',ProvinciaDelete.as_view(), name='provincia_eliminar'),
]