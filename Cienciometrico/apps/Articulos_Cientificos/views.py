# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from apps.Articulos_Cientificos.models import articulos_cientificos
from apps.Articulos_Cientificos.form import articuloform
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from apps.roles.models import Rol
from apps.perfiles.models import Perfil
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
    def get_context_data(self, **kwargs):
        context = super(articulocreate, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Perfil.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio = []
        for r in roles:
            privi.append(r.id)
        for p in privi:
            roles5 = Rol.objects.get(pk=p)
            priv = roles5.privilegios.all()
            for pr in priv:
                privilegios.append(pr.codename)
        for i in privilegios:
            if i not in privilegio:
                privilegio.append(i)
        context['usuario'] = privilegio
        return context

class articuloList(ListView):
    model = articulos_cientificos
    template_name = 'ArticuloCientifico/ListarArticulos.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(articuloList, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Perfil.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio = []
        for r in roles:
            privi.append(r.id)
        for p in privi:
            roles5 = Rol.objects.get(pk=p)
            priv = roles5.privilegios.all()
            for pr in priv:
                privilegios.append(pr.codename)
        for i in privilegios:
            if i not in privilegio:
                privilegio.append(i)
        context['usuario'] = privilegio
        return context

class articuloUpdate (UpdateView):
    model = articulos_cientificos
    form_class = articuloform
    template_name = 'ArticuloCientifico/UpdateArticulo.html'
    success_url = reverse_lazy ('articulosCientificos:ListaArticulo')
    def get_context_data(self, **kwargs):
        context = super(articuloUpdate, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Perfil.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio = []
        for r in roles:
            privi.append(r.id)
        for p in privi:
            roles5 = Rol.objects.get(pk=p)
            priv = roles5.privilegios.all()
            for pr in priv:
                privilegios.append(pr.codename)
        for i in privilegios:
            if i not in privilegio:
                privilegio.append(i)
        context['usuario'] = privilegio
        return context

class articuloDelete (DeleteView):
    model = articulos_cientificos
    template_name = 'ArticuloCientifico/DeleteArticulo.html'
    success_url = reverse_lazy('articulosCientificos:ListaArticulo')
    def get_context_data(self, **kwargs):
        context = super(articuloDelete, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Perfil.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        privilegio = []
        for r in roles:
            privi.append(r.id)
        for p in privi:
            roles5 = Rol.objects.get(pk=p)
            priv = roles5.privilegios.all()
            for pr in priv:
                privilegios.append(pr.codename)
        for i in privilegios:
            if i not in privilegio:
                privilegio.append(i)
        context['usuario'] = privilegio
        return context