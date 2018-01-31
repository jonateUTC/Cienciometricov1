from django.db import models

# Create your models here.
from apps.perfiles.models import User
class libro(models.Model):
    Titulo=models.CharField(max_length=200, null=True, blank=True)
    Resumen=models.TextField(null=True)
    PalabrasClave = models.CharField(max_length=300, null=True, blank=True)
    Documento=models.FileField(upload_to='libro/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    ISBN = models.CharField(max_length=50, null=True, blank=True)
    UbicacionFisica=models.CharField(max_length=50, null=True, blank=True)
    Anio=models.CharField(max_length=5, null=True, blank=True)
    Editorial = models.CharField(max_length=50, null=True, blank=True)
    Url = models.URLField(null=True, blank=True)



    def __str__(self): return '{}'.format(self.Titulo)

    class Meta:
        permissions = (
            ("ver_libro", "ver libro"),
        )
