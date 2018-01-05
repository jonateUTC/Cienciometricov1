from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.Revista.models import revista
from apps.Revista.views import Revistacrear,RevistaList,RevistaDelete,RevistaEdit
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^uploads/form/$', login_required(Revistacrear), name='create_Revista'),
    url(r'^listar', login_required(RevistaList.as_view(queryset= revista.objects.all().order_by('id'))), name='lista_Revista'),
    url(r'^editar/(?P<id_revista>\d+)/$', login_required(RevistaEdit), name='update_Revista'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(RevistaDelete.as_view()), name='delete_Revista'),
    
]