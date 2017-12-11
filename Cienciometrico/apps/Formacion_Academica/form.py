from django import forms
from apps.Formacion_Academica.models import formacion_academica

class FormacionAform (forms.ModelForm):
    class Meta:
        model=formacion_academica
        fields=[
            'Nivel_Estudios',
            'Fecha_Fin_Estudios',
            'Nombre_Centro_Estudios',
            'investigador',

        ]
        labels={
            'Nivel_Estudios':'Nivel_Estudios' ,
            'Fecha_Fin_Estudios' :'Fecha_Fin_Estudios',
            'Nombre_Centro_Estudios':'Nombre_Centro_Estudios',
            'investigador':'Investigador',
        }

        widgets = {
            'Nivel_Estudios':forms.TextInput(attrs={'class':'form-control'}),
            'Fecha_Fin_Estudios':forms.DateInput(attrs={'class':'form-control'}),
            'Nombre_Centro_Estudios':forms.TextInput(attrs={'class':'form-control'}),
            'investigador':forms.Select(attrs={'class':'form-control'}),

        }
