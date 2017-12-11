# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from apps.Formacion_Academica.models import formacion_academica
from apps.Formacion_Academica.form import FormacionAform
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView

# Create your views here.

class CreateFormacion_Academica (CreateView):
    model = formacion_academica
    form_class = FormacionAform
    template_name = 'FormacionAcademica/CreateFormacionAcademica.html'
    success_url = reverse_lazy('FormacionAcademica:lista_Formacion_Academica')

class ListFormacion_Academica(ListView):
    model = formacion_academica
    template_name = 'FormacionAcademica/ListFormacionAcademica.html'

class UpdateFormacion_Academica (UpdateView):
    model = formacion_academica
    form_class = FormacionAform
    template_name = 'FormacionAcademica/UpdateFormacionAcademica.html'
    success_url = reverse_lazy ('FormacionAcademica:lista_Formacion_Academica')

class DeleteFormacion_Academica (DeleteView):
    model = formacion_academica
    template_name = 'FormacionAcademica/DeleteFormacionAcademica.html'
    success_url = reverse_lazy('FormacionAcademica:lista_Formacion_Academica')