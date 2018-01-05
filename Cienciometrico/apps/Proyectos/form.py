from django import forms

from apps.Proyectos.models import proyecto


class DocumentForm(forms.ModelForm):
    class Meta:
        model = proyecto
        fields = [
            'Titulo',
            'Palabras_Claves',
            'Documentos',
            'Tipo',
            'investigador',

        ]
        labels = {
            'Titulo':'Título',
            'Palabras_Claves':'Palabras Clave',
            'Documentos':'Documentos',
            'Tipo':'Tipo de Proyecto',
            'investigador':'Investigador',

        }
        widgets = {
            'Titulo': forms.TextInput   (attrs={'class': 'form-control'}),
            'Palabras_Claves':forms.Textarea(attrs={'class':'form-control'}),
            'Documentos': forms.FileInput(attrs={'class': 'form-control'}),
            'Tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'investigador': forms.Select(attrs={'class': 'form-control'}),

        }
