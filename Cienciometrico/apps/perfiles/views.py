from django.shortcuts import render,HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from apps.perfiles.form import UserForm
from apps.perfiles.models import User
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
# Create your views here.
class UserList(ListView):
    model = User
    template_name = 'User/User_listar.html'
    paginate_by = 6

class UserCreate(CreateView):
    model = User
    form_class = UserForm
    template_name = 'User/User_crear.html'
    success_url = reverse_lazy('User:User_lis')
    def get_context_data(self, **kwargs):
        context= super(UserCreate,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']= self.form_class(self.request.GET)
        return context
    def post(self, request, *args, **kwargs):
        self.object= self.get_object
        form= self.form_class(request.POST)
        if form.is_valid():
            solicitud= form.save(commit=False)
            solicitud.set_password(form.cleaned_data['password'])
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'User/User_update.html'
    success_url = reverse_lazy('User:User_lis')
class UserDelete(DeleteView):
    model = User
    template_name = 'User/User_delete.html'
    success_url = reverse_lazy('User:User_lis')