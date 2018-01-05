from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from apps.Libro.form import DocumentForm
from apps.Libro.models import libro
from django.views.generic import ListView,DeleteView

def Librocrear(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Libro:libro_lis')
    else:
        form = DocumentForm()
    return render(request,'libro/CreateLibro.html', {
        'form': form
    })

class LibroList(ListView):
    model = libro
    template_name = 'libro/ListLibro.html'
    paginate_by = 6

def LibroEdit(request, id_libro):
    proy = libro.objects.get(id=id_libro)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES,instance=proy)
        if form.is_valid():
            form.save()
            return redirect('Libro:libro_lis')
    else:
        form = DocumentForm(instance=proy)
    return render(request, 'libro/UpdateLibro.html', {'form': form})

class LibroDelete(DeleteView):
    model = libro
    template_name = 'libro/DeleteLibro.html'
    success_url = reverse_lazy('Libro:libro_lis')
