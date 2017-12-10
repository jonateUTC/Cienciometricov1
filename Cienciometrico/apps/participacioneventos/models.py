from django.db import models

# Create your models here.
class participacionevento(models.Model):

    Titulo = models.CharField(max_length=255)
    Nivel_Autoria=models.CharField(max_length=255)
    Palabras_Clave = models.TextField()
    Resumen = models.FileField(upload_to='eventos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    Nombre_Evento=models.CharField(max_length=255)
    Nivel=models.IntegerField()
    Lugar_Evento=models.CharField(max_length=255)