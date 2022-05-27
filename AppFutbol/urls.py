from .views import *
from django.urls import path




urlpatterns = [
    path('jugador/', jugador),
    path('equipo/', equipo),
    path('directortecnico/', directortecnico),
    path('', inicio),
]