from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from apps.Proyectos.models import proyecto
from django.views.generic import ListView,DeleteView
from apps.Proyectos.form import ProyectoForm
# Create your views here.
def Proyectoscrear(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('proyectos:lista_Proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'proyecto/CreateProyectos.html', {
        'form': form
    })
class ListProyectos(ListView):
    model = proyecto
    template_name = 'proyecto/ListProyectos.html'
    paginate_by = 6
def ProyectosEdit(request, id_Proyectos):
    pevento = proyecto.objects.get(id=id_Proyectos)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES,instance=pevento)
        if form.is_valid():
            form.save()
            return redirect('proyectos:lista_Proyectos')
    else:
        form = ProyectoForm(instance=pevento)
    return render(request, 'proyecto/UpdateProyectos.html', {'form': form})
class DeleteProyectos(DeleteView):
    model = proyecto
    template_name = 'proyecto/DeleteProyectos.html'
    success_url = reverse_lazy('proyectos:lista_Proyectos')

