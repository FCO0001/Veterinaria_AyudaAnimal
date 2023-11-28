from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate
from .models import diferentesUser
from collections import defaultdict
from django.shortcuts import render, redirect, get_object_or_404
from .forms import HorarioVeterinarioForm
from citas.models import HorarioVeterinario


@login_required
@user_passes_test(lambda u: u.is_superuser)
def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado con éxito')
            return redirect('create_user')  # Actualiza con tu URL de redirección
        else:
            messages.error(request, 'Error al crear el usuario')
    else:
        form = CustomUserCreationForm()

    return render(request, 'Parciales/CrearUsuario.html', {'form': form})

# Create your views here.
@login_required
@user_passes_test(lambda u: u.is_superuser)
def eliminar_usuario(request):
    if request.method == 'POST':
        # Verificación de la contraseña del administrador
        password = request.POST.get('password')
        admin = authenticate(username=request.user.username, password=password)
        if admin:
            # Eliminación del usuario
            usuario_id = request.POST.get('usuario_id')
            diferentesUser.objects.filter(id=usuario_id).delete()
            messages.success(request, 'Usuario eliminado correctamente.')
            return redirect('eliminar_usuario')
        else:
            messages.error(request, 'Contraseña incorrecta.')

    # Lista de todos los usuarios
    usuarios_por_tipo = defaultdict(list)
    for usuario in diferentesUser.objects.all():
        usuarios_por_tipo[usuario.tipo_usuario].append(usuario)

    return render(request, 'Parciales/eliminar_usuario.html', {'usuarios_por_tipo': usuarios_por_tipo})



@login_required
@user_passes_test(lambda u: u.is_superuser)
def gestionar_horarios(request, horario_id=None):
    if horario_id:
        horario = get_object_or_404(HorarioVeterinario, pk=horario_id)
    else:
        horario = None

    if request.method == 'POST':
        form = HorarioVeterinarioForm(request.POST, instance=horario)
        if form.is_valid():
            form.save()
            return redirect('gestion_horario_medico')
    else:
        form = HorarioVeterinarioForm(instance=horario)

    return render(request, 'Parciales/gestion_horario_medico.html', {'form': form})



 

