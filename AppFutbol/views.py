from django.shortcuts import redirect, render
from AppFutbol.forms import BlogForm, BlogUpdateForm
from .models import *
from .models import Avatar
from AppFutbol.forms import UserEditForm, jugForm, equiForm, dirForm, UserRegistrationForm, AvatarForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
            equipo = Equipo(team=informacion['team'], cantidad_de_jugadores=informacion['cantidad_de_jugadores'], torneo_liga_campeonato=informacion['torneo_liga_campeonato'], puesto=informacion['puesto'], partidos_jugados=informacion['partidos_jugados'], titulos=informacion['titulos'], goles_a_favor=informacion['goles_a_favor'], dias_de_partido=informacion['dias_de_partido'], email=informacion['email'])
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

#-----------------------------Buscar--------------------------------------------------
@login_required
def buscarJugador(request):
    if request.GET['posicion']:
        posicion=request.GET['posicion']
        jugadores=Jugador.objects.filter(posicion__icontains=posicion)
        return render(request, "AppFutbol/resultadosJugador.html", {'jugadores':jugadores})
    else:
        respuesta="No se ingreso ninguna posicion"
        return render(request, "AppFutbol/resultadosJugador.html", {'respuesta':respuesta})

@login_required
def buscarEquipo(request):
    if request.GET['dias_de_partido']:
        dias_de_partido=request.GET['dias_de_partido']
        equipos=Equipo.objects.filter(dias_de_partido__icontains=dias_de_partido)
        return render(request, "AppFutbol/resultadosEquipo.html", {'equipos':equipos})
    else:
        respuesta="No se ingreso ningun dia"
        return render(request, "AppFutbol/resultadosEquipo.html", {'respuesta':respuesta})    

@login_required
def buscarDirectortecnico(request):
    if request.GET['dias_disponibles']:
        dias_disponibles=request.GET['dias_disponibles']
        dts=DirectorTecnico.objects.filter(dias_disponibles__icontains=dias_disponibles)
        return render(request, "AppFutbol/resultadosDirectortecnico.html", {'dts':dts})
    else:
        respuesta="No se ingreso ningun dia"
        return render(request, "AppFutbol/resultadosDirectortecnico.html", {'respuesta':respuesta})

#--------------------------------------LEER------------------------------------------------

@login_required
def leerJugadores(request):
    jugadores=Jugador.objects.all()
    contexto={'jugadores':jugadores}
    return render(request, "AppFutbol/leerJugadores.html", contexto)

@login_required
def leerEquipos(request):
    equipos=Equipo.objects.all()
    contexto={'equipos':equipos}
    return render(request, "AppFutbol/leerEquipos.html", contexto)

@login_required
def leerDts(request):
    Dts=DirectorTecnico.objects.all()
    contexto={'Dts':Dts}
    return render(request, "AppFutbol/leerDts.html", contexto)

#--------------------------------ELIMINAR---------------------------------------

@login_required
def eliminarJugador(request, id):
    jugador=Jugador.objects.get(id=id)
    jugador.delete()
    jugadores=Jugador.objects.all()
    contexto={'jugadores':jugadores}
    return render(request, "AppFutbol/leerJugadores.html", contexto)

@login_required
def eliminarEquipo(request, id):
    equipo=Equipo.objects.get(id=id)
    equipo.delete()
    equipos=Equipo.objects.all()
    contexto={'equipos':equipos}
    return render(request, "AppFutbol/leerEquipos.html", contexto)

@login_required
def eliminarDT(request, id):
    dt=DirectorTecnico.objects.get(id=id)
    dt.delete()
    Dts=DirectorTecnico.objects.all()
    contexto={'Dts':Dts}
    return render(request, "AppFutbol/leerDts.html", contexto)

#--------------------------EDITAR----------------------------- 

@login_required
def editarJugadores(request,id):
    jugador=Jugador.objects.get(id=id)
    if request.method == 'POST':
        miFormulario=jugForm(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            jugador.nombre=informacion['nombre']
            jugador.apellido=informacion['apellido']
            jugador.email=informacion['email']
            jugador.sexo=informacion['sexo']
            jugador.edad=informacion['edad']
            jugador.peso=informacion['peso']
            jugador.altura=informacion['altura']
            jugador.pie_habil=informacion['pie_habil']
            jugador.posicion=informacion['posicion']
            jugador.numero_de_camiseta=informacion['numero_de_camiseta']
            jugador.club_equipo=informacion['club_equipo']
            jugador.goles=informacion['goles']
            jugador.save()
            jugadores=Jugador.objects.all()
            contexto={'jugadores':jugadores}
            return render(request, "AppFutbol/leerJugadores.html", contexto)
    else:
        miFormulario=jugForm(initial={'nombre':jugador.nombre, 'apellido':jugador.apellido, 'email':jugador.email,'sexo':jugador.sexo, 'edad':jugador.edad, 'peso':jugador.peso,'altura':jugador.altura, 'pie_habil':jugador.pie_habil, 'posicion':jugador.posicion, 'numero_de_camiseta':jugador.numero_de_camiseta, 'club_equipo':jugador.club_equipo, 'goles':jugador.goles })
    return render(request, "AppFutbol/editarJugadores.html", {'miFormulario':miFormulario, 'id':id})

@login_required
def editarEquipos(request,id):
    equipo=Equipo.objects.get(id=id)
    if request.method == 'POST':
        miFormulario=equiForm(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            equipo.team=informacion['team']
            equipo.cantidad_de_jugadores=informacion['cantidad_de_jugadores']
            equipo.torneo_liga_campeonato=informacion['torneo_liga_campeonato']
            equipo.puesto=informacion['puesto']
            equipo.partidos_jugados=informacion['partidos_jugados']
            equipo.titulos=informacion['titulos']
            equipo.goles_a_favor=informacion['goles_a_favor']
            equipo.dias_de_partido=informacion['dias_de_partido']
            equipo.save()
            equipos=Equipo.objects.all()
            contexto={'equipos':equipos}
            return render(request, "AppFutbol/leerEquipos.html", contexto)
    else:
        miFormulario=equiForm(initial={'team':equipo.team, 'cantidad_de_jugadores':equipo.cantidad_de_jugadores, 'torneo_liga_campeonato':equipo.torneo_liga_campeonato,'puesto':equipo.puesto, 'partidos_jugados':equipo.partidos_jugados, 'titulos':equipo.titulos, 'goles_a_favor':equipo.goles_a_favor, 'dias_de_partido':equipo.dias_de_partido })
    return render(request, "AppFutbol/editarEquipos.html", {'miFormulario':miFormulario, 'id':id})

@login_required
def editarDts(request,id):
    dt=DirectorTecnico.objects.get(id=id)
    if request.method == 'POST':
        miFormulario=dirForm(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            dt.nombre=informacion['nombre']
            dt.apellido=informacion['apellido']
            dt.email=informacion['email']
            dt.edad=informacion['edad']
            dt.dirige=informacion['dirige']
            dt.titulos=informacion['titulos']
            dt.dias_disponibles=informacion['dias_disponibles']
            dt.save()
            Dts=DirectorTecnico.objects.all()
            contexto={'Dts':Dts}
            return render(request, "AppFutbol/leerDts.html", contexto)
    else:
        miFormulario=dirForm(initial={'nombre':dt.nombre, 'apellido':dt.apellido, 'email':dt.email,'edad':dt.edad, 'dirige':dt.dirige, 'titulos':dt.titulos, 'dias_disponibles':dt.dias_disponibles })
    return render(request, "AppFutbol/editarDts.html", {'miFormulario':miFormulario, 'id':id}) 

#-----------------------------Views---------------------------------------------

class JugadorDetalle(LoginRequiredMixin, DetailView):
    model = Jugador
    template_name = "AppFutbol/Jugador_detalle.html"

class JugadorEliminacion(DeleteView):
    model = Jugador
    success_url= reverse_lazy('jugador_borrar')
    fields= ['nombre','apellido', 'email', 'sexo', 'edad', 'peso', 'altura', 'pie_habil', 'posicion', 'numero_de_camiseta', 'club_equipo', 'goles']

class EquipoDetalle(LoginRequiredMixin, DetailView):
    model = Equipo
    template_name = "AppFutbol/Equipo_detalle.html"

class EquipoEliminacion(DeleteView):
    model = Jugador
    success_url= reverse_lazy('equipo_borrar')
    fields=['team', 'cantidad_de_jugadores','torneo_liga_campeonato', 'puesto', 'partidos_jugados', 'titulos', 'goles_a_favor', 'dias_de_partido' ]

class DirectorTecnicoDetalle(LoginRequiredMixin, DetailView):
    model = DirectorTecnico
    template_name = "AppFutbol/DirectorTecnico_detalle.html"

class DirectorTecnicoEliminacion(DeleteView):
    model = DirectorTecnico
    success_url= reverse_lazy('dt_borrar')
    fields= ['nombre','apellido', 'email', 'edad', 'dirige', 'titulos', 'dias_disponibles']

#-------------------MAS DE LA WEB--------------------------------
def about(request):
    return render(request, "AppFutbol/about.html")

def pages(request):
    avatar=Avatar.objects.filter(user=request.user)
    return render(request, "AppFutbol/pages.html", {'blogs': avatar})

def bienvenido(request):
    return render(request, "AppFutbol/bienvenido.html")

#-----------------------------PERFIL-----------------------------------

@login_required
def editarPerfil(request):
    usuario=request.user
    user=User.objects.get(pk=request.user.id)       
    if request.method == 'POST':
        miFormulario= UserEditForm(request.POST, instance=usuario)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()
            
            return render(request, "AppFutbol/inicio.html", {'usuario':usuario, 'mensaje':'Perfil editado exitosamente'})
    else:
        miFormulario= UserEditForm(instance=usuario)
    return render(request, "AppFutbol/editarPerfil.html", {'miFormulario':miFormulario, 'usuario':usuario.username})

class PerfilDetalle(LoginRequiredMixin, DetailView):
    model = User
    template_name = "AppFutbol/miPerfil.html"
    
    def get_context_data(self, **kwargs):
        context = super(PerfilDetalle, self).get_context_data(**kwargs)
        user=User.objects.get(pk=self.request.user.id)
        try:
            context['avatar'] = Avatar.objects.get(user=user)
        except Avatar.DoesNotExist :
            pass
        return context

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
                return render(request, "AppFutbol/bienvenido.html",{'usuario':usuario, 'mensaje':'Bienvenido/a al sistema!'})
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

#----------------------blog---------------------------

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "AppFutbol/Blog_create.html"
    form_class= BlogForm
    success_url=reverse_lazy("inicio")

class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "AppFutbol/blog_list.html"

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "AppFutbol/blog_confirm_delete.html"
    success_url=reverse_lazy("inicio")

class BlogDetalle(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "AppFutbol/blog_detalle.html"

@login_required
def eliminarBlog(request, id):
    blog=Blog.objects.get(id=id)
    blog.delete()
    blogs=Blog.objects.all()
    contexto={'blogs':blogs}
    return render(request, "AppFutbol/blog_list.html", contexto)

@login_required
def editarBlog(request,id):
    blog=Blog.objects.get(id=id)
    if request.method == 'POST':
        miFormulario=BlogUpdateForm(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            blog.titulo=informacion['titulo']
            blog.subtitulo=informacion['subtitulo']
            blog.user=informacion['user']
            
            blog.cuerpo=informacion['cuerpo']
            
            blog.save()
            blogs=Blog.objects.all()
            contexto={'blogs':blogs}
            return redirect('blog_list')
    else:
        miFormulario=BlogUpdateForm(initial={'titulo':blog.titulo, 'subtitulo':blog.subtitulo, 'cuerpo':blog.cuerpo, 'user':blog.user })
    return render(request, "AppFutbol/blog_edit.html", {'miFormulario':miFormulario, 'id':id})
        
#-----------------------------AVATAR--------------------------------

@login_required
def agregarAvatar(request):
    user=User.objects.get(username=request.user)
    avatar=Avatar.object.filter(user=user)
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.get(user=request.user)
            if(avatarViejo.avatar):
                avatarViejo.delete()
            avatar=Avatar(user=user, avatar=formulario.cleaned_data['avatar'])
            avatar.save()
            return render(request, 'AppFutbol/inicio.html', {'usuario':user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE'})
    else:
        formulario=AvatarForm()
    return render(request, 'AppFutbol/editarPerfil.html', {'formulario':formulario, 'usuario':user, 'avatar':avatar})

class AvatarCreateView(CreateView):
    model = Avatar
    form_class = AvatarForm
    template_name = "AppFutbol/agregarAvatar.html"
    success_url=reverse_lazy("inicio")

class AvatarUpdateView(UpdateView):
    model = Avatar
    form_class = AvatarForm
    template_name = "AppFutbol/agregarAvatar.html"
    success_url=reverse_lazy("inicio")


