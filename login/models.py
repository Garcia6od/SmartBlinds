from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    pass

class Alarma(models.Model):
        usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
        hora_open = models.TimeField()
        hora_close = models.TimeField()




