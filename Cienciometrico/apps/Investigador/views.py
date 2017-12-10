from django.contrib import messages
from django.shortcuts import render,redirect
from apps.Investigador.form import formInvestigador,UserForm
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User


def ActualizarInves(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        investigador_form = formInvestigador(request.POST, instance=request.user.investigador)
        if user_form.is_valid() and investigador_form.is_valid():
            user_form.save()
            investigador_form.save()
            messages.success(request,('Los datos se han actualizado CORRECTAMENTE!'), extra_tags='alert')
            return redirect('investigador:actualizar')
        else:
            messages.error(request,('Hubo un error verifique los datos.'))
    else:
        user_form = UserForm(instance=request.user)
        investigador_form = formInvestigador(instance=request.user.investigador)
    return render(request, 'investigador/ActualizarDatos.html', {
        'user_form': user_form,
        'investigador_form': investigador_form
    })
class RegistroUsuario(CreateView):
    model = User
    template_name ='investigador/CreateInvestigador.html'
    form_class = UserForm
    success_url = reverse_lazy('investigador:listar')

class ListUsuario(ListView):
    model = User
    template_name = 'investigador/ListInvestigador.html'
    paginate_by = 6

class UpdateInvestigador (UpdateView):
    model = User
    form_class = UserForm
    template_name = 'investigador/UpdateInvestigador.html'
    success_url = reverse_lazy ('investigador:listar')
