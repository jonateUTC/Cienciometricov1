# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from apps.Publicaciones.models import publicaciones
from apps.Publicaciones.form import formPublicaciones
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView

# Create your views here.

def CreatePublicaciones(request):
    if request.method == 'POST':
        form = formPublicaciones(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('publicaciones:lista_Publicaciones')
    else:
        form = formPublicaciones()
    return render(request, 'Publicaciones/CreatePublicaciones.html', {
        'form': form
    })

class ListPublicaciones(ListView):
    model = publicaciones
    template_name = 'Publicaciones/ListPublicaciones.html'

def UpdatePublicaciones(request, id_publicaciones):
    proy = publicaciones.objects.get(id=id_publicaciones)
    if request.method == 'POST':
        form = formPublicaciones(request.POST, request.FILES,instance=proy)
        if form.is_valid():
            form.save()
            return redirect('publicaciones:lista_Publicaciones')
    else:
        form = formPublicaciones(instance=proy)
    return render(request, 'Publicaciones/UpdatePublicaciones.html', {'form': form})

class DeletePublicaciones (DeleteView):
    model = publicaciones
    template_name = 'Publicaciones/DeletePublicaciones.html'
    success_url = reverse_lazy('publicaciones:lista_Publicaciones')