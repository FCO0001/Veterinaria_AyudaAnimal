from django.db import models

# Create your models here.

class Medico(models.Model):
    nombre = models.CharField(max_length=200, default="juanito")
    
    def __str__(self):
        return self.nombre
    

    