from django.urls import path
from . import views

urlpatterns = [
    path('Mensaje_registro/', views.vista_formulario_cita, name='Mensaje_registro'),
]
