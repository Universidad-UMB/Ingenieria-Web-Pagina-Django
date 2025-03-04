import requests
from django.utils.dateparse import parse_datetime
from itertools import cycle

dataGloabal=""

def getPartidos():
    url="https://v3.football.api-sports.io/fixtures?date=2025-03-04&timezone=America/Bogota"
    headers= {
        "x-rapidapi-key" : "6cdba232beafff9b6ba90f32cda449c6",
        "x-rapidapi-host": "v3.football.api-sports.io"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        jsonData=response.json()
        data = jsonData.get("response", [])
        
        for partido in data:
            if "fixture" in partido and "date" in partido["fixture"]:
                partido["fixture"]["date"]=parse_datetime(partido["fixture"]["date"])
        
        return data
    except requests.exceptions.RequestException as e:
         print(f"Error en la API: {e}")  # Muestra el error en la consola
         return None
     
def getOdds():
    oddLocal = [2.49, 1.28, 2.1, 1.3, 3.1, 1.89, 2.9, 3.5, 1.4, 2.35]
    oddVisitante = [ 1.9, 2.48, 3.3, 1.2, 1.64, 2.33, 2.19, 2.74, 1.42, 3.42]
    
    
    return  oddLocal, oddVisitante
                        
   
   
def partidosOdds(responseDataPartido, oddLocal, oddVisitante):
    partidosOdd = list(zip(responseDataPartido, cycle(oddLocal), cycle(oddVisitante)))
    return partidosOdd       
       