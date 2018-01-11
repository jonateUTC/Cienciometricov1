from django import forms

from apps.participacioneventos.models import participacionevento
class DocuForm(forms.ModelForm):
    class Meta:
        model = participacionevento
        fields = [
            'Titulo',
            'Nivel_Autoria',
            'Palabras_Clave',
            'Resumen',
            'Nombre_Evento',
            'Nivel',
            'Lugar_Evento',
        ]
        labels = {
            'Titulo':'Título',
            'Nivel_Autoria':'Nivel de Autoria',
            'Palabras_Clave':'Palabras Clave',
            'Resumen':'Resumen',
            'Nombre_Evento':'Nombre del Evento',
            'Nivel':'Nivel',
            'Lugar_Evento':'Lugar del Evento',
        }
        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'Nivel_Autoria':forms.TextInput(attrs={'class': 'form-control'}),
            'Palabras_Clave':forms.Textarea(attrs={'class':'form-control','id':'tags'}),
            'Resumen': forms.FileInput(attrs={'class': 'form-control'}),
            'Nombre_Evento': forms.TextInput(attrs={'class': 'form-control'}),
            'Nivel':forms.NumberInput(attrs={'class': 'form-control'}),
            'Lugar_Evento': forms.TextInput(attrs={'class': 'form-control'}),
        }
