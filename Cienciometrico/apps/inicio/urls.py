from apps.inicio.views import inicio
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
urlpatterns = [

    url(r'^inicio$',login_required(inicio), name="logeo"),
    ]