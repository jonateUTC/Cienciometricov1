# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from apps.Evento.models import evento
from apps.Evento.form import EventoForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView

# Create your views here.

class CreateEvento (CreateView):
    model = evento
    form_class = EventoForm
    template_name = 'Evento/CreateEvento.html'
    success_url = reverse_lazy('evento:lista_Evento')

class ListEvento(ListView):
    model = evento
    template_name = 'Evento/ListEvento.html'

class UpdateEvento (UpdateView):
    model = evento
    form_class = EventoForm
    template_name = 'Evento/UpdateEvento.html'
    success_url = reverse_lazy ('evento:lista_Evento')

class DeleteEvento (DeleteView):
    model = evento
    template_name = 'Evento/DeleteEvento.html'
    success_url = reverse_lazy('evento:lista_Evento')