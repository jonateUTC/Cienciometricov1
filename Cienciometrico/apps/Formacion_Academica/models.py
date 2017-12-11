# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from apps.Investigador.models import investigador
class formacion_academica(models.Model):
 Nivel_Estudios=models.CharField(max_length=250,null=True)
 Fecha_Fin_Estudios=models.DateField(null=True)
 Nombre_Centro_Estudios=models.CharField(max_length=250,null=True)
 investigador = models.ForeignKey(investigador, null=True, blank=True, on_delete=models.CASCADE)