from django.db import models
from apps.Investigador.models import investigador
# Create your models here.
class revista(models.Model):

 Nombre = models.CharField(max_length=500)
 Archivo = models.FileField(upload_to='revista/')
 uploaded_at = models.DateTimeField(auto_now_add=True)
 investigador = models.ForeignKey(investigador, null=True, blank=True, on_delete=models.CASCADE)
 ISSN=models.CharField(max_length=250)
 Base_Indexada=models.CharField(max_length=500)
 Cuartil_Pertenece=models.CharField(max_length=500)
 Factor_Impacto=models.CharField(max_length=500)
 Url=models.URLField()

 class Meta:
  permissions = (
   ("ver_Revista", "ver Revista"),
  )
