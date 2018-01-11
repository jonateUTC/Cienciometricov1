from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.pais.form import PaisForm
from apps.pais.models import pais
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apps.perfiles.models import Perfil
from apps.roles.models import Rol
# Create your views here.
class PaisList(ListView):
    model = pais
    template_name = 'pais/pais_listar.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(PaisList, self).get_context_data(**kwargs)
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

class PaisCreate(CreateView):
    model = pais
    form_class = PaisForm
    template_name = 'pais/pais_crear.html'
    success_url = reverse_lazy('pais:pais_listar')
class PaisUpdate(UpdateView):
    model = pais
    form_class = PaisForm
    template_name = 'pais/pais_update.html'
    success_url = reverse_lazy('pais:pais_listar')
class PaisDelete(DeleteView):
    model = pais
    template_name = 'pais/pais_eliminar.html'
    success_url = reverse_lazy('pais:pais_listar')