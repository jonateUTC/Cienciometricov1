from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from apps.investigaciones.form import DocumentForm
from apps.investigaciones.models import investigacion
from django.views.generic import ListView,DeleteView
# Create your views here.
def Investigacioncrear(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('investigacion:investigaciones_lis')
    else:
        form = DocumentForm()
    return render(request, 'investigaciones/investigaciones_crear.html', {
        'form': form
    })
class InvestigacionList(ListView):
    model = investigacion
    template_name = 'investigaciones/investigaciones_listar.html'
    paginate_by = 6
def InvestigacionEdit(request, id_investigacion):
    inves = investigacion.objects.get(id=id_investigacion)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES,instance=inves)
        if form.is_valid():
            form.save()
            return redirect('investigacion:investigaciones_lis')
    else:
        form = DocumentForm(instance=inves)
    return render(request, 'investigaciones/investigaciones_update.html', {'form': form})
class InvestigacionDelete(DeleteView):
    model = investigacion
    template_name = 'investigaciones/investigaciones_delete.html'
    success_url = reverse_lazy('investigacion:investigaciones_lis')

