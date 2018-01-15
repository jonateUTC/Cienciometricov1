from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from apps.Revista.form import DocumentForm
from apps.Revista.models import revista
from django.views.generic import ListView,DeleteView
from apps.perfiles.models import Perfil
from apps.roles.models import Rol
# Create your views here.
def Revistacrear(request):
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
            return redirect('Revista:lista_Revista')
    else:
        form = DocumentForm()
    return render(request, 'revista/CreateRevista.html', {
        'form': form, 'usuario': privilegio
    })

class RevistaList(ListView):
    model = revista
    template_name = 'revista/ListRevista.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(RevistaList, self).get_context_data(**kwargs)
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
    

def RevistaEdit(request, id_revista):
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
    proy = revista.objects.get(id=id_revista)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES,instance=proy)
        if form.is_valid():
            form.save()
            return redirect('Revista:lista_Revista')
    else:
        form = DocumentForm(instance=proy)
    return render(request, 'revista/UpdateRevista.html', {'form': form, 'usuario': privilegio})

class RevistaDelete(DeleteView):
    model = revista
    template_name = 'revista/DeleteRevista.html'
    success_url = reverse_lazy('Revista:lista_Revista')
    def get_context_data(self, **kwargs):
        context = super(RevistaDelete, self).get_context_data(**kwargs)
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