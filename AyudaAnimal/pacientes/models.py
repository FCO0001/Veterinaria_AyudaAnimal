from django.db import models

# Create your models here.
class pacientes(models.Model):
    nombre = models.CharField(max_length=200, default="jorge")
    
    def __str__(self):
        return self.nombre