from django import forms
from pacientes.models import Mascota

class MascotaForms(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = [
            'nombre',
            'especie',
            'raza',
            'edad',
            'nombre_dueño', 
            'run_dueño'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'especie': forms.Select(attrs={'class':'form-control'}),
            'raza': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_dueño': forms.TextInput(attrs={'class':'form-control'}),
            'run_dueño': forms.TextInput(attrs={'class':'form-control'})
        }

    