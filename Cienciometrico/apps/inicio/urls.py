from apps.inicio.views import inicio
from django.conf.urls import url

urlpatterns = [

    url(r'^inicio$',inicio, name="logeo"),
    ]