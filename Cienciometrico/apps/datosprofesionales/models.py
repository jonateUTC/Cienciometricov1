from django.db import models

# Create your models here.
class datos_profecionales(models.Model):
    Nombre_Profecion=models.CharField(max_length=255)
    Grado_Cientifico=models.CharField(max_length=255)
    Categoria=models.CharField(max_length=255)