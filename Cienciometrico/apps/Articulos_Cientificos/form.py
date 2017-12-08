from django import forms
from apps.Articulos_Cientificos.models import articulos_cientificos

class articuloform(forms.ModelForm):
    class Meta:
        model=articulos_cientificos
        fields=[
            'Nombre',
            'Numero',
            'Estado',
            'Anio',
            'ISSN',
            'Base_Datos',
            'Url',
            'Fecha_Publicacion',
            'investigador',

        ]
        labels={
            'Nombre':'Nombre',
            'Numero':'Numero',
            'Estado':'Estado',
            'Anio':'Anio',
            'ISSN':'ISSN',
            'Base_Datos':'Base de Datos',
            'Url':'URL',
            'Fecha_Publicacion':'Fecha Publicacion',
            'investigador':'Investigador',
        }
        widgets={
            'Nombre':forms.TextInput(attrs={'class':'form-control'}),
            'Numero':forms.TextInput(attrs={'class':'form-control'}),
            'Estado':forms.TextInput(attrs={'class':'form-control'}),
            'Anio':forms.DateInput(attrs={'class':'form-control'}),
            'ISSN':forms.TextInput(attrs={'class':'form-control'}),
            'Base_Datos':forms.TextInput(attrs={'class':'form-control'}),
            'Url':forms.URLInput(attrs={'class':'form-control'}),
            'Fecha_Publicacion':forms.DateInput(format='%d/%m/%y', attrs={'class':'form-control'}),
            'investigador':forms.Select(attrs={'class':'form-control'}),
         }