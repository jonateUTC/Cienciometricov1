from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from apps.Proyectos.form import DocumentForm
from apps.Proyectos.models import proyecto
from django.views.generic import ListView,DeleteView
# Create your views here.
def Proyectocrear(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('proyecto:proyectos_lis')
    else:
        form = DocumentForm()
    return render(request, 'proyecto/proyectos_crear.html', {
        'form': form
    })
class ProyectoList(ListView):
    model = proyecto
    template_name = 'proyecto/proyectos_listar.html'
    paginate_by = 6

def ProyectoEdit(request, id_proyecto):
    proy = proyecto.objects.get(id=id_proyecto)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES,instance=proy)
        if form.is_valid():
            form.save()
            return redirect('proyecto:proyectos_lis')
    else:
        form = DocumentForm(instance=proy)
    return render(request, 'proyecto/proyectos_update.html', {'form': form})

class ProyectoDelete(DeleteView):
    model = proyecto
    template_name = 'proyecto/proyectos_delete.html'
    success_url = reverse_lazy('proyecto:proyectos_lis')

