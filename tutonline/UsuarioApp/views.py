from django.shortcuts import render, redirect, get_object_or_404
from api.models import *
from datetime import date
from .forms import *
# Create your views here.

def calcular_anios_pasados(anio):
    anio_actual = date.today().year
    anios_pasados = anio_actual - anio.year
    return anios_pasados

def Perfil(request):
    def ObtenerProfesion(request):
        user_id = request.user.id
        profesion = Profesion.objects.filter(idProfesor_id=user_id)
        dataProfesion = {'profesion':profesion}
        return dataProfesion
    def ObtenerAnios(request):
        profesion = Profesion.objects.filter(idProfesor=request.user.id).first()
        anio_egreso = profesion.anioEgreso if profesion else None
        anios_pasados = calcular_anios_pasados(anio_egreso) if anio_egreso else None
        return {'anios_pasados':anios_pasados}
    def ObtenerDescripcion(request):
        user_id = request.user.id
        descripcion = Descripcion.objects.filter(idProfesor_id=user_id)
        dataDescripcion = {'descripcion':descripcion}
        return dataDescripcion
    def ObtenerClases(request):
        user_id = request.user.id
        clases = Clase.objects.filter(idProfesor_id=user_id)
        dataClase = {'clases':clases}
        return dataClase
    def ObtenerPublicaciones(request):
        user_id = request.user.id
        publicaciones = Publicacion.objects.filter(idEstudiante_id=user_id)
        dataPublicacion = {'publicaciones':publicaciones}
        return dataPublicacion
    context = {
        **ObtenerProfesion(request),
        **ObtenerAnios(request),
        **ObtenerDescripcion(request),
        **ObtenerClases(request),
        **ObtenerPublicaciones(request)
    }
    return render(request,'Perfiles/Perfil.html',context)    

def PerfilTutor(request, username=None):
    def IdentificarUser(request, username=None): 
        current_user = request.user
        if username and username != current_user.username:
            user = User.objects.get(username=username)
            profesion = user.profesion.all()
            print(profesion)
            descripcion = user.descripcion.all()
            print (descripcion)
            clase = user.clase.all()
            dataUser = {'user':user, 'profesion':profesion, 'descripcion':descripcion, 'clase':clase}
            return dataUser
        else:
            user = current_user
            profesion = user.profesion.all()
            print(profesion)
            descripcion = user.descripcion.all()
            print (descripcion)
            clase = user.clase.all()
            dataUser = {'user':user, 'profesion':profesion, 'descripcion':descripcion, 'clase':clase}
            return dataUser
            
    context = {
        **IdentificarUser(request, username=username),        
    }
    return render(request, 'Perfiles/PerfilTutor.html', context)

def PerfilEstudiante(request, username=None):
    def IdentificarUser(request, username=None): 
        current_user = request.user
        if username and username != current_user.username:
            user = User.objects.get(username=username)
            publicacion = user.publicacion.all()
            print(publicacion)
            dataUser = {'user':user, 'publicacion':publicacion}
            return dataUser
        else:
            user = current_user
            publicacion = user.publicacion.all()
            print(publicacion)
            dataUser = {'user':user, 'publicacion':publicacion}
            return dataUser
    context = {
        **IdentificarUser(request, username=username),        
    }
    return render(request, 'Perfiles/PerfilEstudiante.html', context)