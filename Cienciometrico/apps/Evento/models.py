# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class evento(models.Model):
    Nombre=models.CharField(max_length=250,null=True)
    Lugar=models.CharField(max_length=250,null=True)
    Fecha=models.DateField(null=True)

