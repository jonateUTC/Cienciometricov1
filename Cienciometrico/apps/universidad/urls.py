from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.universidad.models import universidad
from apps.universidad.views import UniversidadList,vista_ubicacion1,Universidad_edit,UniversidadDelete
from django.contrib.auth.decorators import login_required
urlpatterns = [

    url(r'^listar',login_required(UniversidadList.as_view(queryset= universidad.objects.all().order_by('id'))), name='universidad_listar'),
    url(r'^nuevo',login_required(vista_ubicacion1), name='universidad_crear'),
    url(r'^update/(?P<id_universidad>\d+)/$',login_required(Universidad_edit), name='universidad_update'),
    url(r'^delete/(?P<pk>\d+)/$',login_required(UniversidadDelete.as_view()), name='universidad_delete'),
]