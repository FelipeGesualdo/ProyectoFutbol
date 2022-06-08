from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.forms import User
from AppFutbol.models import Blog, Avatar
class jugForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email= forms.EmailField()
    sexo = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    peso = forms.IntegerField()
    altura = forms.IntegerField()
    pie_habil = forms.CharField(max_length=50)
    posicion = forms.CharField(max_length=50)
    numero_de_camiseta= forms.IntegerField()
    club_equipo = forms.CharField(max_length=50)
    goles = forms.IntegerField()


class equiForm(forms.Form):
    team=forms.CharField(max_length=50)
    cantidad_de_jugadores = forms.IntegerField()
    torneo_liga_campeonato = forms.CharField(max_length=50)
    puesto = forms.IntegerField()
    partidos_jugados= forms.IntegerField()
    titulos = forms.CharField(max_length=50)
    goles_a_favor = forms.IntegerField()
    dias_de_partido = forms.CharField(max_length=50)
    email = email= forms.EmailField()

class dirForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email= forms.EmailField()
    edad = forms.IntegerField()
    dirige = forms.CharField(max_length=50)
    titulos = forms.CharField(max_length=50)
    dias_disponibles = forms.CharField(max_length=50)

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields=('username', 'email', 'password1', 'password2')
        help_texts={k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label="Modificar Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget= forms.PasswordInput)
   

    class Meta:
        model = User
        fields=('username', 'email', 'password1', 'password2')
        help_texts={k:"" for k in fields}



class BlogForm(forms.ModelForm):
    
    class Meta:
        model= Blog
        fields=('imagen', 'titulo', 'subtitulo', 'cuerpo', 'user')

class BlogUpdateForm(forms.ModelForm):
    
    class Meta:
        model= Blog
        fields=('titulo', 'subtitulo', 'cuerpo', 'user')
    
class AvatarForm(forms.ModelForm):
    
    class Meta:
        model= Avatar
        
        fields=('user', 'avatar')




              
        
