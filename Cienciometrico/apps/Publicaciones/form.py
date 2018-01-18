from django import forms
from apps.Publicaciones.models import publicaciones

class formPublicaciones(forms.ModelForm):
    class Meta:
        model= publicaciones
        fields = [
        'Titulo',
        'Nivel_Autoria',
        'investigador',
        'Palabras_Clave',
        'Resumen',
        'Fecha',
        'Editorial',
        'DB_Indexada',
        'Url',
        ]
        labels={
            'Titulo': 'Titulo',
            'Nivel_Autoria':'Nivel_Autoria',
            'investigador':'Investigador',
            'Palabras_Clave':'Palabras Clave',
            'Resumen':'Resumen',
            'Fecha':'Fecha',
            'Editorial':'Editorial',
            'DB_Indexada':'DB Indexada',
            'Url':'Url',
        }
        widgets = {
            'Titulo': forms.TextInput(attrs={'class':'form-control'}),
            'Nivel_Autoria': forms.NumberInput(attrs={'class':'form-control'}),
            'investigador': forms.Select(attrs={'class':'form-control'}),
            'Palabras_Clave':forms.TextInput(attrs={'class':'form-control','id':'tags'}),
            'Resumen': forms.FileInput(attrs={'class':'form-control'}),
            'Fecha': forms.DateInput(attrs={'class':'datepicker','placeholder':'6/1/2018','title':'Ejemplo de Fecha : 6/1/2018'}),
            'Editorial': forms.TextInput(attrs={'class':'form-control'}),
            'DB_Indexada': forms.TextInput(attrs={'class':'form-control'}),
            'Url': forms.URLInput(attrs={'class': 'form-control'}),


        }