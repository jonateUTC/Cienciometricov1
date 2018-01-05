from django.db import models

# Create your models here.
from  apps.Investigador.models import investigador
class publicaciones(models.Model):
     Titulo = models.CharField(max_length=500)
     Nivel_Autoria=models.IntegerField()
     investigador = models.ForeignKey(investigador, null=True, blank=True, on_delete=models.CASCADE)
     Palabras_Clave = models.CharField(max_length=500)
     Resumen = models.FileField(upload_to='publicaciones/')
     uploaded_at = models.DateTimeField(auto_now_add=True)
     Fecha = models.DateField()
     Editorial = models.CharField(max_length=500)
     DB_Indexada=models.CharField(max_length=500)
     Url=models.URLField()