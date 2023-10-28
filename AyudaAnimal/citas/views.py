from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import formulario_cita_medico
from django.contrib import messages


def vista_formulario_cita(request):
    if request.method == "POST":
        form = formulario_cita_medico(request.POST)
        if form.is_valid():
            cita = form.save()
            messages.success(request, f"Cita agendada con éxito: {cita.Paciente} con {cita.medico} el {cita.dia} de {cita.get_horario_display()}")
            return redirect('Mensaje_registro')

    else:
        form = formulario_cita_medico()
    return render(request, 'Mensaje_registro.html', {'form': form})




# Create your views here.
