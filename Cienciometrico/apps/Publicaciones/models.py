from django.db import models

# Create your models here.
from  apps.Investigador.models import investigador
class publicaciones(models.Model):
     Titulo = models.CharField(max_length=500)
     NombrePublica=models.TextField(null=True)
     UbicacionFisica=models.TextField(null=True)
     Url=models.URLField(null=True)

     class Meta:
          permissions = (
               ("ver_Publicaciones", "ver Publicaciones"),
          )