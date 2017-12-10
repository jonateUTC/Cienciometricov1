# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from apps.Articulos_Cientificos.models import articulos_cientificos
from apps.Articulos_Cientificos.form import articuloform
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
# Create your views here.

def articulo(request):
    return render(request,'ArticuloCientifico/ArticulosCientificos.html'  )
def listarArticulo(request):
    return render(request, 'ArticuloCientifico/ListarArticulos.html')

class articulocreate(CreateView):
    model = articulos_cientificos
    form_class = articuloform
    template_name = 'ArticuloCientifico/ArticulosCientificos.html'
    success_url = reverse_lazy ('articulosCientificos:ListaArticulo')

class articuloList(ListView):
    model = articulos_cientificos
    template_name = 'ArticuloCientifico/ListarArticulos.html'

class articuloUpdate (UpdateView):
    model = articulos_cientificos
    form_class = articuloform
    template_name = 'ArticuloCientifico/UpdateArticulo.html'
    success_url = reverse_lazy ('articulosCientificos:ListaArticulo')

class articuloDelete (DeleteView):
    model = articulos_cientificos
    template_name = 'ArticuloCientifico/DeleteArticulo.html'
    success_url = reverse_lazy('articulosCientificos:ListaArticulo')