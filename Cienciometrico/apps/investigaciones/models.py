from django.db import models

# Create your models here.
class investigacion(models.Model):
    Titulo = models.CharField(max_length=255)
    Palabras_Claves = models.TextField()
    Resumen = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    Fecha = models.DateField()
    Editor = models.CharField(max_length=255)
    Url = models.URLField();