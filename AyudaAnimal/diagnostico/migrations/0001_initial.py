# Generated by Django 4.2.5 on 2023-11-28 02:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Clínica Veterinaria Ejemplo', max_length=100)),
                ('direccion', models.CharField(default='123 Calle Principal', max_length=255)),
                ('telefono', models.CharField(default='+1234567890', max_length=20)),
                ('telefono_emergencia', models.CharField(default='+0987654321', max_length=20)),
                ('email', models.EmailField(default='info@clinicaveterinariaejemplo.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ResultadosPruebas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_pruebas', models.TextField()),
                ('resultados', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.pacientes')),
                ('veterinario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecetaMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicamento', models.CharField(max_length=100)),
                ('dosificacion', models.CharField(max_length=100)),
                ('frecuencia', models.CharField(max_length=100)),
                ('duracion', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.pacientes')),
                ('veterinario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlanTratamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('citas_seguimiento', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.pacientes')),
                ('veterinario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InstruccionesPostConsulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrucciones', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.pacientes')),
                ('veterinario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('hallazgos_examen', models.TextField()),
                ('recomendaciones', models.TextField()),
                ('diagnostico_id', models.IntegerField()),
                ('sintomas_observaciones_id', models.IntegerField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.pacientes')),
                ('veterinario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalles', models.TextField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_emision', models.DateTimeField(auto_now_add=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.pacientes')),
                ('veterinario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sintomas', models.TextField()),
                ('diagnostico_ia', models.TextField(blank=True, null=True)),
                ('diagnostico_medico', models.TextField()),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.pacientes')),
            ],
        ),
    ]
