
from django.urls import path

from App_Familia.views import amigos, cursos, entregables, estudiantes, familia, inicio, lista_amigos, lista_familiar, lista_mascotas, mascotas, profesores

urlpatterns = [
    path('agrega-familiar/<nombre>/<apellido>/<edad>/<altura>/<fecha_de_nacimiento>', familia),
    path('lista-familiar/',lista_familiar),
    path('agrega-amigo/<nombre>/<apellido>/<edad>/<altura>/<fecha_de_nacimiento>', amigos),
    path('lista-amigos/',lista_amigos),
    path('agrega-mascota/<nombre>/<raza>/<edad>/<peso>/<fecha_de_nacimiento>', mascotas),
    path('lista-mascotas/',lista_mascotas),
    path('cursos/',cursos),
    path('estudiantes/',estudiantes),
    path('profesores/',profesores),
    path('', inicio),
    path('entregables/',entregables),

]
