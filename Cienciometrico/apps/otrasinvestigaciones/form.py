from django import forms

from apps.otrasinvestigaciones.models import otrasinvestigaciones
class DocumentForm(forms.ModelForm):
    class Meta:
        model = otrasinvestigaciones
        fields = [
            'Titulo',
            'Palabras_Clave',
            'Resumen',
            'Editor',
            'Estado_Investigacion',
            'Url',
        ]
        labels = {
            'Titulo':'Título',
            'Palabras_Clave':'Palabras Clave',
            'Resumen':'Resumen',
            'Editor':'Editor',
            'Estado_Investigacion':'Estado Investigación',
            'Url':'Link',
        }
        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'Palabras_Clave':forms.Textarea(attrs={'class':'form-control','id':'tags'}),
            'Resumen': forms.FileInput(attrs={'class': 'form-control'}),
            'Editor': forms.TextInput(attrs={'class': 'form-control'}),
            'Estado_Investigacion':forms.Textarea(attrs={'class': 'form-control'}),
            'Url': forms.URLInput(attrs={'class': 'form-control'}),
        }
