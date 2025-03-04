from django.urls import path
from . import views

app_name= 'apps_fotos'

urlpatterns = [
    path('album-evangelion/', views.album, name='album')
]