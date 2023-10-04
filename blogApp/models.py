from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatar")
    user = models.ForeignKey(User,on_delete=models.CASCADE, null = True, blank = True)

class AgregarPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    imagen = models.ImageField( upload_to="avatar", null=False, blank=False)
    fechaPublicacion = models.DateTimeField(null=False, blank=False)

    class Meta:
        ordering = ['user', '-fechaPublicacion']

    def __str__(self):
        return self.titulo
    
