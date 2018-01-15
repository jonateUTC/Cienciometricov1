from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from apps.Proyectos.form import DocumentForm
from apps.Proyectos.models import proyecto
from django.views.generic import ListView,DeleteView
from apps.perfiles.models import Perfil
from apps.roles.models import Rol
# Create your views here.
def Proyectocrear(request):
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
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('proyecto:proyectos_lis')
    else:
        form = DocumentForm()
    return render(request, 'proyecto/proyectos_crear.html', {
        'form': form, 'usuario': privilegio
    })
class ProyectoList(ListView):
    model = proyecto
    template_name = 'proyecto/proyectos_listar.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(ProyectoList, self).get_context_data(**kwargs)
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

def ProyectoEdit(request, id_proyecto):
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
    proy = proyecto.objects.get(id=id_proyecto)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES,instance=proy)
        if form.is_valid():
            form.save()
            return redirect('proyecto:proyectos_lis')
    else:
        form = DocumentForm(instance=proy)
    return render(request, 'proyecto/proyectos_update.html', {'form': form, 'usuario': privilegio})

class ProyectoDelete(DeleteView):
    model = proyecto
    template_name = 'proyecto/proyectos_delete.html'
    success_url = reverse_lazy('proyecto:proyectos_lis')
    def get_context_data(self, **kwargs):
        context = super(ProyectoDelete, self).get_context_data(**kwargs)
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

