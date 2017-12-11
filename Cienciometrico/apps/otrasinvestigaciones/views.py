from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from apps.otrasinvestigaciones.models import otrasinvestigaciones
from django.views.generic import ListView,DeleteView
from apps.otrasinvestigaciones.form import DocumentForm
# Create your views here.
def Otrainvestigacioncrear(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('otrainvestigacion:otrasinvestigaciones_lis')
    else:
        form = DocumentForm()
    return render(request, 'otrasinvestigaciones/otrasinvestigaciones_crear.html', {
        'form': form
    })
class OtrainvestigacionList(ListView):
    model = otrasinvestigaciones
    template_name = 'otrasinvestigaciones/otrasinvestigaciones_listar.html'
    paginate_by = 6
def OtrainvestigacionEdit(request, id_otrainvestigacion):
    oinves = otrasinvestigaciones.objects.get(id=id_otrainvestigacion)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES,instance=oinves)
        if form.is_valid():
            form.save()
            return redirect('otrainvestigacion:otrasinvestigaciones_lis')
    else:
        form = DocumentForm(instance=oinves)
    return render(request, 'otrasinvestigaciones/otrasinvestigaciones_update.html', {'form': form})
class OtrainvestigacionDelete(DeleteView):
    model = otrasinvestigaciones
    template_name = 'otrasinvestigaciones/otrasinvestigaciones_delete.html'
    success_url = reverse_lazy('otrainvestigacion:otrasinvestigaciones_lis')

