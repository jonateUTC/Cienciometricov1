from django.db import models

# Create your models here.
class otrasinvestigaciones(models.Model):

 Titulo = models.CharField(max_length=255)
 Palabras_Clave = models.TextField()
 Resumen = models.FileField(upload_to='otrasinvestigaciones/')
 uploaded_at = models.DateTimeField(auto_now_add=True)
 Editor = models.CharField(max_length=250)
 Estado_Investigacion=models.CharField(max_length=255)
 Url = models.URLField();

 def __str__(self):
  return '{}'.format(self.Titulo)
