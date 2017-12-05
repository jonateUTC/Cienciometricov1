from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.zona.models import zona
from apps.zona.views import ZonaCreate,ZonaList,ZonaDelete,ZonaUpdate
urlpatterns = [
    url(r'^nuevo',ZonaCreate.as_view(), name='zona_crear'),
    url(r'^listar',ZonaList.as_view(queryset= zona.objects.all().order_by('id')), name='zona_listar'),
    url(r'^editar/(?P<pk>\d+)/$',ZonaUpdate.as_view(), name='zona_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',ZonaDelete.as_view(), name='zona_eliminar'),
]