from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from apps.Revista.form import DocumentForm
from apps.Revista.models import revista
from django.views.generic import ListView,DeleteView
# Create your views here.
def Revistacrear(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Revista:lista_Revista')
    else:
        form = DocumentForm()
    return render(request, 'revista/CreateRevista.html', {
        'form': form
    })

class RevistaList(ListView):
    model = revista
    template_name = 'revista/ListRevista.html'
    paginate_by = 6
    

def RevistaEdit(request, id_revista):
    proy = revista.objects.get(id=id_revista)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES,instance=proy)
        if form.is_valid():
            form.save()
            return redirect('Revista:lista_Revista')
    else:
        form = DocumentForm(instance=proy)
    return render(request, 'revista/UpdateRevista.html', {'form': form})

class RevistaDelete(DeleteView):
    model = revista
    template_name = 'revista/DeleteRevista.html'
    success_url = reverse_lazy('Revista:lista_Revista')