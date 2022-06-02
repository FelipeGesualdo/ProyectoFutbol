from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppFutbol.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

#--------------------VIEWS------------------------------------------
def inicio(request):
    return render(request, "AppFutbol/inicio.html")

def jugador(request):
    if request.method == 'POST':
        formulario= jugForm(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            jugador = Jugador(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], sexo=informacion['sexo'], edad=informacion['edad'], peso=informacion['peso'], altura=informacion['altura'], pie_habil=informacion['pie_habil'], posicion=informacion['posicion'], numero_de_camiseta=informacion['numero_de_camiseta'], club_equipo=informacion['club_equipo'], goles=informacion['goles'])
            jugador.save()
            return render(request, "AppFutbol/inicio.html")
    else:
        formulario= jugForm()
        return render(request, "AppFutbol/jugador.html", {'formulario':formulario})

def equipo(request):
    if request.method == 'POST':
        formulario= equiForm(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            equipo = Equipo(team=informacion['team'], cantidad_de_jugadores=informacion['cantidad_de_jugadores'], torneo_liga_campeonato=informacion['torneo_liga_campeonato'], puesto=informacion['puesto'], partidos_jugados=informacion['partidos_jugados'], titulos=informacion['titulos'], goles_a_favor=informacion['goles_a_favor'], dias_de_partido=informacion['dias_de_partido'])
            equipo.save()
            return render(request, "AppFutbol/inicio.html")
    else:
        formulario= equiForm()
        return render(request, "AppFutbol/equipo.html", {'formulario':formulario})

def directortecnico(request):
    if request.method == 'POST':
        formulario = dirForm(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            directortecnico = DirectorTecnico(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], edad=informacion['edad'], dirige=informacion['dirige'], titulos=informacion['titulos'], dias_disponibles=informacion['dias_disponibles'])
            directortecnico.save()
            return render(request, "AppFutbol/inicio.html")
    else:
        formulario= dirForm()
        return render(request, "AppFutbol/directortecnico.html", {'formulario':formulario})

#----------------------FORMULARIOS-----------------------------------

def jugadorFormulario (request):
    return render(request, "AppFutbol/jugadorFormulario.html")

def equipoFormulario (request):
    return render(request, "AppFutbol/equipoFormulario.html")

def directortecnicoFormulario (request):
    return render(request, "AppFutbol/directortecnicoFormulario.html")

#-------------------MAS DE LA WEB--------------------------------
def about(request):
    return render(request, "AppFutbol/about.html")
#contar sobre mi y el proyecto

def pages(request):
    return render(request, "AppFutbol/pages.html")
#mostrar los blogs creados de la BD por los usuarios


#--------------------LOGIN------------------------------------------
def login_request(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request=request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            clave = formulario.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request, "AppFutbol/inicio.html",{'usuario':usuario, 'mensaje':'Bienvenido/a al sistema!'})
            else:
                return render(request, "AppFutbol/inicio.html",{'mensaje':'Usuario o contraseña son incorrectos!. Por favor, vuelva a loguearse'})
        else:
            return render(request, "AppFutbol/login.html",{'mensaje':'Se produjo un error. Su formulaio es invalido. Por favor, vuelva a loguearse'})
    else:
        formulario=AuthenticationForm()
        return render(request, "AppFutbol/login.html", {'formulario':formulario})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppFutbol/inicio.html",{'mensaje':f'Usuario: {username} creado exitosamente!'})
        else:
            return render(request, "AppFutbol/register.html",{'mensaje':'No se pudo crear el usuario'})
    else:
        form = UserRegistrationForm()
        return render(request, "AppFutbol/register.html", {'form':form})




#-------------------BLOGS-----------------------------
#https://www.yoga-bonito.com/futbolyoga
#https://www.bubblefootball.es/blog/ 
#https://sites.duke.edu/wcwp/        (funcion)












#nombre = request.POST['nombre']
        #apellido = request.POST['apellido']
        #email = request.POST['email']
        #sexo = request.POST['sexo']
        #edad = request.POST['edad']
        #peso = request.POST['peso']
        #altura = request.POST['altura']
        #pie_habil = request.POST['pie_habil']
        #posicion = request.POST['posicion']
        #numero_de_camiseta = request.POST['numero_de_camiseta']
        #club_equipo = request.POST['club_equipo']
        #jugador = Jugador(nombre=nombre, apellido=apellido, email=email, sexo=sexo, edad=edad, peso=peso, altura=altura, pie_habil=pie_habil, posicion=posicion, numero_de_camiseta=numero_de_camiseta, club_equipo=club_equipo)

#def jugador(request):
    #jugador= Jugador(nombre="Felipe", apellido= "Gesualdo", sexo= "Masculino", edad=19,email="feligesu@gmail.com")
    #jugador.save()
    #return HttpResponse(f"Jugador creado: {jugador.nombre}" )