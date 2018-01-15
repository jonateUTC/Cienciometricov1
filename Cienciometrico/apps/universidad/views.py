from django.shortcuts import render, HttpResponseRedirect, redirect
from django.core.urlresolvers import reverse_lazy
from apps.universidad.form import  UniversidadForm
from apps.universidad.models import universidad
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from .models import zona, pais
from apps.provincia.models import provincia
from apps.canton.models import canton
from apps.perfiles.models import Perfil
from apps.roles.models import Rol
# Create your views here.
class UniversidadList(ListView):
    model = universidad
    template_name = 'universidad/universidad_listar.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(UniversidadList, self).get_context_data(**kwargs)
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


def vista_ubicacion1(request):
    Pais = pais.objects.all()
    Zona= zona.objects.all()
    Provincia=provincia.objects.all()
    Canton=canton.objects.all()
    usuario = request.user.id
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
    if request.method == 'POST':
        form= UniversidadForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('universidad:universidad_listar')
    else:
        form= UniversidadForm()
    return render(request,'universidad/universidad_crear.html',{'form':form,'Pais': Pais,'Zona': Zona, 'Provincia':Provincia, 'Canton':Canton, 'usuario': privilegio})
def Universidad_edit(request, id_universidad):
    Pais = pais.objects.all()
    Zona = zona.objects.all()
    Provincia = provincia.objects.all()
    Canton = canton.objects.all()
    usuario = request.user.id
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
    univer = universidad.objects.get(id=id_universidad)
    if request.method == 'GET':
        form= UniversidadForm(instance=univer)
    else:
        form = UniversidadForm(request.POST, instance=univer)
        if form.is_valid():
            form.save()
        return redirect('universidad:universidad_listar')
    return render(request,'universidad/universidad_update.html',{'form':form,'Pais': Pais,'Zona': Zona, 'Provincia':Provincia, 'Canton':Canton, 'usuario': privilegio} )

class UniversidadDelete(DeleteView):
    model = universidad
    template_name = 'universidad/universidad_delete.html'
    success_url = reverse_lazy('universidad:universidad_listar')
    def get_context_data(self, **kwargs):
        context = super(UniversidadDelete, self).get_context_data(**kwargs)
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
