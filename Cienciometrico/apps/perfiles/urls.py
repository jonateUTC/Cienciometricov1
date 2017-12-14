from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.perfiles.models import User
from apps.perfiles.views import UserCreate,UserDelete,UserUpdate,UserList


urlpatterns = [
    url(r'^uploads/form/$', UserCreate.as_view(), name='User_crear'),
    url(r'^listar', UserList.as_view(queryset= User.objects.all().order_by('id')), name='User_lis'),
    url(r'^editar/(?P<pk>\d+)/$',UserUpdate.as_view(), name='User_update'),
    url(r'^eliminar/(?P<pk>\d+)/$',UserDelete.as_view(), name='User_eliminar'),
]
