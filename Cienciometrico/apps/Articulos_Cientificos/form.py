from django import forms
from apps.Articulos_Cientificos.models import articulos_cientificos

class articuloform(forms.ModelForm):
    class Meta:
        model=articulos_cientificos
        fields=[
            'Nombre',
            'Resumen',
            'PalabrasClaves',
            'Documento',
            'NombreRevista',
            'Volumen',
            'Numero',
            'ISSN',
            'Base_Datos',
            'Url',
            'Fecha_Publicacion',
        ]
        labels={
            'Nombre':'Título del Artículo',
            'Resumen':'Resumen del Artículo',
            'PalabrasClaves':'Palabras Claves',
            'Documento':'Adjuntar Documento',
            'NombreRevista':'Nombre de la Revista',
            'Volumen':'Volumen de Artículo',
            'Numero':'Número de Artículo',
            'ISSN':'ISSN',
            'Base_Datos':'Base de Datos donde esta indexada la Revista',
            'Url':'Url donde se encuentra la revista',
            'Fecha_Publicacion':'Fecha de Publicación de la Revista',
        }
        widgets={
            'Nombre':forms.TextInput(attrs={'class':'form-control'}),
            'Resumen':forms.TextInput(attrs={'class':'form-control'}),
            'PalabrasClaves':forms.TextInput(attrs={'class':'form-control','id':'tags','placeholder':'Palabras Claves'}),
            'Documento':forms.FileInput(attrs={'class':'form-control'}),
            'NombreRevista':forms.TextInput(attrs={'class':'form-control'}),
            'Volumen':forms.TextInput(attrs={'class':'form-control'}),
            'Numero':forms.NumberInput(attrs={'class':'form-control'}),
            'ISSN':forms.TextInput(attrs={'class':'form-control'}),
            'Base_Datos':forms.TextInput(attrs={'class':'form-control'}),
            'Url':forms.URLInput({'required':False}),
            'Fecha_Publicacion':forms.DateInput(format='%d/%m/%y', attrs={'class':'datepicker'}),

         }