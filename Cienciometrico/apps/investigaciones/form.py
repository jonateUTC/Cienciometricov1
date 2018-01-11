from django import forms

from apps.investigaciones.models import investigacion


class DocumentForm(forms.ModelForm):
    class Meta:
        model = investigacion
        fields = [
            'Titulo',
            'Palabras_Claves',
            'Resumen',
            'Fecha',
            'Editor',
            'Url',
        ]
        labels = {
            'Titulo':'Título',
            'Palabras_Claves':'Palabras Clave',
            'Resumen':'Resumen',
            'Fecha':'Fecha',
            'Editor':'Editor',
            'Url':'Link',
        }
        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'Palabras_Claves':forms.Textarea(attrs={'class':'form-control'}),
            'Resumen': forms.FileInput(attrs={'class': 'form-control'}),
            'Fecha': forms.DateInput(attrs={'class': 'form-control'}),
            'Editor': forms.TextInput(attrs={'class': 'form-control'}),
            'Url': forms.URLInput(attrs={'class': 'form-control'}),
        }
