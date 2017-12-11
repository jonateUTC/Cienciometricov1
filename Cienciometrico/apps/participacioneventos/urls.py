from django.conf.urls import url
from apps.participacioneventos.models import participacionevento
from apps.participacioneventos.views import participacioneventoscrear,participacioneventosDelete,participacioneventosEdit,participacioneventosList


urlpatterns = [
    url(r'^uploads/form/$', participacioneventoscrear, name='partevento_crear'),
    url(r'^listar', participacioneventosList.as_view(queryset= participacionevento.objects.all().order_by('id')), name='partevento_lis'),
    url(r'^editar/(?P<id_participacioneventos>\d+)/$',participacioneventosEdit, name='partevento_update'),
    url(r'^eliminar/(?P<pk>\d+)/$',participacioneventosDelete.as_view(), name='partevento_eliminar'),
]
