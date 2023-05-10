from django import http
from django.views import View
from .models import *
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

class ProfesorView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, rutProf=''):
        if (rutProf):
            profesores = list(Profesor.objects.filter(rutProf=rutProf).values())
            if len(profesores)>0:
                profesor = profesores[0]
                datos = {'message': "Success", 'profesor': profesor}
            else:
                datos = {'message': "Profesor no encontrado"}
            return JsonResponse(datos)
        else:
            profesores = list(Profesor.objects.values())
            if len(profesores)>0:
                datos = {'message': "Success", 'profesores': profesores}
            else:
                datos = {'message': "No se encontraron profesores"}
            return JsonResponse(datos)

    def post(self, request):
        #convertimos el formato de json a un diccionario de python
        jd = json.loads(request.body)
        Profesor.objects.create(
            rutProf = jd['rutProf'],
            nombreProf = jd['nombreProf'],
            apellidoPaternoProf = jd['apellidoPaternoProf'],
            apellidoMaternoProf = jd['apellidoMaternoProf'],
            fechaNacimiento = jd['fechaNacimiento'],
            correoProf = jd ['correoProf'],
            contrasenaProf = jd ['contrasenaProf'],
            numeroTelefonoProf = jd['numeroTelefonoProf'],
            regionProf = jd['regionProf'],
            comunaProf = jd['comunaProf'],
            fotoPerfil = jd['fotoPerfil']
            )
        datos = {'message': "Success"}
        return JsonResponse(datos)
        
    def put(self, request, rutProf=''):
        jd = json.loads(request.body)
        profesores = list(Profesor.objects.filter(rutProf=rutProf).values())
        if len(profesores)>0:
            #dif entre filter y get. filter: al no encontrar, no devuelve error. get es lo opuesto
            profesor = Profesor.objects.get(rutProf=rutProf)
            profesor.rutProf = jd['rutProf']
            profesor.nombreProf = jd['nombreProf'] 
            profesor.apellidoPaternoProf = jd['apellidoPaternoProf']
            profesor.apellidoMaternoProf = jd['apellidoMaternoProf']
            profesor.fechaNacimiento = jd['fechaNacimiento']
            profesor.correoProf = jd['correoProf']
            profesor.contrasenaProf = jd['contrasenaProf']
            profesor.numeroTelefonoProf = jd['numeroTelefonoProf']
            profesor.regionProf = jd['regionProf']
            profesor.comunaProf = jd['comunaProf']
            profesor.fotoPerfil = jd['fotoPerfil']
            profesor.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Profesor no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, rutProf=''):
        profesores = list(Profesor.objects.filter(rutProf=rutProf).values())
        if len(profesores)>0:
            Profesor.objects.filter(rutProf=rutProf).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Profesor no encontrado"}
        return JsonResponse(datos)

class EstudianteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, rutEst=''):

        if (rutEst):
            estudiantes = list(Estudiante.objects.filter(rutEst=rutEst).values())
            if len(estudiantes)>0:
                estudiante = estudiantes[0]
                datos = {'message': "Success", 'estudiante': estudiante}
            else:
                datos = {'message': "Estudiante no encontrado"}
            return JsonResponse(datos)
        else:
            estudiantes = list(Estudiante.objects.values())
            if len(estudiantes)>0:
                datos = {'message': "Success", 'estudiantes': estudiantes}
            else:
                datos = {'message': "No se encontraron estudiantes"}
            return JsonResponse(datos)
        
    def post(self, request):
            #convertimos el formato de json a un diccionario de python
            jd = json.loads(request.body)
            Estudiante.objects.create(
                rutEst = jd['rutEst'],
                nombreEst = jd['nombreEst'],
                apellidoPaternoEst = jd['apellidoPaternoEst'],
                apellidoMaternoEst = jd['apellidoMaternoEst'],
                fechaNacimiento = jd['fechaNacimiento'],
                correoEst = jd ['correoEst'],
                contrasenaEst = jd ['contrasenaEst'],
                numeroTelefonoEst = jd['numeroTelefonoEst'],
                regionEst = jd['regionEst'],
                comunaEst = jd['comunaEst'],
                fotoPerfil = jd['fotoPerfil'],
                saldo = jd['saldo']
                )
            datos = {'message': "Success"}
            return JsonResponse(datos)
    
    def put(self, request, rutEst=''):
        jd = json.loads(request.body)
        estudiantes = list(Estudiante.objects.filter(rutEst=rutEst).values())
        if len(estudiantes)>0:
            #dif entre filter y get. filter: al no encontrar, no devuelve error. get es lo opuesto
            estudiante = Estudiante.objects.get(rutEst=rutEst)
            estudiante.rutEst = jd['rutEst']
            estudiante.nombreEst = jd['nombreEst'] 
            estudiante.apellidoPaternoEst = jd['apellidoPaternoEst']
            estudiante.apellidoMaternoEst = jd['apellidoMaternoEst']
            estudiante.fechaNacimiento = jd['fechaNacimiento']
            estudiante.correoEst = jd['correoEst']
            estudiante.contrasenaEst = jd['contrasenaEst']
            estudiante.numeroTelefonoEst = jd['numeroTelefonoEst']
            estudiante.regionEst = jd['regionEst']
            estudiante.comunaEst = jd['comunaEst']
            estudiante.fotoPerfil = jd['fotoPerfil']
            estudiante.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Estudiante no encontrado"}
        return JsonResponse(datos)
    
    def delete(self, request, rutEst=''):

        estudiantes = list(Estudiante.objects.filter(rutEst=rutEst).values())
        if len(estudiantes)>0:
            Estudiante.objects.filter(rutEst=rutEst).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Estudiante no encontrado"}
        return JsonResponse(datos)
    
class Profesion(View):
    pass
