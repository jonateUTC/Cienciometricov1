from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.pais.form import PaisForm
from apps.pais.models import pais
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
# Create your views here.
class PaisList(ListView):
    model = pais
    template_name = 'pais/pais_listar.html'
    paginate_by = 6

class PaisCreate(CreateView):
    model = pais
    form_class = PaisForm
    template_name = 'pais/pais_crear.html'
    success_url = reverse_lazy('pais:pais_listar')
class PaisUpdate(UpdateView):
    model = pais
    form_class = PaisForm
    template_name = 'pais/pais_update.html'
    success_url = reverse_lazy('pais:pais_listar')
class PaisDelete(DeleteView):
    model = pais
    template_name = 'pais/pais_eliminar.html'
    success_url = reverse_lazy('pais:pais_listar')