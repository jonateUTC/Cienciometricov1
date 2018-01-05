from django.shortcuts import render
from django.views.generic import CreateView
from apps.roles.models import Rol
from apps.roles.form import Registrorol
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class RegistroRol(CreateView):
    model = Rol
    template_name = "roles/rol_crear.html"
    form_class = Registrorol
    success_url = reverse_lazy('roles:crear_rol')
