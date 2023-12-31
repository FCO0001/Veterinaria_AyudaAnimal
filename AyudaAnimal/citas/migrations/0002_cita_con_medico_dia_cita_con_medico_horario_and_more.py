# Generated by Django 4.2.5 on 2023-10-27 19:16

import citas.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('citas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita_con_medico',
            name='dia',
            field=models.DateField(default=datetime.date.today, help_text='Introduzca una fecha para la cita', validators=[citas.models.validar_dia]),
        ),
        migrations.AddField(
            model_name='cita_con_medico',
            name='horario',
            field=models.CharField(choices=[('1', '07:00 ás 08:00'), ('2', '08:00 ás 09:00'), ('3', '09:00 ás 10:00'), ('4', '10:00 ás 11:00'), ('5', '11:00 ás 12:00')], default=datetime.date.today, max_length=10),
        ),
        migrations.AddField(
            model_name='cita_con_medico',
            name='medico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Horas_medicos', to='usuarios.medico'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='cita_con_medico',
            unique_together={('horario', 'dia')},
        ),
        migrations.RemoveField(
            model_name='cita_con_medico',
            name='Fecha_hora',
        ),
        migrations.RemoveField(
            model_name='cita_con_medico',
            name='Nombre_doctor',
        ),
    ]
