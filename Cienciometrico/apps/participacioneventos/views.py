from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from apps.participacioneventos.models import participacionevento
from django.views.generic import ListView,DeleteView
from apps.participacioneventos.form import DocuForm
# Create your views here.
def participacioneventoscrear(request):
    if request.method == 'POST':
        form = DocuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('partevento:partevento_lis')
    else:
        form = DocuForm()
    return render(request, 'participacioneventos/participacioneventos_crear.html', {
        'form': form
    })
class participacioneventosList(ListView):
    model = participacionevento
    template_name = 'participacioneventos/participacioneventos_listar.html'
    paginate_by = 6
def participacioneventosEdit(request, id_participacioneventos):
    pevento = participacionevento.objects.get(id=id_participacioneventos)
    if request.method == 'POST':
        form = DocuForm(request.POST, request.FILES,instance=pevento)
        if form.is_valid():
            form.save()
            return redirect('partevento:partevento_lis')
    else:
        form = DocuForm(instance=pevento)
    return render(request, 'participacioneventos/participacioneventos_update.html', {'form': form})
class participacioneventosDelete(DeleteView):
    model = participacionevento
    template_name = 'participacioneventos/participacioneventos_delete.html'
    success_url = reverse_lazy('partevento:partevento_lis')

