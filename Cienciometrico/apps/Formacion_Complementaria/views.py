# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from apps.Formacion_Complementaria.models import formacion_complementaria
from apps.Formacion_Complementaria.form import FormacionComform
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView

# Create your views here.

class CreateFormacion_Complementaria (CreateView):
    model = formacion_complementaria
    form_class = FormacionComform
    template_name = 'FormacionComplementaria/CreateFormacionComplementaria.html'
    success_url = reverse_lazy('FormacionComplementaria:lista_Formacion_Complementaria')

class ListFormacion_Complementaria(ListView):
    model = formacion_complementaria
    template_name = 'FormacionComplementaria/ListFormacionComplementaria.html'

class UpdateFormacion_Complementaria (UpdateView):
    model = formacion_complementaria
    form_class = FormacionComform
    template_name = 'FormacionComplementaria/UpdateFormacionComplementaria.html'
    success_url = reverse_lazy ('FormacionComplementaria:lista_Formacion_Complementaria')

class DeleteFormacion_Complementaria (DeleteView):
    model = formacion_complementaria
    template_name = 'FormacionComplementaria/DeleteFormacionComplementaria.html'
    success_url = reverse_lazy('FormacionComplementaria:lista_Formacion_Complementaria')