from .views import *
from django.urls import path
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('jugador/', jugador, name='jugador'),
    path('equipo/', equipo, name='equipo'),
    path('directortecnico/', directortecnico, name='directortecnico'),
    path('', inicio, name='inicio'),

    path('buscarJugador/', buscarJugador, name='buscarJugador'),
    path('buscarEquipo/', buscarEquipo, name='buscarEquipo'),
    path('buscarDirectortecnico/', buscarDirectortecnico, name='buscarDirectortecnico'),

    path('leerJugadores/', leerJugadores, name='leerJugadores'),
    path('leerEquipos/', leerEquipos, name='leerEquipos'),
    path('leerDts/', leerDts, name='leerDts'),

    path('editarJugadores/<id>', editarJugadores, name='editarJugadores'),
    path('editarEquipos/<id>', editarEquipos, name='editarEquipos'),
    path('editarDts/<id>', editarDts, name='editarDts'),

    path('eliminarJugador/<id>', eliminarJugador, name='eliminarJugador'),
    path('eliminarEquipo/<id>', eliminarEquipo, name='eliminarEquipo'),
    path('eliminarDT/<id>', eliminarDT, name='eliminarDT'),

    path('leerJugadores/<pk>', JugadorDetalle.as_view(), name='Jugador_detalle'),   
    path('leerEquipos/<pk>', EquipoDetalle.as_view(), name='Equipo_detalle'),  
    path('leerDts/<pk>', DirectorTecnicoDetalle.as_view(), name='DirectorTecnico_detalle'),

    path('about/', about, name='about'),
    path('bienvenido/', bienvenido, name='bienvenido'),
    path('pages/', pages, name='pages'),

    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name = "AppFutbol/logout.html"), name='logout'),
    
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    
    path('blog_confirm_delete/<pk>', BlogDeleteView.as_view(), name='blog_confirm_delete'),
    path('blog_detalle/<pk>', BlogDetalle.as_view(), name='blog_detalle'),
    path('miPerfil/<pk>', PerfilDetalle.as_view(), name='miPerfil'),
    path('blog_edit/<id>', editarBlog, name='blog_edit'),
    path('avatar_create/', AvatarCreateView.as_view(), name='crear_avatar'),
    path('avatar_update/<pk>', AvatarUpdateView.as_view(), name='editar_avatar'),

]