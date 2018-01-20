from django import forms

from apps.Proyectos.models import proyecto


class DocumentForm(forms.ModelForm):
    class Meta:
        model = proyecto
        fields = [

            'Titulo',
            'Resumen',
            'Palabras_Claves',
            'Tipo',
            'LineaInvestigacion',
            'Documentos',

        ]
        labels = {
            'Titulo':'Título',
            'Palabras_Claves':'Palabras Clave',
            'LineaInvestigacion':'Linea de Investigacion',
            'Tipo':'Tipo de Proyecto',
            'Documentos':'Documentos',


        }
        widgets = {
            'Titulo': forms.TextInput   (attrs={'class': 'form-control'}),
            'Resumen':forms.TextInput   (attrs={'class': 'form-control'}),
            'Palabras_Claves':forms.TextInput(attrs={'class':'form-control','id':'tags','placeholder':'Palabras Claves'}),
            'Tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'LineaInvestigacion': forms.TextInput(attrs={'class': 'form-control'}),
            'Documentos': forms.FileInput(attrs={'class': 'form-control'}),
        }
