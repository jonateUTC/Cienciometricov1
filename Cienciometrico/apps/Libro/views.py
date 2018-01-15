from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from apps.Libro.form import DocumentForm
from apps.Libro.models import libro
from django.views.generic import ListView,DeleteView
from apps.roles.models import Rol
from apps.perfiles.models import Perfil

def Librocrear(request):
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
            return redirect('Libro:libro_lis')
    else:
        form = DocumentForm()
    return render(request,'libro/CreateLibro.html', {
        'form': form, 'usuario': privilegio
    })

class LibroList(ListView):
    model = libro
    template_name = 'libro/ListLibro.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(LibroList, self).get_context_data(**kwargs)
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

def LibroEdit(request, id_libro):
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
    proy = libro.objects.get(id=id_libro)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES,instance=proy)
        if form.is_valid():
            form.save()
            return redirect('Libro:libro_lis')
    else:
        form = DocumentForm(instance=proy)
    return render(request, 'libro/UpdateLibro.html', {'form': form, 'usuario': privilegio})

class LibroDelete(DeleteView):
    model = libro
    template_name = 'libro/DeleteLibro.html'
    success_url = reverse_lazy('Libro:libro_lis')
    def get_context_data(self, **kwargs):
        context = super(LibroDelete, self).get_context_data(**kwargs)
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
