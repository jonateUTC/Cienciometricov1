from django.db import models
from django.db import models
from apps.provincia.models import provincia
# Create your models here.
class canton (models.Model):
    Nombre=models.CharField(max_length=155)
    provincia=models.ForeignKey(provincia,null=True ,blank=True ,on_delete=models.CASCADE)