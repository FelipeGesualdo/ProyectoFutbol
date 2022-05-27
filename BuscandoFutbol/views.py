from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Hola Mundo!")

def dia_de_hoy(request):
    dia=datetime.now()
    frase=f"hoy es:{dia}"
    return HttpResponse(frase)

def saludo_persona(request,nombre):
    return HttpResponse (f"Hola {nombre}")

def probando_template(request):

    lista_de_nombres=["Juan","Pedro","Ana","Maria","Luis","Micaela"]
    diccionario={"lista":lista_de_nombres}
    
    plantilla=loader.get_template("inicio.html")
    
    documento= plantilla.render(diccionario)
    return HttpResponse(documento)