from .views import *
from django.urls import path
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path('jugador/', jugador, name='jugador'),
    path('equipo/', equipo, name='equipo'),
    path('directortecnico/', directortecnico, name='directortecnico'),
    path('', inicio, name='inicio'),

    path('jugadorFormulario/', jugadorFormulario, name='jugadorFormulario'),
    path('equipoFormulario/', equipoFormulario, name='equipoFormulario'),
    path('directortecnicoFormulario/', directortecnicoFormulario, name='directortecnicoFormulario'),

    path('buscarJugador/', buscarJugador, name='buscarJugador'),
    path('buscarEquipo/', buscarEquipo, name='buscarEquipo'),
    path('buscarDirectortecnico/', buscarDirectortecnico, name='buscarDirectortecnico'),

    path('leerJugadores/', leerJugadores, name='leerJugadores'),
    path('leerEquipos/', leerEquipos, name='leerEquipos'),
    path('leerDts/', leerDts, name='leerDts'),

    path('eliminarJugador/<id>', eliminarJugador, name='eliminarJugador'),
    path('eliminarEquipo/<id>', eliminarEquipo, name='eliminarEquipo'),
    path('eliminarDT/<id>', eliminarDT, name='eliminarDT'),


    path('about/', about, name='about'),
    path('bienvenido/', bienvenido, name='bienvenido'),
    path('pages/', pages, name='pages'),
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name = "AppFutbol/logout.html"), name='logout'),
]