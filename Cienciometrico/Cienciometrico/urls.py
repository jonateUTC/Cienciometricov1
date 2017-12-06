"""Cienciometrico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pais/', include('apps.pais.urls', namespace="pais")),
    url(r'^zona/', include('apps.zona.urls', namespace="zona")),
    url(r'^provincia/', include('apps.provincia.urls', namespace="provincia")),
    url(r'^canton/', include('apps.canton.urls', namespace="canton")),
    url(r'^universidad/', include('apps.universidad.urls', namespace="universidad")),
    url(r'^campus/', include('apps.campus.urls', namespace="campus")),
]
