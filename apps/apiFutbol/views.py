from django.shortcuts import render, redirect
from .services.apiFutbol import getPartidos, getOdds, partidosOdds
from .models import Apuesta
from django.http import  JsonResponse
from .services.crearApuesta import crearApuesta

def partidos(request):
    
   responseDataPartidos = getPartidos()
   oddLocal, oddVisitante=  getOdds()
   partidosOdd= partidosOdds(responseDataPartidos, oddLocal, oddVisitante)
   #return render(
        #request, 
        #"apiFutbol/partidosPrueba.html", 
        #{
            #'responseDataPartidos': responseDataPartidos, 
            #'oddLocal': oddLocal, 
            #'oddVisitante': oddVisitante
        #}
    #)
     
   if not responseDataPartidos:  # Si hubo un error en la API
        return render(request, "apiFutbol/partidos.html", {'error': "Error al obtener datos"})
   return render(request, "apiFutbol/partidos.html", 
                { 'responseDataPartidos': responseDataPartidos, 
                'partidosOdd': partidosOdd})

def registrarApuesta(request):
    
    if request.method == "POST":
        try:
            nombreLocal = request.POST['nombreLocal']
            nombreVisitante = request.POST['nombreVisitante']
            ganador = request.POST['nombreGanador']
            odd = float(request.POST['odd'])
            apuesta = int(request.POST['cantidadApostar'])
            premio = int(odd*apuesta)
            finalizada = False
            idFixture = int(request.POST['idPartido'])
            estado="En Juego"
            crearApuesta(nombreLocal, nombreVisitante, ganador, odd, apuesta, premio, finalizada, idFixture, estado)
            return redirect("apps_apiFutbol:partidos")
        
        except ValueError:
            return JsonResponse({"error": "Dato inválido"}, status=400)
        
    return JsonResponse({"error": "Método no permitido"}, status=405)
    
        
def traerApuestas(request):
    listaApuestas = Apuesta.objects.all()
    return render(request, 'apiFutbol/historial.html', {'listaApuestas': listaApuestas} )