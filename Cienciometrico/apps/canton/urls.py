from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.canton.models import canton
from apps.canton.views import CantonCreate,CantonList,CantonDelete,CantonUpdate
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^nuevo',login_required(CantonCreate.as_view()), name='canton_crear'),
    url(r'^listar',login_required(CantonList.as_view(queryset= canton.objects.all().order_by('id'))), name='canton_listar'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(CantonUpdate.as_view()), name='canton_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(CantonDelete.as_view()), name='canton_eliminar'),
]