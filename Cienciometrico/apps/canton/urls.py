from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.canton.models import canton
from apps.canton.views import CantonCreate,CantonList,CantonDelete,CantonUpdate
urlpatterns = [
    url(r'^nuevo',CantonCreate.as_view(), name='canton_crear'),
    url(r'^listar',CantonList.as_view(queryset= canton.objects.all().order_by('id')), name='canton_listar'),
    url(r'^editar/(?P<pk>\d+)/$',CantonUpdate.as_view(), name='canton_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',CantonDelete.as_view(), name='canton_eliminar'),
]