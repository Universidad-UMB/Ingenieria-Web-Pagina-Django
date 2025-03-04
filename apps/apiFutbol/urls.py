from django.urls import path
from . import views

app_name= "apps_apiFutbol"

urlpatterns = [ 
        path("partidos", views.partidos , name="partidos"),
        path("registrar-apuesta", views.registrarApuesta, name="registrar_apuesta"),
        path("historial", views.traerApuestas, name="traerApuestas")
]