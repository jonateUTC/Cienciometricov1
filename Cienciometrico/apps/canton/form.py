from django import forms
from apps.canton.models import canton
class CantonForm(forms.ModelForm):
    class Meta:
        model= canton
        fields= [
            'Nombre',
            'provincia',
        ]
        labels={
            'Nombre':'Nombre',
            'provincia': 'Provincias',
        }
        widgets={
            'Nombre':forms.TextInput(attrs={'class':'form-control'}),
            'provincia': forms.Select(attrs={'class': 'form-control'}),
        }