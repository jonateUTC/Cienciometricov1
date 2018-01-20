# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from apps.Investigador.models import investigador


# Create your models here.
class articulos_cientificos (models.Model):
    Nombre=models.CharField(max_length=250,blank=True,null=True,unique=True)
    Resumen = models.CharField(max_length=250, blank=True, null=True)
    PalabrasClaves = models.CharField(max_length=250, blank=True, null=True)
    Documento = models.FileField(upload_to='articulos/',null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    NombreRevista = models.CharField(max_length=250, blank=True, null=True)
    Volumen = models.CharField(max_length=250, blank=True, null=True)
    Numero=models.CharField(max_length=250,blank=True,null=True)
    ISSN=models.CharField(max_length=250,blank=True,null=True)
    Base_Datos=models.CharField(max_length=250,blank=True,null=True)
    Url=models.URLField(blank=True,null=True)
    Fecha_Publicacion=models.DateField(blank=True,null=True)

    class Meta:
        permissions = (
            ("ver_articulo", "ver articulo"),
        )

