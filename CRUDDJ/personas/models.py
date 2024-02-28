from django.db import models

# Create your models here.
class Personas(models.Model):
    documento=models.BigIntegerField()
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    correo=models.EmailField(max_length=50)