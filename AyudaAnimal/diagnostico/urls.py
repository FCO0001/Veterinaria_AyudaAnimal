from django.urls import path
from .utils import obtener_prediagnostico
from .views import (vista_prediagnostico, crear_receta_medica, crear_instrucciones_post_consulta, 
                    crear_resultados_pruebas, crear_plan_tratamiento, crear_factura, crear_historia_clinica)

urlpatterns = [
    path('obtener_prediagnostico/', obtener_prediagnostico, name='obtener_prediagnostico'),
    path('prediagnostico/', vista_prediagnostico, name='prediagnostico'),
    path('receta_medica/<int:diagnostico_id>/', crear_receta_medica, name='crear_receta_medica'),
    path('instrucciones_post_consulta/<int:diagnostico_id>/', crear_instrucciones_post_consulta, name='crear_instrucciones_post_consulta'),
    path('resultados_pruebas/<int:diagnostico_id>/', crear_resultados_pruebas, name='crear_resultados_pruebas'),
    path('plan_tratamiento/<int:diagnostico_id>/', crear_plan_tratamiento, name='crear_plan_tratamiento'),
    path('factura/<int:diagnostico_id>/', crear_factura, name='crear_factura'),
    path('historia_clinica/<int:diagnostico_id>/', crear_historia_clinica, name='crear_historia_clinica'),
    # ... otras URLs ...
]
