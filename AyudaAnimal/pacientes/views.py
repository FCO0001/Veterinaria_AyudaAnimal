from django.shortcuts import render, redirect
from pacientes.forms import MascotaForms


def showView(request):
   if request.method == "POST":
      form = MascotaForms(request.POST)
      if form.is_valid():
         form.save()
      return redirect('Mensaje_registro')
   else:
     form = MascotaForms()
   return render(request, 'agregar_paciente.html', {'form': form})

def showViewEdit(request):
   return render(request, "editar_paciente.html")


# Create your views here.
