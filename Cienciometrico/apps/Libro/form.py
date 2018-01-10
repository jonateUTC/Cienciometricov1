from django import forms

from apps.Libro.models import libro


class DocumentForm(forms.ModelForm):
    class Meta:
        model = libro
        fields = [
            'Titulo',
            'Editorial',
            'ISBN',
            'Resumen',
            'Ubicacion',
            'Url',
            'Anio',
            'user',
            'PalabrasClave',

        ]
        labels = {
            'Titulo':'Titulo',
            'Editorial':'Editorial',
            'ISBN':'ISBN',
            'Resumen':'Resumen',
            'Ubicacion':'Ubicacion',
            'Url':'URL',
            'Anio':'Año',
            'user':'Investigador',
            'PalabrasClave':'Palabras Claves',

        }
        widgets = {
            'Titulo':forms.TextInput(attrs={'class': 'form-control'}),
            'Editorial':forms.TextInput(attrs={'class': 'form-control'}),
            'ISBN':forms.TextInput(attrs={'class': 'form-control'}),
            'Resumen':forms.FileInput(attrs={'class': 'form-control'}),
            'Ubicacion':forms.TextInput(attrs={'class': 'form-control'}),
            'Url':forms.URLInput(attrs={'class': 'form-control'}),
            'Anio':forms.TextInput(attrs={'class': 'form-control'}),
            'user':forms.CheckboxSelectMultiple(attrs={}),
            'PalabrasClave':forms.TextInput(attrs={'class': 'form-control','id':'tags'}),

        }
