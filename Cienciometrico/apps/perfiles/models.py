from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.carrera.models import carrera
from apps.universidad.models import universidad
from apps.facultad.models import facultad
# Create your models here.
class User(AbstractUser):
    Cedula = models.CharField(max_length=10,null=True ,blank=True)
    Direccion = models.CharField(max_length=500,null=True ,blank=True)
    Coordenadas = models.CharField(max_length=450,null=True ,blank=True)
    Telefono = models.CharField(max_length=10,null=True ,blank=True)
    Genero = models.CharField(max_length=100,null=True ,blank=True)
    Ciudadania = models.CharField(max_length=100,null=True ,blank=True)
    is_universidad = models.BooleanField(default=False)
    is_facultad = models.BooleanField(default=False)
    is_investigador = models.BooleanField(default=False)
    carrera = models.ManyToManyField(carrera)
    universidad = models.OneToOneField(universidad, on_delete=models.CASCADE,null=True ,blank=True)
    facultad = models.OneToOneField(facultad, on_delete=models.CASCADE,null=True ,blank=True)

    class Meta:
        db_table = 'auth_user'