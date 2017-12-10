from django.conf.urls import url
from apps.otrasinvestigaciones.models import otrasinvestigaciones
from apps.otrasinvestigaciones.views import Otrainvestigacioncrear,OtrainvestigacionDelete,OtrainvestigacionEdit,OtrainvestigacionList


urlpatterns = [
    url(r'^uploads/form/$', Otrainvestigacioncrear, name='otrasinvestigaciones_crear'),
    url(r'^listar', OtrainvestigacionList.as_view(queryset= otrasinvestigaciones.objects.all().order_by('id')), name='otrasinvestigaciones_lis'),
    url(r'^editar/(?P<id_otrainvestigacion>\d+)/$',OtrainvestigacionEdit, name='otrasinvestigaciones_update'),
    url(r'^eliminar/(?P<pk>\d+)/$',OtrainvestigacionDelete.as_view(), name='otrasinvestigaciones_eliminar'),
]
