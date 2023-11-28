from django.urls import path
from . import views

urlpatterns = [
    path('CrearUsuarios', views.create_user, name='create_user'),
    path('EliminarUsuarios', views.eliminar_usuario, name='eliminar_usuario'),
    path('horarios/gestionar/<int:horario_id>/', views.gestionar_horarios, name='gestionar_horarios'),
    path('horarios/gestionar/', views.gestionar_horarios, name='crear_horario'),
]





    


