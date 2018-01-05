from django.db import models
from apps.Investigador.models import investigador
# Create your models here.
class proyecto(models.Model):
    Titulo = models.CharField(max_length=255)
    Palabras_Claves = models.TextField()
    Documentos = models.FileField(upload_to='proyecto/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    Tipo = models.CharField(max_length=255)
    investigador = models.ForeignKey(investigador, null=True, blank=True, on_delete=models.CASCADE);

    class Meta:
        permissions = (
            ("ver_Proyectos", "ver Proyectos"),
        )