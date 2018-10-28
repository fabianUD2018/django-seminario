from django.db import models
from restaurante.models import Restaurante
# Create your models here.

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    def __str__(self):
        return self.nombre
    

class Platillo (models.Model):
    name = models.CharField(max_length=50 )
    precio = models.IntegerField()
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente)
    def __str__(self):
        return self.name
