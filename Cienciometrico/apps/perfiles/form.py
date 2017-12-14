from django import forms

from apps.perfiles.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'Cedula',
            'Coordenadas',
            'Telefono',
            'Genero',
            'Ciudadania',
            'username',
            'password',
            'is_universidad',
            'is_facultad',
            'is_investigador',
            'carrera',
            'facultad',
            'universidad',

        ]
        labels = {
            'first_name':'Nombres',
            'last_name':'Apellidos',
            'email':'Correo Electronico',
            'Cedula':'CI',
            'Coordenadas':'Coordenadas',
            'Telefono':'Telefono',
            'Genero':'Genero',
            'Ciudadania':'Ciudadania',
            'username':'Usuario',
            'password':'Contraseña',
            'is_universidad':'Perfil Universidad',
            'is_facultad':'Perfil Facultad',
            'is_investigador':'Perfil Investigador',
            'carrera':'Carrera',
            'facultad':'Facultad',
            'universidad':'Universidad',

        }
        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'Palabras_Claves':forms.Textarea(attrs={'class':'form-control'}),
            'Documentos': forms.FileInput(attrs={'class': 'form-control'}),
            'Tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'investigador': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'Coordenadas': forms.TextInput(attrs={'class': 'form-control'}),
            'Telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'Genero': forms.TextInput(attrs={'class': 'form-control'}),
            'Ciudadania': forms.TextInput(attrs={'class': 'form-control'}),
            'username':forms.TextInput(attrs={'class': 'form-control'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control'}),
            'is_universidad': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'is_facultad': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'is_investigador': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'carrera': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'facultad': forms.Select(attrs={'class': 'form-control'}),
            'universidad': forms.Select(attrs={'class': 'form-control'}),

        }
