from django import forms
from apps.Revista.models import revista

class DocumentForm(forms.ModelForm):
    class Meta:
        model= revista
        fields = [
        'Nombre',
        'Archivo',
        'ISSN',
        'Base_Indexada',
        'Cuartil_Pertenece',
        'Factor_Impacto',
        'Url',
        'investigador',

        ]
        labels={
            'Nombre': 'Nombre',
            'Archivo': 'Archivo',
            'ISSN':'ISSN',
            'Base_Indexada':'Base Indexada',
            'Cuartil_Pertenece':'Cuartil Pertenece',
            'Factor_Impacto':'Factor Impacto',
            'Url':'Url',
            'investigador': 'Investigador',

        }
        widgets = {
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'Archivo': forms.FileInput(attrs={'class': 'form-control'}),
            'ISSN': forms.TextInput(attrs={'class':'form-control'}),
            'Base_Indexada': forms.TextInput(attrs={'class':'form-control'}),
            'Cuartil_Pertenece': forms.TextInput(attrs={'class':'form-control'}),
            'Factor_Impacto': forms.TextInput(attrs={'class':'form-control'}),
            'Url': forms.URLInput(attrs={'class':'form-control'}),
            'investigador': forms.Select(attrs={'class': 'form-control'}),

        }