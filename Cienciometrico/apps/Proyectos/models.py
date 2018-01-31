from django.db import models
from apps.Investigador.models import investigador
# Create your models here.
class proyecto(models.Model):
    Titulo = models.CharField(max_length=255)
    Resumen=models.TextField()
    Palabras_Claves = models.TextField()
    Tipo = models.CharField(max_length=255)
    LineaInvestigacion = models.CharField(max_length=255)
    Documentos = models.FileField(upload_to='proyecto/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = (
            ("ver_Proyectos", "ver Proyectos"),
        )