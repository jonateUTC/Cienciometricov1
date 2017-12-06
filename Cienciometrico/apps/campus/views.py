from django.shortcuts import render
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from apps.campus.form import CampusForm
from apps.campus.models import campus
from apps.pais.models import pais
from apps.provincia.models import provincia
from apps.zona.models import zona
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
# Create your views here.
class CampusList(ListView):
    model = campus
    template_name = 'campus/campus_listar.html'
    paginate_by = 6

def CampusCreate(request):
    Pais = pais.objects.all()
    Zona = zona.objects.all()
    Provincia = provincia.objects.all()
    if request.method == 'POST':
        form= CampusForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('campus:campus_listar')
    else:
        form= CampusForm()
    return render(request,'campus/campus_crear.html',{'form':form,'Pais': Pais,'Zona': Zona, 'Provincia':Provincia})
def Campus_edit(request, id_campus):
    Pais = pais.objects.all()
    Zona = zona.objects.all()
    Provincia = provincia.objects.all()

    camp = campus.objects.get(id=id_campus)
    if request.method == 'GET':
        form= CampusForm(instance=camp)
    else:
        form = CampusForm(request.POST, instance=camp)
        if form.is_valid():
            form.save()
        return redirect('campus:campus_listar')
    return render(request,'campus/campus_update.html',{'form':form,'Pais': Pais,'Zona': Zona, 'Provincia':Provincia})
class CampusDelete(DeleteView):
    model = campus
    template_name = 'campus/campus_delete.html'
    success_url = reverse_lazy('campus:campus_listar')
