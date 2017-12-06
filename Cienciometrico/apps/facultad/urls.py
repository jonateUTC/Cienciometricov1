from django.conf.urls import url
from apps.facultad.models import facultad
from apps.facultad.views import CreateFacultad,ListFacultad,UpdateFacultad,DeleteFacultad

urlpatterns = [

    url(r'^CrearFacultad$',CreateFacultad.as_view(), name="create_Facultad"),
   url(r'^ListarFacultad',ListFacultad.as_view(queryset=facultad.objects.all().order_by('id')), name="lista_Facultad"),
   url(r'^UpdateFacultad/(?P<pk>\d+)/$',UpdateFacultad.as_view(), name="update_Facultad"),
   url(r'^DeleteFacultad/(?P<pk>\d+)/$',DeleteFacultad.as_view(), name="delete_Facultad"),

]