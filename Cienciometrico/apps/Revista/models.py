from django.db import models
from apps.Investigador.models import investigador
# Create your models here.
class revista(models.Model):

 Nombre = models.CharField(max_length=500,unique=True)
 Archivo = models.FileField(upload_to='revista/', null=True, blank=True)
 uploaded_at = models.DateTimeField(auto_now_add=True,null=True)
 investigador = models.ForeignKey(investigador, null=True, blank=True, on_delete=models.CASCADE)
 ISSN=models.CharField(max_length=250,null=True,blank=True)
 Base_Indexada=models.CharField(max_length=500,null=True,blank=True)
 Cuartil_Pertenece=models.CharField(max_length=500,null=True,blank=True)
 Factor_Impacto=models.CharField(max_length=500,null=True,blank=True)
 Url=models.URLField(null=True,blank=True)

 class Meta:
  permissions = (
   ("ver_Revista", "ver Revista"),
  )
