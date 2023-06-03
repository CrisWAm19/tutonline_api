from django.contrib import admin
from .models import *
import sys

class BuscarUserAdmin(admin.ModelAdmin):
    list_display=('rut','first_name','last_name','tipoDeUsuario')
    search_fields = ('rut','first_name','last_name','tipoDeUsuario')
class BuscarProfesionAdmin(admin.ModelAdmin):
    list_display=('codigoVerificador','institucion','profesion','anioEgreso','tituloValidado','idProfesor')
    search_fields = ('codigoVerificador','institucion','profesion','anioEgreso','tituloValidado')
class BuscarDescripcionAdmin(admin.ModelAdmin):
    list_display=('id','descripcionTutor','idProfesor')
    search_fields = ('id','descripcionTutor')
class BuscarAsignaturaAdmin(admin.ModelAdmin):
    list_display=('id','nombreAsignatura','descripcionAsignatura','idCarrera')
    search_fields = ('id','nombreAsignatura','descripcionAsignatura')
# class BuscarClaseAdmin(admin.ModelAdmin):
#     list_display=('id','nombreAsignatura','descripcionAsignatura','idCarrera')
#     search_fields = ('id','nombreAsignatura','descripcionAsignatura')
class BuscadorClaseAdmin(admin.ModelAdmin):
    list_display=('id','fecha','hora','modalidad','tarifa','idProfesor','idAsignatura')
    search_fields = ('id','fecha','hora','modalidad','tarifa')
class BuscadorPublicacionAdmin(admin.ModelAdmin):
    list_display=('id','titulo','descripcionPublicacion','fecha','hora','idEstudiante','idAsignatura')
    search_fields = ('id','titulo','descripcionPublicacion','fecha','hora')
class BuscadorComentarioAdmin(admin.ModelAdmin):
    list_display=('id','comentario','valoracion','fecha','idEstudianteEmisor','idProfesorReceptor')
    search_fields = ('id','comentario','valoracion','fecha')
class BuscadorClaseAgendadaAdmin(admin.ModelAdmin):
    list_display=('id','idEstudiante','idProfesor','idClase')
    search_fields = ['id']
class BuscadorNotificacionAdmin(admin.ModelAdmin):
    list_display=('id','descripcion','idEstudiante')
    search_fields = ('id','descripcion')
class BuscadorSolicitudnAdmin(admin.ModelAdmin):
    list_display=('id','estadoSolicitud','idEstudiante','idProfesor','idClase')
    search_fields = ('id','estadoSolicitud')

admin.site.register(User, BuscarUserAdmin)
admin.site.register(Profesion,BuscarProfesionAdmin)
admin.site.register(Descripcion,BuscarDescripcionAdmin)
admin.site.register(Asignatura,BuscarAsignaturaAdmin)
admin.site.register(Carrera)
admin.site.register(Clase,BuscadorClaseAdmin)
admin.site.register(Publicacion,BuscadorPublicacionAdmin)
admin.site.register(Comentario,BuscadorComentarioAdmin)
admin.site.register(ClaseAgendada,BuscadorClaseAgendadaAdmin)
admin.site.register(Notificacion,BuscadorNotificacionAdmin)
admin.site.register(Solicitud,BuscadorSolicitudnAdmin)

