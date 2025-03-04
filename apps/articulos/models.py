from django.db import models

class articulo(models.Model):
    titulo = models.CharField(max_length=80)
    fechaPublicacion = models.DateField()
    resumen = models.CharField(max_length=200)
    detalle = models.CharField(max_length=1000)
    foto = models.CharField(max_length=150)
    estadoPublicado= models.BooleanField(default=True)

    def __str__(self):
        return self.titulo  