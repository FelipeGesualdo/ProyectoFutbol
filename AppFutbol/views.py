from django.shortcuts import render
from django.http import HttpResponse
from .models import *
#from AppFutbol.forms import *

def inicio(request):
    return render(request, "AppFutbol/inicio.html")

def jugador(request):
    return render(request, "AppFutbol/jugador.html")

def equipo(request):
    return render(request, "AppFutbol/equipo.html")

def directortecnico(request):
    return render(request, "AppFutbol/directortecnico.html")




















#def jugador(request):
    #jugador= Jugador(nombre="Felipe", apellido= "Gesualdo", sexo= "Masculino", edad=19,email="feligesu@gmail.com")
    #jugador.save()
    #return HttpResponse(f"Jugador creado: {jugador.nombre}" )