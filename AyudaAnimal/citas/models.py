from django.db import models
from datetime import date
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.fields.related import ForeignKey
from usuarios.models import Medico
from pacientes.models import pacientes


def validar_dia(value):
    today = date.today()
    weekday = date.fromisoformat(f'{value}').weekday()

    if value < today:
        raise ValidationError('No puede elegir una fecha tardía a la fecha actual.')
    if (weekday == 5) or (weekday == 6):
        raise ValidationError('Elige un día laborable de la semana.')
# Create your models here.


class Cita_con_medico(models.Model):
    medico = ForeignKey(Medico, on_delete=models.CASCADE, related_name='Horas_medicos')
    Paciente = ForeignKey(pacientes,on_delete=models.CASCADE,related_name='Pacientes_medicos')
    dia = models.DateField(help_text="Introduzca una fecha para la cita", validators=[validar_dia],default=date.today)
    HORARIOS = (
        ("1", "07:00 AM a 08:00 AM"),
        ("2", "08:00 AM a 09:00 AM"),
        ("3", "09:00 AM a 10:00 AM"),
        ("4", "10:00 AM a 11:00 AM"),
        ("5", "11:00 AM a 12:00 PM"),
    )
    horario = models.CharField(max_length=10, choices=HORARIOS,default=date.today)
    
    class Meta:
        unique_together = ('horario', 'dia')
        
    
    def __str__(self):
        return f"{self.Paciente} con {self.medico} el {self.dia} a las {self.horario}"



