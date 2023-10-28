from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Cita_con_medico
from .forms import formulario_cita_medico

def vista_formulario_cita(request):
    if request.method == "POST":
        form = formulario_cita_medico(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Confirmacion')
    else:
        form = formulario_cita_medico()
    return render(request, 'Mensaje_registro.html', {'form': form})

def confirmacion_cita(request):
    return render(request, 'Confirmacion.html')

# Create your views here.
