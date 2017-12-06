# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from apps.facultad.models import facultad
from apps.facultad.form import FacultadForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from apps.pais.models import pais
from apps.zona.models import zona
from apps.universidad.models import universidad
from apps.campus.models import campus
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
def Facultadcrear(request):
    Pais = pais.objects.all()
    Zona= zona.objects.all()
    Universidad=universidad.objects.all()
    Campus=campus.objects.all()
    if request.method == 'POST':
        form= FacultadForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Facultad:lista_Facultad')
    else:
        form= FacultadForm()
    return render(request,'Facultad/CreateFacultad.html',{'form':form,'Pais': Pais,'Zona': Zona, 'Universidad':Universidad, 'Campus':Campus})
def Facultadedit(request, id_facultad):
    Pa = pais.objects.all()
    Zo = zona.objects.all()
    Uni = universidad.objects.all()
    Cam = campus.objects.all()
    fac = facultad.objects.get(id=id_facultad)

    if request.method == 'GET':
        form= FacultadForm(instance=fac)
    else:
        form = FacultadForm(request.POST, instance=fac)
        if form.is_valid():
            form.save()
        return redirect('Facultad:lista_Facultad')
    return render(request, 'Facultad/UpdateFacultad.html',{'form':form,'Pa': Pa,'Zo': Zo, 'Uni':Uni, 'Cam':Cam})