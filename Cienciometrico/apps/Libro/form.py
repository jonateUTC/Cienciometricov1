from django import forms

from apps.Libro.models import libro


class DocumentForm(forms.ModelForm):
    class Meta:
        model = libro
        fields = [
            'Titulo',
            'Resumen',
            'PalabrasClave',
            'Documento',
            'ISBN',
            'UbicacionFisica',
            'Anio',
            'Editorial',
            'Url',




        ]
        labels = {
            'Titulo':'Título del Libro',
            'Resumen': 'Resumen del Libro',
            'PalabrasClave': 'Palabras Claves',
            'Documento':'Adjuntar Archivo',
            'ISBN':'ISBN',
            'UbicacionFisica':'Ubicación Física del Libro',
            'Anio':'Año',
            'Editorial': 'Editorial',
            'Url':'URL',


        }
        widgets = {
            'Titulo':forms.TextInput(attrs={'class': 'form-control'}),
            'Resumen': forms.TextInput(attrs={'class': 'form-control'}),
            'PalabrasClave': forms.TextInput(attrs={'class': 'form-control', 'id': 'tags','placeholder':'Palabras Claves'}),
            'Documento':forms.FileInput(attrs={'class': 'form-control'}),
            'ISBN':forms.TextInput(attrs={'class': 'form-control'}),
            'UbicacionFisica':forms.TextInput(attrs={'class': 'form-control'}),
            'Anio': forms.TextInput(attrs={'class': 'form-control'}),
            'Editorial':forms.TextInput(attrs={'class': 'form-control'}),
            'Url':forms.URLInput(attrs={'class': 'form-control'}),


        }
