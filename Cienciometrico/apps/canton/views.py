from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from apps.canton.form import CantonForm
from apps.canton.models import canton
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apps.perfiles.models import Perfil
from apps.roles.models import Rol
# Create your views here.
class CantonList(ListView):
    model = canton
    template_name = 'canton/canton_listar.html'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super(CantonList, self).get_context_data(**kwargs)
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
class CantonCreate(CreateView):
    model = canton
    form_class = CantonForm
    template_name = 'canton/canton_crear.html'
    success_url = reverse_lazy('canton:canton_listar')
class CantonUpdate(UpdateView):
    model = canton
    form_class =CantonForm
    template_name = 'canton/canton_update.html'
    success_url = reverse_lazy('canton:canton_listar')
class CantonDelete(DeleteView):
    model = canton
    template_name = 'canton/canton_delete.html'
    success_url = reverse_lazy('canton:canton_listar')