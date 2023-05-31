from django.shortcuts import render
from api.models import *
from datetime import date
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


    context = {
        **ObtenerProfesion(request),
        **ObtenerAnios(request),
        **ObtenerDescripcion(request)
    }
    return render(request,'Perfiles/PerfilTutor.html',context)