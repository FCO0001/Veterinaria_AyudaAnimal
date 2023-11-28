
from django.db import models
from django.conf import settings
from pacientes.models import pacientes
 

class Diagnostico(models.Model):
    medico = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paciente = models.ForeignKey('pacientes.pacientes', on_delete=models.CASCADE)  # Reemplaza 'PacienteModel' con tu modelo de paciente
    sintomas = models.TextField()
    diagnostico_ia = models.TextField(blank=True, null=True)
    diagnostico_medico = models.TextField()

    def __str__(self):
        return f"Diagnóstico para {self.paciente}"


class HistoriaClinica(models.Model):
    veterinario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paciente = models.ForeignKey(pacientes, on_delete=models.CASCADE)  # Vinculación con el modelo Paciente
    fecha = models.DateTimeField(auto_now_add=True)
    hallazgos_examen = models.TextField()
    recomendaciones = models.TextField()

    # Estos campos son para referenciar el diagnóstico y síntomas/observaciones
    diagnostico_id = models.IntegerField()  # ID del diagnóstico (de la sección de diagnóstico IA y médico)
    sintomas_observaciones_id = models.IntegerField()  # ID de síntomas y observaciones

    def __str__(self):
        return f"Historia Clínica de {self.paciente.nombre} - {self.fecha.strftime('%Y-%m-%d')}"
    


class RecetaMedica(models.Model):
    veterinario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paciente = models.ForeignKey(pacientes, on_delete=models.CASCADE)  # Asume un modelo Paciente existente
    medicamento = models.CharField(max_length=100)
    dosificacion = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=100)
    duracion = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Receta para {self.paciente.nombre} - {self.medicamento}"
    

class InstruccionesPostConsulta(models.Model):
    veterinario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paciente = models.ForeignKey(pacientes, on_delete=models.CASCADE)  # Asume un modelo Paciente existente
    instrucciones = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Instrucciones Post-Consulta para {self.paciente.nombre}"


class ResultadosPruebas(models.Model):
    veterinario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paciente = models.ForeignKey(pacientes, on_delete=models.CASCADE)  # Asume un modelo Paciente existente
    descripcion_pruebas = models.TextField()
    resultados = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resultados de Pruebas para {self.paciente.nombre}"

class PlanTratamiento(models.Model):
    veterinario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paciente = models.ForeignKey(pacientes, on_delete=models.CASCADE)  # Asume un modelo Paciente existente
    descripcion = models.TextField()
    citas_seguimiento = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"Plan de Tratamiento para {self.paciente.nombre}"



class Factura(models.Model):
    veterinario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paciente = models.ForeignKey(pacientes, on_delete=models.CASCADE)  # Asume un modelo Paciente existente
    detalles = models.TextField()  # Aquí puedes almacenar un resumen detallado de los costos
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_emision = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Factura para {self.paciente.nombre} - Total: {self.total}"


class Clinica(models.Model):
    nombre = models.CharField(max_length=100, default='Clínica Veterinaria Ejemplo')
    direccion = models.CharField(max_length=255, default='123 Calle Principal')
    telefono = models.CharField(max_length=20, default='+1234567890')
    telefono_emergencia = models.CharField(max_length=20, default='+0987654321')
    email = models.EmailField(default='info@clinicaveterinariaejemplo.com')

    def __str__(self):
        return self.nombre

# Create your models here.
