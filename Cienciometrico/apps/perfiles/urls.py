from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.perfiles.models import User
from apps.perfiles.views import UserCreate,UserDelete,UserUpdate,UserList
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^uploads/form/$', login_required(UserCreate.as_view()), name='User_crear'),
    url(r'^listar', login_required(UserList.as_view(queryset= User.objects.all().order_by('id'))), name='User_lis'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(UserUpdate.as_view()), name='User_update'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(UserDelete.as_view()), name='User_eliminar'),
]
