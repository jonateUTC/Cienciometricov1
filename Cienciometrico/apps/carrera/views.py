# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from apps.carrera.models import carrera
from apps.carrera.form import CarreraForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from apps.pais.models import pais
from apps.zona.models import zona
from apps.universidad.models import universidad
from apps.campus.models import campus
from apps.facultad.models import facultad
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
    
def Carreracrear(request):
    Pais = pais.objects.all()
    Zona= zona.objects.all()
    Universidad=universidad.objects.all()
    Campus=campus.objects.all()
    Facultad = facultad.objects.all()
    if request.method == 'POST':
        form= CarreraForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('carrera:lista_Carrera')
    else:
        form= CarreraForm()
    return render(request,'carrera/CreateCarrera.html',{'form':form,'Pais': Pais,'Zona': Zona, 'Universidad':Universidad, 'Campus':Campus,'Facultad':Facultad})
def Carreradedit(request, id_carrera):
    Pais = pais.objects.all()
    Zona = zona.objects.all()
    Universidad = universidad.objects.all()
    Campus = campus.objects.all()
    Facultad = facultad.objects.all()
    carr = carrera.objects.get(id=id_carrera)

    if request.method == 'GET':
        form= CarreraForm(instance=carr)
    else:
        form = CarreraForm(request.POST, instance=carr)
        if form.is_valid():
            form.save()
        return redirect('carrera:lista_Carrera')
    return render(request, 'carrera/UpdateCarrera.html',{'form':form,'Pais': Pais,'Zona': Zona, 'Universidad':Universidad, 'Campus':Campus,'Facultad':Facultad})