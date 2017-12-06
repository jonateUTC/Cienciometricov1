from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.canton.form import CantonForm
from apps.canton.models import canton
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
# Create your views here.
class CantonList(ListView):
    model = canton
    template_name = 'canton/canton_listar.html'
    paginate_by = 6

class CantonCreate(CreateView):
    model = canton
    form_class = CantonForm
    template_name = 'canton/canton_crear.html'
    success_url = reverse_lazy('canton:canton_listar')
class CantonUpdate(UpdateView):
    model = canton
    form_class =CantonForm
    template_name = 'canton/canton_update.html'
    success_url = reverse_lazy('canton:canton_listar')
class CantonDelete(DeleteView):
    model = canton
    template_name = 'canton/canton_delete.html'
    success_url = reverse_lazy('canton:canton_listar')