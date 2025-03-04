from django.db import models

class Apuesta(models.Model):
    nombreLocal = models.CharField(max_length=60)
    nombreVisitante = models.CharField(max_length=60)
    ganador = models.CharField(max_length=60)
    odd = models.FloatField()
    apuesta = models.IntegerField()
    premio = models.IntegerField()
    finalizada = models.BooleanField(default=False)
    idFixture = models.IntegerField()
    estado = models.CharField(max_length=25)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.ganador