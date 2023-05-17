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
    
class ProfesionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, codigoVerificador=''):
        if (codigoVerificador):
            profesiones = list(Profesion.objects.filter(codigoVerificador=codigoVerificador).values())
            if len(profesiones)>0:
                profesion = profesiones[0]
                datos = {'message': "Success", 'profesion': profesion}
            else:
                datos = {'message': "profesion no encontrada"}
            return JsonResponse(datos)
        else:
            profesiones = list(Profesion.objects.values())
            if len(profesiones)>0:
                datos = {'message': "Success", 'profesiones': profesiones}
            else:
                datos = {'message': "No se encontraron profesiones"}
            return JsonResponse(datos)
    
    def post(self, request):
            #convertimos el formato de json a un diccionario de python
            jd = json.loads(request.body)
            Profesion.objects.create(
                codigoVerificador = jd['codigoVerificador'],
                institucion = jd['institucion'],
                profesion = jd['profesion'],
                anioEgreso = jd['anioEgreso'],
                tituloValidado = jd['tituloValidado'],
                rutProf_id = jd ['rutProf_id']
                )
            datos = {'message': "Success"}
            return JsonResponse(datos)
    
    def put(self, request, codigoVerificador=''):
        jd = json.loads(request.body)
        profesiones = list(Profesion.objects.filter(codigoVerificador=codigoVerificador).values())
        if len(profesiones)>0:
            #dif entre filter y get. filter: al no encontrar, no devuelve error. get es lo opuesto
            profesion = Profesion.objects.get(codigoVerificador=codigoVerificador)
            profesion.codigoVerificador = jd['codigoVerificador']
            profesion.institucion = jd['institucion']
            profesion.profesion = jd['profesion']
            profesion.anioEgreso = jd['anioEgreso']
            profesion.tituloValidado = jd['tituloValidado']
            profesion.rutProf_id = jd['rutProf_id']
            profesion.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Estudiante no encontrado"}
        return JsonResponse(datos)

    def delete(self, request, codigoVerificador=''):
        profesiones = list(Profesion.objects.filter(codigoVerificador=codigoVerificador).values())
        if len(profesiones)>0:
            Profesion.objects.filter(codigoVerificador=codigoVerificador).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Profesion no encontrada"}
        return JsonResponse(datos)
    
class AsignaturaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id>0):
            asignaturas = list(Asignatura.objects.filter(id=id).values())
            if len(asignaturas)>0:
                asignatura = asignaturas[0]
                datos = {'message': "Success", 'asignatura': asignatura}
            else:
                datos = {'message': "Asignatura no encontrada"}
            return JsonResponse(datos)
        else:
            asignaturas = list(Asignatura.objects.values())
            if len(asignaturas)>0:
                datos = {'message': "Success", 'asignaturas': asignaturas}
            else:
                datos = {'message': "No se encontraron asignaturas"}
            return JsonResponse(datos)
        
    def post(self, request):
            #convertimos el formato de json a un diccionario de python
            jd = json.loads(request.body)
            Asignatura.objects.create(
                id = jd['id'],
                nombreAsignatura = jd['nombreAsignatura'],
                carreraPerteneciente = jd['carreraPerteneciente'],
                descripcionAsignatura = jd['descripcionAsignatura'],
                )
            datos = {'message': "Success"}
            return JsonResponse(datos)
    
    def put(self, request, id=0):
        jd = json.loads(request.body)
        asignaturas = list(Asignatura.objects.filter(id=id).values())
        if len(asignaturas)>0:
            #dif entre filter y get. filter: al no encontrar, no devuelve error. get es lo opuesto
            asignatura = Asignatura.objects.get(id=id)
            asignatura.id = jd['id']
            asignatura.nombreAsignatura = jd['nombreAsignatura']
            asignatura.carreraPerteneciente = jd['carreraPerteneciente']
            asignatura.descripcionAsignatura = jd['descripcionAsignatura']
            asignatura.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Asignatura no encontrada"}
        return JsonResponse(datos)
    
    def delete(self, request, id=0):
        asignaturas = list(Asignatura.objects.filter(id=id).values())
        if len(asignaturas)>0:
            Asignatura.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "asignatura no encontrada"}
        return JsonResponse(datos)

class PublicacionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id>0):
            publicaciones = list(Publicacion.objects.filter(id=id).values())
            if len(publicaciones)>0:
                publicacion = publicaciones[0]
                datos = {'message': "Success", 'publicacion': publicacion}
            else:
                datos = {'message': "Publicacion no encontrada"}
            return JsonResponse(datos)
        else:
            publicaciones = list(Publicacion.objects.values())
            if len(publicaciones)>0:
                datos = {'message': "Success", 'publicaciones': publicaciones}
            else:
                datos = {'message': "No se encontraron publicaciones"}
            return JsonResponse(datos)
    
    def post(self, request):
            #convertimos el formato de json a un diccionario de python
            jd = json.loads(request.body)
            Publicacion.objects.create(
                id = jd['id'],
                titulo = jd['titulo'],
                descripcionPublicacion = jd['descripcionPublicacion'],
                fecha = jd['fecha'],
                hora = jd['hora'],
                rutEst_id = jd['rutEst_id'],
                idAsignatura_id = jd['idAsignatura_id'],
                )
            datos = {'message': "Success"}
            return JsonResponse(datos)
    
    def put(self, request, id=0):
        jd = json.loads(request.body)
        publicaciones = list(Publicacion.objects.filter(id=id).values())
        if len(publicaciones)>0:
            #dif entre filter y get. filter: al no encontrar, no devuelve error. get es lo opuesto
            publicacion = Publicacion.objects.get(id=id)
            publicacion.id = jd['id']
            publicacion.titulo = jd['titulo']
            publicacion.descripcionPublicacion = jd['descripcionPublicacion']
            publicacion.fecha = jd['fecha']
            publicacion.hora = jd['hora']
            publicacion.rutEst_id = jd['rutEst_id']
            publicacion.idAsignatura_id = jd['idAsignatura_id']
            publicacion.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Publicacion no encontrada"}
        return JsonResponse(datos)
    
    def delete(self, request, id=0):
        publicaciones = list(Publicacion.objects.filter(id=id).values())
        if len(publicaciones)>0:
            Publicacion.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Publicacion no encontrada"}
        return JsonResponse(datos)

class DescripcionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id>0):
            descripciones = list(Descripcion.objects.filter(id=id).values())
            if len(descripciones)>0:
                descripcion = descripciones[0]
                datos = {'message': "Success", 'descripcion': descripcion}
            else:
                datos = {'message': "Descripcion no encontrada"}
            return JsonResponse(datos)
        else:
            descripciones = list(Descripcion.objects.values())
            if len(descripciones)>0:
                datos = {'message': "Success", 'descripciones': descripciones}
            else:
                datos = {'message': "No se encontraron descripciones"}
            return JsonResponse(datos)
    
    def post(self, request):
            #convertimos el formato de json a un diccionario de python
            jd = json.loads(request.body)
            Descripcion.objects.create(
                id = jd['id'],
                descripcionTutor = jd['descripcionTutor'],
                rutProf_id = jd['rutProf_id'],
                )
            datos = {'message': "Success"}
            return JsonResponse(datos)
    
    def put(self, request, id=0):
        jd = json.loads(request.body)
        descipciones = list(Descripcion.objects.filter(id=id).values())
        if len(descipciones)>0:
            #dif entre filter y get. filter: al no encontrar, no devuelve error. get es lo opuesto
            descripcion = Descripcion.objects.get(id=id)
            descripcion.id = jd['id']
            descripcion.descripcionTutor = jd['descripcionTutor']
            descripcion.rutProf_id = jd['rutProf_id']
            descripcion.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Descripcion no encontrada"}
        return JsonResponse(datos)
    
    def delete(self, request, id=0):
        descripciones = list(Descripcion.objects.filter(id=id).values())
        if len(descripciones)>0:
            Descripcion.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Descripcion no encontrada"}
        return JsonResponse(datos)
    
class ClaseView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id>0):
            clases = list(Clase.objects.filter(id=id).values())
            if len(clases)>0:
                clase = clases[0]
                datos = {'message': "Success", 'clase': clase}
            else:
                datos = {'message': "Clase no encontrada"}
            return JsonResponse(datos)
        else:
            clases = list(Clase.objects.values())
            if len(clases)>0:
                datos = {'message': "Success", 'clases': clases}
            else:
                datos = {'message': "No se encontraron clases"}
            return JsonResponse(datos)
    
    def post(self, request):
            #convertimos el formato de json a un diccionario de python
            jd = json.loads(request.body)
            Clase.objects.create(
                id = jd['id'],
                fecha = jd['fecha'],
                hora = jd['hora'],
                modalidad = jd['modalidad'],
                rutProf_id = jd['rutProf_id'],
                idAsignatura_id = jd['idAsignatura_id'],
                )
            datos = {'message': "Success"}
            return JsonResponse(datos)
    
    def put(self, request, id=0):
        jd = json.loads(request.body)
        clases = list(Clase.objects.filter(id=id).values())
        if len(clases)>0:
            #dif entre filter y get. filter: al no encontrar, no devuelve error. get es lo opuesto
            clase = Clase.objects.get(id=id)
            clase.id = jd['id']
            clase.fecha = jd['fecha']
            clase.hora = jd['hora']
            clase.modalidad = jd['modalidad']
            clase.rutProf_id = jd['rutProf_id']
            clase.idAsignatura_id = jd['idAsignatura_id']
            clase.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Clase no encontrada"}
        return JsonResponse(datos)
    
    def delete(self, request, id=0):
        clases = list(Clase.objects.filter(id=id).values())
        if len(clases)>0:
            Clase.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Clase no encontrada"}
        return JsonResponse(datos)

class ComentarioView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id>0):
            comentarios = list(Comentario.objects.filter(id=id).values())
            if len(comentarios)>0:
                comentario = comentarios[0]
                datos = {'message': "Success", 'comentario': comentario}
            else:
                datos = {'message': "Comentario no encontrado"}
            return JsonResponse(datos)
        else:
            comentarios = list(Comentario.objects.values())
            if len(comentarios)>0:
                datos = {'message': "Success", 'comentarios': comentarios}
            else:
                datos = {'message': "No se encontraron comentarios"}
            return JsonResponse(datos)

    def post(self, request):
            #convertimos el formato de json a un diccionario de python
            jd = json.loads(request.body)
            Comentario.objects.create(
                id = jd['id'],
                comentario = jd['comentario'],
                valoracion = jd['valoracion'],
                fecha = jd['fecha'],
                rutEst_id = jd['rutEst_id'],
                rutProf_id = jd['rutProf_id'],
                )
            datos = {'message': "Success"}
            return JsonResponse(datos)
    
    def put(self, request, id=0):
        jd = json.loads(request.body)
        comentarios = list(Comentario.objects.filter(id=id).values())
        if len(comentarios)>0:
            #dif entre filter y get. filter: al no encontrar, no devuelve error. get es lo opuesto
            comentario = Comentario.objects.get(id=id)
            comentario.id = jd['id']
            comentario.comentario = jd['comentario']
            comentario.valoracion = jd['valoracion']
            comentario.fecha = jd['fecha']
            comentario.rutEst_id = jd['rutEst_id']
            comentario.rutProf_id = jd['rutProf_id']
            comentario.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Comentario no encontrada"}
        return JsonResponse(datos)
    
    def delete(self, request, id=0):
        comentarios = list(Comentario.objects.filter(id=id).values())
        if len(comentarios)>0:
            Comentario.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Comentario no encontrada"}
        return JsonResponse(datos)
    
class ClaseAgendadaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id>0):
            clasesAgendadas = list(ClaseAgendada.objects.filter(id=id).values())
            if len(clasesAgendadas)>0:
                clasesAgendada = clasesAgendadas[0]
                datos = {'message': "Success", 'clasesAgendada': clasesAgendada}
            else:
                datos = {'message': "Clase agendada no encontrado"}
            return JsonResponse(datos)
        else:
            clasesAgendadas = list(ClaseAgendada.objects.values())
            if len(clasesAgendadas)>0:
                datos = {'message': "Success", 'clasesAgendadas': clasesAgendadas}
            else:
                datos = {'message': "No se encontraron clases agendadas"}
            return JsonResponse(datos)
    
    def post(self, request):
            #convertimos el formato de json a un diccionario de python
            jd = json.loads(request.body)
            ClaseAgendada.objects.create(
                id = jd['id'],
                rutProf_id = jd['rutProf_id'],
                rutEst_id = jd['rutEst_id'],
                idClase_id = jd['idClase_id'],
                )
            datos = {'message': "Success"}
            return JsonResponse(datos)

    def put(self, request, id=0):
        jd = json.loads(request.body)
        clasesAgendadas = list(ClaseAgendada.objects.filter(id=id).values())
        if len(clasesAgendadas)>0:
            #dif entre filter y get. filter: al no encontrar, no devuelve error. get es lo opuesto
            claseAgendada = ClaseAgendada.objects.get(id=id)
            claseAgendada.id = jd['id']
            claseAgendada.rutProf_id = jd['rutProf_id']
            claseAgendada.rutEst_id = jd['rutEst_id']
            claseAgendada.idClase_id = jd['idClase_id']
            claseAgendada.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Clase agendada no encontrada"}
        return JsonResponse(datos)

    def delete(self, request, id=0):
        clasesAgendadas = list(ClaseAgendada.objects.filter(id=id).values())
        if len(clasesAgendadas)>0:
            ClaseAgendada.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Clase agendada no encontrada"}
        return JsonResponse(datos)

class NotificacionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id>0):
            notificaciones = list(Notificacion.objects.filter(id=id).values())
            if len(notificaciones)>0:
                notificacion = notificaciones[0]
                datos = {'message': "Success", 'notificacion': notificacion}
            else:
                datos = {'message': "Notificacion no encontrada"}
            return JsonResponse(datos)
        else:
            notificaciones = list(Notificacion.objects.values())
            if len(notificaciones)>0:
                datos = {'message': "Success", 'notificaciones': notificaciones}
            else:
                datos = {'message': "No se encontraron notificaciones"}
            return JsonResponse(datos)
    
    def post(self, request):
            #convertimos el formato de json a un diccionario de python
            jd = json.loads(request.body)
            Notificacion.objects.create(
                id = jd['id'],
                descripcion = jd['descripcion'],
                rutEst_id = jd['rutEst_id']                
                )
            datos = {'message': "Success"}
            return JsonResponse(datos)
    
    def put(self, request, id=0):
        jd = json.loads(request.body)
        notificaciones = list(Notificacion.objects.filter(id=id).values())
        if len(notificaciones)>0:
            #dif entre filter y get. filter: al no encontrar, no devuelve error. get es lo opuesto
            notificacion = Notificacion.objects.get(id=id)
            notificacion.id = jd['id']
            notificacion.descripcion = jd['descripcion']
            notificacion.rutEst_id = jd['rutEst_id']            
            notificacion.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Notificacion no encontrada"}
        return JsonResponse(datos)
    
    def delete(self, request, id=0):
        notificaiones = list(Notificacion.objects.filter(id=id).values())
        if len(notificaiones)>0:
            Notificacion.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Notificacion no encontrada"}
        return JsonResponse(datos)