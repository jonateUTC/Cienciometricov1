from django.db import models
from django.contrib.auth.models import User
from apps.roles.models import Rol
# Create your models here.
class Perfil(models.Model):
    Cedula = models.CharField(max_length=10, blank=True)
    Documento = models.FileField(upload_to='foto/', null=True,blank=True)
    Direccion = models.CharField(max_length=500, blank=True)
    Coordenadas = models.CharField(max_length=450, blank=True)
    Telefono = models.CharField(max_length=10, blank=True)
    Genero = models.CharField(max_length=100, blank=True)
    Ciudadania = models.CharField(max_length=100, blank=True)
    roles = models.ManyToManyField(Rol)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}  {}'.format(self.Cedula, self.Direccion)

    # Permisos

    class Meta:
        permissions = (
            ("ver_perfil", "ver perfil"),
        )