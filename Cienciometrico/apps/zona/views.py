from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.zona.form import ZonaForm
from apps.zona.models import zona
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apps.perfiles.models import Perfil
from apps.roles.models import Rol
# Create your views here.
class ZonaList(ListView):
    model = zona
    template_name='zona/zona_listar.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(ZonaList, self).get_context_data(**kwargs)
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

class ZonaCreate(CreateView):
    model = zona
    form_class = ZonaForm
    template_name = 'zona/zona_crear.html'
    success_url = reverse_lazy('zona:zona_listar')
class ZonaUpdate(UpdateView):
    model = zona
    form_class = ZonaForm
    template_name = 'zona/zona_update.html'
    success_url = reverse_lazy('zona:zona_listar')
class ZonaDelete(DeleteView):
    model = zona
    template_name = 'zona/zona_delete.html'
    success_url = reverse_lazy('zona:zona_listar')