from django.db import models

# Create your models here.
from apps.carrera.models import carrera
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class investigador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Cedula=models.CharField(max_length=10, blank=True)
    Direccion=models.CharField(max_length=500, blank=True)
    Coordenadas= models.CharField(max_length=450, blank=True)
    Telefono=models.CharField(max_length=10,blank=True)
    Genero=models.CharField(max_length=100, blank=True)
    Ciudadania=models.CharField(max_length=100, blank=True)
    carrera=models.ManyToManyField(carrera)

    def __str__(self):
        return '{}  {}'.format(self.user.first_name,self.user.last_name)

@receiver(post_save, sender=User)
def create_user_investigador(sender, instance, created, **kwargs):
    if created:
        investigador.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_investigador(sender, instance, **kwargs):
    instance.investigador.save()

