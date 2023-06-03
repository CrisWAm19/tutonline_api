from django.shortcuts import render, redirect
from api.models import *
from datetime import date
from .forms import *
from django.contrib import messages
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
    return render(request,'Perfiles/PerfilTutor.html',context)    


# ESTUDIANTE
def PublicacionEstudiante(request):
    data = {'form': FormPublicacion(initial={'idEstudiante': request.user.id})}
    if request.method == 'POST':
        form = FormPublicacion(data=request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.idEstudiante_id = request.user.id
            form.save()
            messages.success(request, "Publicacion registrada")
            return redirect(Perfil)
        else: 
            data["form"] = form
    return render (request, 'PublicacionTemplates/Publicacion.html',data)