# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from apps.Investigador.models import investigador


# Create your models here.
class articulos_cientificos (models.Model):
    Nombre=models.CharField(max_length=250,blank=True,null=True)
    Numero=models.CharField(max_length=250,blank=True,null=True)
    Estado=models.CharField(max_length=250,blank=True,null=True)
    Anio=models.IntegerField(null=True)
    ISSN=models.CharField(max_length=250,blank=True,null=True)
    Base_Datos=models.CharField(max_length=250,blank=True,null=True)
    Url=models.URLField(blank=True,null=True)
    Fecha_Publicacion=models.DateField(blank=True,null=True)
    investigador = models.ForeignKey(investigador, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ("ver_articulo", "ver articulo"),
        )

