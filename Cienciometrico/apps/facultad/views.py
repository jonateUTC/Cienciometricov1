# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from app.Facultad.models import facultad
from app.Facultad.form import FacultadForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView

# Create your views here.

class CreateFacultad (CreateView):
    model = facultad
    form_class = FacultadForm
    template_name = 'Facultad/CreateFacultad.html'
    success_url = reverse_lazy('Facultad:lista_Facultad')

class ListFacultad(ListView):
    model = facultad
    template_name = 'Facultad/ListFacultad.html'

class UpdateFacultad (UpdateView):
    model = facultad
    form_class = FacultadForm
    template_name = 'Facultad/UpdateFacultad.html'
    success_url = reverse_lazy ('Facultad:lista_Facultad')

class DeleteFacultad (DeleteView):
    model = facultad
    template_name = 'Facultad/DeleteFacultad.html'
    success_url = reverse_lazy('Facultad:lista_Facultad')