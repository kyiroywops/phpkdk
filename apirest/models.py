from django.db import models

# Create your models here.

class productos(models.Model):
    id = models.AutoField(primary_key=True, null = False)
    ean13 = models.CharField(max_length=13, null = False)
    nombre = models.CharField(max_length=100, null = False)
    creacion = models.DateTimeField(null= False)
    minimo = models.IntegerField(null= True)
