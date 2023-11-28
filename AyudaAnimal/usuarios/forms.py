from django.contrib.auth.forms import UserCreationForm
from .models import Medico
from django.contrib.auth import get_user_model
from citas.models import HorarioVeterinario
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email', 'tipo_usuario')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            if user.tipo_usuario == 'MEDICO':
                Medico.objects.create(usuario=user, nombre=user.username)
        return user
    


class HorarioVeterinarioForm(forms.ModelForm):
    class Meta:
        model = HorarioVeterinario
        fields = ['medico', 'fecha', 'hora_inicio', 'hora_fin']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time'}),
        }

