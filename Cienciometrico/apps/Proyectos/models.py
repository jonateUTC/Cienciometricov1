from django.db import models
from apps.Investigador.models import investigador
# Create your models here.
class proyecto(models.Model):

    Titulo = models.CharField(max_length=255)
    Palabras_Clave = models.TextField()
    Documentos = models.FileField(upload_to='eventos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    Tipo_Proyecto=models.CharField(max_length=255)
    investigador = models.ForeignKey(investigador, null=True, blank=True, on_delete=models.CASCADE)
