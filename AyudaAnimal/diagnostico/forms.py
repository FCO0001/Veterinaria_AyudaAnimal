from django import forms
from .models import HistoriaClinica, InstruccionesPostConsulta, ResultadosPruebas, PlanTratamiento, Factura,RecetaMedica,Diagnostico


class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['paciente', 'sintomas', 'diagnostico_medico']
        widgets = {
            'sintomas': forms.Textarea(attrs={'rows': 4}),
            'diagnostico_medico': forms.Textarea(attrs={'rows': 4})
        }



class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = ['paciente', 'hallazgos_examen', 'recomendaciones']
        widgets = {
            'hallazgos_examen': forms.Textarea(attrs={'rows': 3}),
            'recomendaciones': forms.Textarea(attrs={'rows': 3}),
        }


class RecetaMedicaForm(forms.ModelForm):
    class Meta:
        model = RecetaMedica
        fields = ['paciente', 'medicamento', 'dosificacion', 'frecuencia', 'duracion']
        widgets = {
            'medicamento': forms.TextInput(attrs={'class': 'form-control'}),
            'dosificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'frecuencia': forms.TextInput(attrs={'class': 'form-control'}),
            'duracion': forms.TextInput(attrs={'class': 'form-control'}),
        }


class InstruccionesPostConsultaForm(forms.ModelForm):
    class Meta:
        model = InstruccionesPostConsulta
        fields = ['paciente', 'instrucciones']
        widgets = {
            'instrucciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class ResultadosPruebasForm(forms.ModelForm):
    class Meta:
        model = ResultadosPruebas
        fields = ['paciente', 'descripcion_pruebas', 'resultados']
        widgets = {
            'descripcion_pruebas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'resultados': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class PlanTratamientoForm(forms.ModelForm):
    class Meta:
        model = PlanTratamiento
        fields = ['paciente', 'descripcion', 'citas_seguimiento', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'citas_seguimiento': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['paciente', 'detalles', 'total']
        widgets = {
            'detalles': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
        }

