from django.contrib import admin
from .models import *
import sys

class BuscarProfAdmin(admin.ModelAdmin):
    list_display=('rutProf','nombreProf','apellidoPaternoProf','apellidoMaternoProf')
    search_fields = ('rutProf','nombreProf','apellidoPaternoProf','apellidoMaternoProf')
class BuscarEstAdmin(admin.ModelAdmin):
    list_display=('rutEst','nombreEst','apellidoPaternoEst','apellidoMaternoEst')
    search_fields = ('rutEst','nombreEst','apellidoPaternoEst','apellidoMaternoEst')
class BuscarProfesionAdmin(admin.ModelAdmin):
    list_display=('codigoVerificador','institucion','profesion','anioEgreso','tituloValidado','rutProf')
    search_fields = ('codigoVerificador','institucion','profesion','anioEgreso','tituloValidado')
class BuscarDescripcionAdmin(admin.ModelAdmin):
    list_display=('id','descripcionTutor','rutProf')
    search_fields = ('id','descripcionTutor')
class BuscarAsignaturaAdmin(admin.ModelAdmin):
    list_display=('id','nombreAsignatura','carreraPerteneciente','descripcionAsignatura')
    search_fields = ('id','nombreAsignatura','carreraPerteneciente','descripcionAsignatura')
class BuscadorClaseAdmin(admin.ModelAdmin):
    list_display=('id','fecha','hora','modalidad','rutProf','idAsignatura')
    search_fields = ('id','fecha','hora','modalidad')
class BuscadorPublicacionAdmin(admin.ModelAdmin):
    list_display=('id','titulo','descripcionPublicacion','fecha','hora','rutEst','idAsignatura')
    search_fields = ('id','titulo','descripcionPublicacion','fecha','hora')
class BuscadorComentarioAdmin(admin.ModelAdmin):
    list_display=('id','comentario','valoracion','fecha','rutEst','rutProf')
    search_fields = ('id','comentario','valoracion','fecha')
class BuscadorClaseAgendadaAdmin(admin.ModelAdmin):
    list_display=('id','rutProf','rutEst','idClase')
    search_fields = ['id']
class BuscadorNotificacionAdmin(admin.ModelAdmin):
    list_display=('id','descripcion','rutEst')
    search_fields = ('id','descripcion')

admin.site.register(Profesor,BuscarProfAdmin)
admin.site.register(Estudiante,BuscarEstAdmin)
admin.site.register(Profesion,BuscarProfesionAdmin)
admin.site.register(Descripcion,BuscarDescripcionAdmin)
admin.site.register(Asignatura,BuscarAsignaturaAdmin)
admin.site.register(Clase,BuscadorClaseAdmin)
admin.site.register(Publicacion,BuscadorPublicacionAdmin)
admin.site.register(Comentario,BuscadorComentarioAdmin)
admin.site.register(ClaseAgendada,BuscadorClaseAgendadaAdmin)
admin.site.register(Notificacion,BuscadorNotificacionAdmin)

