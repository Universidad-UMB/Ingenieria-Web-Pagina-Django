from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import articulo

def articulos(request):
    mis_articulos = articulo.objects.all()
    return render(request,"articulos/articulos.html", {"articulos":mis_articulos} )

def DetalleArticulo(request, id):
    Articulo = get_object_or_404(articulo, id=id)
    return render(request, 'articulos/DetalleArticulo.html' , {'articulo': Articulo})