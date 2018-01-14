from apps.perfiles.models import Perfil
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistroForm(forms.ModelForm):
    class Meta:
        model= Perfil
        fields = [
            'Cedula',
            'Direccion',
            'Coordenadas',
            'Telefono',
            'Genero',
            'Ciudadania',
            'roles',


        ]
        labels = {
            'Cedula': 'Cedula',
            'Direccion': 'Direccion',
            'Coordenadas': 'Coordenadas',
            'Telefono': 'Telefono',
            'Genero': 'Genero',
            'Ciudadania': 'Ciudadania',
            'roles': 'Roles',
        }

        widgets = {

            'Cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'Coordenadas': forms.TextInput(attrs={'class': 'form-control'}),
            'Telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'Genero': forms.TextInput(attrs={'class': 'form-control'}),
            'Ciudadania': forms.TextInput(attrs={'class': 'form-control'}),
            'roles': forms.CheckboxSelectMultiple(),

        }


class UserForm (forms.ModelForm):
    class Meta:
        model = User
        fields=[
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'is_staff',
        ]
        labels={
            'username':'username',
            'password':'password',
            'first_name':'first_name',
            'last_name':'last_name',
            'email':'email',
            'is_staff':'is_staff',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_staff': forms.CheckboxInput(),


        }