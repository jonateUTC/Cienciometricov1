from django.conf.urls import url
from apps.Evento.models import evento
from apps.Evento.views import CreateEvento,ListEvento,UpdateEvento,DeleteEvento

urlpatterns = [

    url(r'^CrearEvento$',CreateEvento.as_view(), name="create_Evento"),
   url(r'^ListarEvento',ListEvento.as_view(queryset=evento.objects.all().order_by('id')), name="lista_Evento"),
   url(r'^UpdateEvento/(?P<pk>\d+)/$',UpdateEvento.as_view(), name="update_Evento"),
   url(r'^DeleteEvento/(?P<pk>\d+)/$',DeleteEvento.as_view(), name="delete_Evento"),

]