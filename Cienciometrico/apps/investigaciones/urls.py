from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.investigaciones.models import investigacion
from apps.investigaciones.views import InvestigacionList,Investigacioncrear,InvestigacionEdit,InvestigacionDelete


urlpatterns = [
    url(r'^uploads/form/$', Investigacioncrear, name='investigaciones_crear'),
    url(r'^listar', InvestigacionList.as_view(queryset= investigacion.objects.all().order_by('id')), name='investigaciones_lis'),
    url(r'^editar/(?P<id_investigacion>\d+)/$',InvestigacionEdit, name='investigaciones_update'),
    url(r'^eliminar/(?P<pk>\d+)/$',InvestigacionDelete, name='investigaciones_eliminar'),
]
