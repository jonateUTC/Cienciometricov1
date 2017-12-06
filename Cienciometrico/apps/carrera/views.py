# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from apps.carrera.models import carrera
from apps.carrera.form import CarreraForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView

# Create your views here.

class CreateCarrera (CreateView):
    model = carrera
    form_class = CarreraForm
    template_name = 'carrera/Createcarrera.html'
    success_url = reverse_lazy('carrera:lista_Carrera')

class ListCarrera(ListView):
    model = carrera
    template_name = 'carrera/Listcarrera.html'

class UpdateCarrera (UpdateView):
    model = carrera
    form_class = CarreraForm
    template_name = 'carrera/Updatecarrera.html'
    success_url = reverse_lazy ('carrera:lista_Carrera')

class DeleteCarrera (DeleteView):
    model = carrera
    template_name = 'carrera/Deletecarrera.html'
    success_url = reverse_lazy('carrera:lista_Carrera')