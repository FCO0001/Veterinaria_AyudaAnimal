from django.db import models

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=200) # para tipos de datos string 
    especies = (
        ("1","Gato"), 
        ("2","Perro"), 
        ("3","Exótico"),
    )
    especie = models.CharField(max_length=200, choices=especies)
    raza = models.CharField(max_length=200)
    edad = models.IntegerField() # para tipos de datos numericos 
    nombre_dueño = models.CharField(max_length=200)
    run_dueño = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

