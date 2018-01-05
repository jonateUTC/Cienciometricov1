from django.shortcuts import render, HttpResponseRedirect
from apps.perfiles.models import Perfil
from apps.roles.models import Rol
# Create your views here.

def inicio(request):
    usuario = request.user.id
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
    return render(request, 'base1/inicio.html', {'usuario': privilegios})
