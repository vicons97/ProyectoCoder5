"""ProyectoFamilia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from App_Familia.views import amigos, familia, lista_amigos, lista_familiar, lista_mascotas, mascotas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agrega-familiar/<nombre>/<apellido>/<edad>/<altura>/<fecha_de_nacimiento>', familia),
    path('lista-familiar/',lista_familiar),
    path('agrega-amigo/<nombre>/<apellido>/<edad>/<altura>/<fecha_de_nacimiento>', amigos),
    path('lista-amigos/',lista_amigos),
    path('agrega-mascota/<nombre>/<raza>/<edad>/<peso>/<fecha_de_nacimiento>', mascotas),
    path('lista-mascotas/',lista_mascotas),
]
