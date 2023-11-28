from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from .models import HistoriaClinica, RecetaMedica, InstruccionesPostConsulta, ResultadosPruebas, PlanTratamiento, Factura, Clinica
from django.shortcuts import render
from openai import OpenAI
import os
def generar_pdf(paciente_id):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Obtener datos de la base de datos
    historia_clinica = HistoriaClinica.objects.get(paciente_id=paciente_id)
    receta_medica = RecetaMedica.objects.filter(paciente_id=paciente_id).first()
    instrucciones_post = InstruccionesPostConsulta.objects.filter(paciente_id=paciente_id).first()
    resultados_pruebas = ResultadosPruebas.objects.filter(paciente_id=paciente_id).first()
    plan_tratamiento = PlanTratamiento.objects.filter(paciente_id=paciente_id).first()
    factura = Factura.objects.filter(paciente_id=paciente_id).first()
    clinica = Clinica.objects.first()

    # Asumiendo que tienes funciones que devuelven texto formateado para cada sección
    # Ejemplo: 
    # historia_texto = formatear_historia_clinica(historia_clinica)
    # ...

    # Añadir texto al documento PDF
    # Ejemplo:
    # p.drawString(100, 800, historia_texto)
    # ...

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer


def obtener_prediagnostico(request):
    if request.method == 'POST':
        # Obtiene los síntomas del formulario
        sintomas = request.POST.get('sintomas', '')

        # Crear una instancia del cliente OpenAI
        client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

        try:
            # Llama a la API de OpenAI para obtener el prediagnóstico
            response = client.Completion.create(
                model="gpt-4",  # Utiliza el modelo que prefieras
                prompt=f"Diagnóstico médico para los siguientes síntomas: {sintomas}",
                max_tokens=50  # Ajusta esto según tus necesidades
            )
            prediagnostico = response.choices[0].text.strip()

            # Renderiza la plantilla con el prediagnóstico
            return render(request, 'Parciales/diagnosticoIA.html', {'prediagnostico': prediagnostico})

        except Exception as e:
            print(f"Error al obtener prediagnóstico: {e}")

    # Si no es una solicitud POST o si ocurre un error, muestra la página inicial
    return render(request, 'Parciales/diagnosticoIA.html', {})

