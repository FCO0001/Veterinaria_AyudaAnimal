from django.urls import path
from . import views

urlpatterns = [
    path('agregar', views.showView, name='pacientes'),
    path('editar', views.showViewEdit, name='editar'),
]

