from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.provincia.form import ProvinciaForm
from apps.provincia.models import provincia
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
# Create your views here.
class ProvinciaList(ListView):
    model = provincia
    template_name = 'provincia/provincia_listar.html'
    paginate_by = 6

class ProvinciaCreate(CreateView):
    model = provincia
    form_class = ProvinciaForm
    template_name = 'provincia/provincia_crear.html'
    success_url = reverse_lazy('provincia:provincia_listar')
class ProvinciaUpdate(UpdateView):
    model = provincia
    form_class = ProvinciaForm
    template_name = 'provincia/provincia_update.html'
    success_url = reverse_lazy('provincia:provincia_listar')
class ProvinciaDelete(DeleteView):
    model = provincia
    template_name = 'provincia/provincia_delete.html'
    success_url = reverse_lazy('provincia:provincia_listar')
