from django.db import models

class Products(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    esta_vivo = models.BooleanField()


