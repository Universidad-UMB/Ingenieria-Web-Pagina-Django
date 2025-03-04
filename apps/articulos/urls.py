from django.urls import path
from . import views

app_name ="apps_articulos"

urlpatterns=[
    path("noticias", views.articulos, name="articulos"),
    path('detalle/<int:id>/', views.DetalleArticulo, name="DetalleArticulo")
]