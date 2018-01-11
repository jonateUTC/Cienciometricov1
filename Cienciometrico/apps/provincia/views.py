from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.provincia.form import ProvinciaForm
from apps.provincia.models import provincia
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apps.perfiles.models import Perfil
from apps.roles.models import Rol
# Create your views here.
class ProvinciaList(ListView):
    model = provincia
    template_name = 'provincia/provincia_listar.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(ProvinciaList, self).get_context_data(**kwargs)
        usuario = self.request.user.id
        perfil = Perfil.objects.get(user_id=usuario)
        roles = perfil.roles.all()
        privi = []
        privilegios = []
        for r in roles:
            privi.append(r.id)
        for p in privi:
            roles5 = Rol.objects.get(pk=p)
            priv = roles5.privilegios.all()
            for pr in priv:
                privilegios.append(pr.codename)
        context['usuario'] = privilegios
        return context
class ProvinciaCreate(CreateView):
    model = provincia
    form_class = ProvinciaForm
    template_name = 'provincia/provincia_crear.html'
    success_url = reverse_lazy('provincia:provincia_listar')
class ProvinciaUpdate(UpdateView):
    model = provincia
    form_class = ProvinciaForm
    template_name = 'provincia/provincia_update.html'
    success_url = reverse_lazy('provincia:provincia_listar')
class ProvinciaDelete(DeleteView):
    model = provincia
    template_name = 'provincia/provincia_delete.html'
    success_url = reverse_lazy('provincia:provincia_listar')
