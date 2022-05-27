from django.db import models

#jugador,equipo,dt 
class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email= models.EmailField()
    sexo = models.CharField(max_length=50)
    edad = models.IntegerField()
    peso = models.IntegerField()
    altura = models.IntegerField()
    pie_habil = models.CharField(max_length=50)
    posicion = models.CharField(max_length=50)
    numero_de_camiseta= models.IntegerField()
    club_equipo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre + self.apellido

class Equipo(models.Model):
    team=models.CharField(max_length=50)
    cantidad_de_jugadores = models.IntegerField()
    torneo_liga_campeonato = models.CharField(max_length=50)
    puesto = models.IntegerField()
    partidos_jugados= models.IntegerField()
    titulos = models.CharField(max_length=50)

    def __str__(self):
        return self.team + self.torneo_liga_campeonato

class DirectorTecnico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email= models.EmailField()
    edad = models.IntegerField()
    dirige = models.CharField(max_length=50)
    titulos = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + self.apellido

