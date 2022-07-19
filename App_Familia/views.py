from django.http import HttpResponse
from django.shortcuts import render

from App_Familia.models import Amigos, Familia, Mascotas

# Create your views here.


def familia(self, nombre, apellido, edad, altura, fecha_de_nacimiento):

    familia = Familia(nombre = nombre, apellido = apellido, edad = edad, altura = altura, fecha_de_nacimiento = fecha_de_nacimiento)
    familia.save()

    return render(self, "agregado.html", {'familia': familia})



def lista_familiar(self):

    lista = Familia.objects.all()

    return render(self, "lista_familiar.html", {'lista_familiar': lista})



def amigos(self, nombre, apellido, edad, altura, fecha_de_nacimiento):

    amigos = Amigos(nombre = nombre, apellido = apellido, edad = edad, altura = altura, fecha_de_nacimiento = fecha_de_nacimiento)
    amigos.save()

    return render(self, "amigo_agregado.html", {'amigos': amigos})

def lista_amigos(self):

    lista = Amigos.objects.all()

    return render(self, "lista_amigos.html", {'lista_amigos': lista})

def mascotas(self, nombre, raza, edad, peso, fecha_de_nacimiento):

    mascotas = Mascotas(nombre = nombre, raza = raza, edad = edad, peso = peso, fecha_de_nacimiento = fecha_de_nacimiento)
    mascotas.save()

    return render(self, "mascota_agregada.html", {'mascotas': mascotas})

def lista_mascotas(self):

    lista = Mascotas.objects.all()

    return render(self, "lista_mascotas.html", {'lista_mascotas': lista})



def inicio(self):

    return render(self, "inicio.html")

def estudiantes(self):

    return render(self, "estudiantes.html")
    #return HttpResponse("Vista de estudiantes")

def profesores(self):

    return render(self, "profesores.html")

def cursos(self):

    return render(self, "cursos.html")

def entregables(self):

    return render(self, "entregables.html")




