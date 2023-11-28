from django.contrib.auth.decorators import login_required
from .forms import HistoriaClinicaForm
from django.contrib import messages
from .forms import DiagnosticoForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecetaMedicaForm
from django.http import HttpResponse
from .utils import generar_pdf
from .models import HistoriaClinica, RecetaMedica, InstruccionesPostConsulta, ResultadosPruebas, PlanTratamiento, Factura, Clinica, Diagnostico
from django.shortcuts import render, redirect
from .utils import obtener_prediagnostico
from .forms import InstruccionesPostConsultaForm
from .forms import ResultadosPruebasForm
from .forms import PlanTratamientoForm
from .forms import FacturaForm
    

@login_required
def vista_prediagnostico(request):
    prediagnostico = None

    if request.method == 'POST':
        form = DiagnosticoForm(request.POST)
        if form.is_valid():
            if 'generar_prediagnostico' in request.POST:
                # Generar y mostrar prediagnóstico
                sintomas = form.cleaned_data['sintomas']
                prediagnostico = obtener_prediagnostico(sintomas)
            elif 'guardar_diagnostico' in request.POST:
                # Guardar diagnóstico final
                diagnostico = form.save(commit=False)
                diagnostico.medico = request.user
                diagnostico.save()
                # Redirigir a la siguiente etapa del flujo
                return redirect('crear_receta_medica', diagnostico_id=diagnostico.id)
    else:
        form = DiagnosticoForm()

    return render(request, 'Parciales/diagnosticoIA.html', {'form': form, 'prediagnostico': prediagnostico})


@login_required
def crear_receta_medica(request, diagnostico_id):
    diagnostico = get_object_or_404(Diagnostico, id=diagnostico_id)
    if request.method == 'POST':
        form = RecetaMedicaForm(request.POST)
        if form.is_valid():
            receta_medica = form.save(commit=False)
            receta_medica.veterinario = request.user
            receta_medica.save()
            return redirect('crear_instrucciones_post_consulta', diagnostico_id=diagnostico.id)
    else:
        form = RecetaMedicaForm()

    return render(request, 'Parciales/recetaMedica.html', {'form': form})

@login_required
def crear_historia_clinica(request, diagnostico_id):
    diagnostico = get_object_or_404(Diagnostico, id=diagnostico_id)
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST)
        if form.is_valid():
            historia_clinica = form.save(commit=False)
            historia_clinica.veterinario = request.user
            historia_clinica.diagnostico_id = diagnostico_id
            historia_clinica.save()
            return redirect('ruta_tras_creacion')
    else:
        form = HistoriaClinicaForm()

    return render(request, 'Parciales/historiaClinica.html', {'form': form, 'diagnostico': diagnostico})




@login_required
def crear_instrucciones_post_consulta(request, diagnostico_id):
    if request.method == 'POST':
        form = InstruccionesPostConsultaForm(request.POST)
        if form.is_valid():
            instrucciones_post_consulta = form.save(commit=False)
            instrucciones_post_consulta.veterinario = request.user
            instrucciones_post_consulta.save()
            return redirect('crear_resultados_pruebas', diagnostico_id=diagnostico_id)
    else:
        form = InstruccionesPostConsultaForm()

    return render(request, 'Parciales/instrucciones_post_consulta.html', {'form': form})



@login_required
def crear_resultados_pruebas(request, diagnostico_id):
    if request.method == 'POST':
        form = ResultadosPruebasForm(request.POST)
        if form.is_valid():
            resultados_pruebas = form.save(commit=False)
            resultados_pruebas.veterinario = request.user
            resultados_pruebas.save()
            return redirect('crear_plan_tratamiento', diagnostico_id=diagnostico_id)
    else:
        form = ResultadosPruebasForm()

    return render(request, 'Parciales/resultados_pruebas.html', {'form': form})



@login_required
def crear_plan_tratamiento(request, diagnostico_id):
    if request.method == 'POST':
        form = PlanTratamientoForm(request.POST)
        if form.is_valid():
            plan_tratamiento = form.save(commit=False)
            plan_tratamiento.veterinario = request.user
            plan_tratamiento.save()
            return redirect('crear_factura', diagnostico_id=diagnostico_id)
    else:
        form = PlanTratamientoForm()

    return render(request, 'Parciales/plan_tratamiento.html', {'form': form})


@login_required
def crear_factura(request, diagnostico_id):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            factura = form.save(commit=False)
            factura.veterinario = request.user
            factura.save()
            return redirect('crear_historia_clinica', diagnostico_id=diagnostico_id)
    else:
        form = FacturaForm()

    return render(request, 'Parciales/factura.html', {'form': form})



def descargar_pdf(request, paciente_id):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="historia_clinica.pdf"'

    buffer = generar_pdf(paciente_id)
    response.write(buffer.getvalue())
    buffer.close()

    return response


def vista_previa_pdf(request, paciente_id):
    historia_clinica = get_object_or_404(HistoriaClinica, paciente_id=paciente_id)
    recetas_medicas = RecetaMedica.objects.filter(paciente_id=paciente_id)
    instrucciones_post = InstruccionesPostConsulta.objects.filter(paciente_id=paciente_id)
    resultados_pruebas = ResultadosPruebas.objects.filter(paciente_id=paciente_id)
    plan_tratamiento = PlanTratamiento.objects.filter(paciente_id=paciente_id)
    factura = Factura.objects.filter(paciente_id=paciente_id)
    clinica = Clinica.objects.first()

    context = {
        'historia_clinica': historia_clinica,
        'recetas_medicas': recetas_medicas,
        'instrucciones_post': instrucciones_post,
        'resultados_pruebas': resultados_pruebas,
        'plan_tratamiento': plan_tratamiento,
        'factura': factura,
        'clinica': clinica,
    }
    return render(request, 'Parciales/vista_previa_pdf.html', context)
