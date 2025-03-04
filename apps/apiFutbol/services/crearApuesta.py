from ..models import Apuesta

def crearApuesta(nombreLocal, nombreVisitante, ganador, odd, apuesta, premio, finalizada, idFixture, estado):
    
        
    newApuesta= Apuesta(nombreLocal=nombreLocal, nombreVisitante=nombreVisitante, 
                            ganador=ganador, odd=odd, apuesta=apuesta, premio=premio,
                            finalizada=finalizada, idFixture=idFixture, estado=estado)
    newApuesta.save()