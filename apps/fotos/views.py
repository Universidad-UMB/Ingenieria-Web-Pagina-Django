from django.shortcuts import render

from .models import Mifoto

def album(request):
    fotos = Mifoto.objects.all()
    return render(request, "fotos/index.html", {"fotos":fotos})
