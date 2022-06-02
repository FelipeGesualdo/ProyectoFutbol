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

    path('about/', about, name='about'),
    path('pages/', pages, name='pages'),
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name = "AppFutbol/logout.html"), name='logout'),
]