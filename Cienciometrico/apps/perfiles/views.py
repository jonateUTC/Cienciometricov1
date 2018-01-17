from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, HttpResponseRedirect
from apps.perfiles.models import Perfil
from apps.roles.models import Rol
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,UpdateView
from django.core.urlresolvers import reverse_lazy
from apps.perfiles.form import RegistroForm,UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
class RegistroUsuario(CreateView):
        model = Perfil
        template_name = "usuario/registrar.html"
        form_class = RegistroForm
        second_form_class = UserForm
        success_url = reverse_lazy('usuario:registrar')

        def get_context_data(self, **kwargs):
            persona = Perfil.objects.all()  # Esto si retorna un QuerySet
            exi = persona.exists()

            context= super(RegistroUsuario,self).get_context_data(**kwargs)
            usuario = self.request.user.id
            perfil = Perfil.objects.get(user_id=usuario)
            roles = perfil.roles.all()
            privi = []
            privilegios = []
            privilegio = []
            for r in roles:
                 privi.append(r.id)
            for p in privi:
                 roles5 = Rol.objects.get(pk=p)
                 priv = roles5.privilegios.all()
                 for pr in priv:
                     privilegios.append(pr.codename)
            for i in privilegios:
                 if i not in privilegio:
                     privilegio.append(i)
            context['usuario'] = privilegio

            if 'form' not in context:
                context['form']= self.form_class(self.request.GET)
            if 'form2' not in context:
                context['form2']= self.second_form_class(self.request.GET)

            return context

        def post(self, request, *args, **kwargs):
              self.object= self.get_object
              form= self.form_class(request.POST)
              form2 = self.second_form_class(request.POST)
              if form.is_valid() and form2.is_valid():

                   perfil= form.save(commit=False)
                   perfil.user=form2.save()
                   perfil.user.set_password(form2.cleaned_data['password'])
                   perfil.user.save()
                   perfil.save()
                   form.save_m2m()
                   data = form2.cleaned_data
                   usu = data['username']
                   passw = data['password']
                   subject = 'Usuario creado exitosamente'
                   text_content = 'This is an important message.'
                   html_content = '<p>Username:<strong>' + usu + '</strong></p><p>Password:<strong>' + passw + '</strong></p>'
                   msg = EmailMultiAlternatives(
                       subject,
                       text_content,
                       'admin@mail.com',  # FROM
                       [data['email']]
                   )
                   msg.attach_alternative(html_content, "text/html")
                   msg.send()
                   messages.success(request,('Se ha registrado satisfactoriamente'),extra_tags='alert')
                   return HttpResponseRedirect(self.get_success_url())

              else:
                   messages.error(request,('Por favor registrese nuevamente'))
                   return self.render_to_response(self.get_context_data(form=form, form2=form2))


class ActualizarUsuario(UpdateView):
    model = Perfil
    second_model = User
    template_name = "usuario/update.html"
    form_class = RegistroForm
    second_form_class = UserForm
    success_url = reverse_lazy('usuario:registrar')
    def get_context_data(self, **kwargs):
            context = super(ActualizarUsuario, self).get_context_data(**kwargs)
            pk = self.kwargs.get('pk', 0)
            perfil = self.model.objects.get(id=pk)
            usuario = self.second_model.objects.get(id=perfil.user_id)

            roles = perfil.roles.all()
            privi = []
            privilegios = []
            privilegio = []
            for r in roles:
                privi.append(r.id)
            for p in privi:
                roles5 = Rol.objects.get(pk=p)
                priv = roles5.privilegios.all()
                for pr in priv:
                    privilegios.append(pr.codename)

            for i in privilegios:
                 if i not in privilegio:
                     privilegio.append(i)
            context['usuario'] = privilegio
            if 'form' not in context:
                context['form'] = self.form_class()
            if 'form2' not in context:
                context['form2'] = self.second_form_class(instance=usuario)
            context['id'] = pk
            return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']
        perfil = self.model.objects.get(id=id_solicitud)
        usuario = self.second_model.objects.get(id=perfil.user_id)
        form = self.form_class(request.POST, instance=perfil)
        form2 = self.second_form_class(request.POST, instance=usuario)
        if form.is_valid() and form2.is_valid():

            perfil = form.save(commit=False)
            perfil.user = form2.save()

            perfil.user.save()
            perfil.save()
            form.save_m2m()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))