from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.zona.form import ZonaForm
from apps.zona.models import zona
from django.views.generic import ListView, CreateView,UpdateView,DeleteView

# Create your views here.
class ZonaList(ListView):
    model = zona
    template_name='zona/zona_listar.html'
    paginate_by = 6


class ZonaCreate(CreateView):
    model = zona
    form_class = ZonaForm
    template_name = 'zona/zona_crear.html'
    success_url = reverse_lazy('zona:zona_listar')
class ZonaUpdate(UpdateView):
    model = zona
    form_class = ZonaForm
    template_name = 'zona/zona_update.html'
    success_url = reverse_lazy('zona:zona_listar')
class ZonaDelete(DeleteView):
    model = zona
    template_name = 'zona/zona_delete.html'
    success_url = reverse_lazy('zona:zona_listar')