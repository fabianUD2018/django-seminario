from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class Restaurante(models.Model):
    name = models.CharField(max_length= 50, verbose_name ='nombre del restaurante')
    owner = models.CharField(max_length=50, verbose_name = 'Dueño del chuzo')
    address = models.CharField(max_length=50)
    phone = models.IntegerField(null =True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True) 

    def __str__(self):
        return self.name