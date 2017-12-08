from django.shortcuts import render
from apps.datosprofesionales.models import datos_profecionales
from django.core.urlresolvers import reverse_lazy
from apps.datosprofesionales.form import DatosProfeForm
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
# Create your views here.
class DatosProfeList(ListView):
    model = datos_profecionales
    template_name = 'DatosProfesionales/profesionales_listar.html'
    paginate_by = 6

class DatosProfeCreate(CreateView):
    model = datos_profecionales
    form_class = DatosProfeForm
    template_name = 'DatosProfesionales/profesionales_crear.html'
    success_url = reverse_lazy('datosprofe:datosprofe_listar')
class DatosProfeUpdate(UpdateView):
    model = datos_profecionales
    form_class = DatosProfeForm
    template_name = 'DatosProfesionales/profesionales_update.html'
    success_url = reverse_lazy('datosprofe:datosprofe_listar')
class DatosProfeDelete(DeleteView):
    model = datos_profecionales
    template_name = 'DatosProfesionales/profesionales_delete.html'
    success_url = reverse_lazy('datosprofe:datosprofe_listar')
