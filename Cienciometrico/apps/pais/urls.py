from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.pais.models import pais
from apps.pais.views import PaisCreate, PaisList, PaisUpdate, PaisDelete
urlpatterns = [
    url(r'^nuevo',PaisCreate.as_view(), name='pais_crear'),
    url(r'^listar',PaisList.as_view(queryset= pais.objects.all().order_by('id')), name='pais_listar'),
    url(r'^editar/(?P<pk>\d+)/$',PaisUpdate.as_view(), name='pais_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',PaisDelete.as_view(), name='pais_eliminar'),

]