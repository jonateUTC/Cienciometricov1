from django import forms
from apps.datosprofesionales.models import datos_profecionales
class DatosProfeForm(forms.ModelForm):
    class Meta:
        model= datos_profecionales
        fields= [
            'Nombre_Profecion',
            'Grado_Cientifico',
            'Categoria',

        ]
        labels={
            'Nombre_Profecion':'Nombre Profeción',
            'Grado_Cientifico':'Grado Científico',
            'Categoria':'Categoría',

        }
        widgets={
            'Nombre_Profecion':forms.TextInput(attrs={'class':'form-control'}),
            'Grado_Cientifico': forms.TextInput(attrs={'class': 'form-control'}),
            'Categoria':forms.TextInput(attrs={'class': 'form-control'}),

        }