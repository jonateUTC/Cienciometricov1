from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.campus.models import campus
from apps.campus.views import CampusCreate, CampusList,Campus_edit, CampusDelete
urlpatterns = [
    url(r'^nuevo',CampusCreate, name='campus_crear'),
    url(r'^listar',CampusList.as_view(queryset= campus.objects.all().order_by('id')), name='campus_listar'),
    url(r'^update/(?P<id_campus>\d+)/$',Campus_edit, name='campus_update'),
    url(r'^delete/(?P<pk>\d+)/$',CampusDelete.as_view(), name='campus_delete'),
]