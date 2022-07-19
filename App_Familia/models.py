from django.db import models

# Create your models here.


class Familia(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    altura = models.FloatField()
    fecha_de_nacimiento = models.DateField(null=False, max_length=50)


class Amigos(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    altura = models.FloatField()
    fecha_de_nacimiento = models.DateField(null=False, max_length=50)

class Mascotas(models.Model):

    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    peso = models.FloatField()
    fecha_de_nacimiento = models.DateField(null=False, max_length=50)