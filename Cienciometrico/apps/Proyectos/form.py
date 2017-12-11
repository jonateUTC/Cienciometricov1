from django import forms

from apps.Proyectos.models import proyecto
class ProyectoForm(forms.ModelForm):
    class Meta:
        model = proyecto
        fields = [
            'Titulo',
            'Palabras_Clave',
            'Documentos',
            'Tipo_Proyecto',
            'investigador',
            
        ]
        labels = {
            'Titulo':'Título',
            'Palabras_Clave':'Palabras Clave',
            'Documentos':'Documentos',
            'Tipo_Proyecto':'Tipo Proyecto',
            'investigador':'investigador',
         }
        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'Palabras_Clave':forms.Textarea(attrs={'class':'form-control'}),
            'Documentos': forms.FileInput(attrs={'class': 'form-control'}),
            'Tipo_Proyecto': forms.TextInput(attrs={'class': 'form-control'}),
            'investigador':forms.Select(attrs={'class': 'form-control'}),
        }
