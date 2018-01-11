from django.shortcuts import render

# Create your views here.
def inde(request):
    return render(request, 'base/inicio.html')
def producc(request):
    return render(request, 'base/produccioncientifica.html')
def similar(request):
    return render(request, 'base/similares.html')