from django.shortcuts import render
from apps.perfiles.models import Perfil
from apps.roles.models import Rol
# Create your views here.
def inde(request):
    return render(request, 'base/inicio.html')
def producc(request):
    return render(request, 'base/produccioncientifica.html')
def similar(request):
    perfil = Perfil.objects.all()
    privi = []
    for p in perfil:
        if p.roles == '3':
            privi.append(p)

    return render(request, 'base/similares.html',{'usuario': perfil})