from django.contrib import admin
from .models import *
import sys

class BuscarProfAdmin(admin.ModelAdmin):
    search_fields = ['rutProf']
class BuscarEstAdmin(admin.ModelAdmin):
    search_fields = ['rutEst']
class BuscarProfesionAdmin(admin.ModelAdmin):
    search_fields = ['codigoVerificador']
class BuscarDescripcionAdmin(admin.ModelAdmin):
    search_fields = ['id']
class BuscarAsignaturaAdmin(admin.ModelAdmin):
    search_fields = ['id']
class BuscadorClaseAdmin(admin.ModelAdmin):
    search_fields = ['id']
class BuscadorPublicacionAdmin(admin.ModelAdmin):
    search_fields = ['id']
class BuscadorComentarioAdmin(admin.ModelAdmin):
    search_fields = ['id']
class BuscadorClaseAgendadaAdmin(admin.ModelAdmin):
    search_fields = ['id']

admin.site.register(Profesor,BuscarProfAdmin)
admin.site.register(Estudiante,BuscarEstAdmin)
admin.site.register(Profesion,BuscarProfesionAdmin)
admin.site.register(Descripcion,BuscarDescripcionAdmin)
admin.site.register(Asignatura,BuscarAsignaturaAdmin)
admin.site.register(Clase,BuscadorClaseAdmin)
admin.site.register(Publicacion,BuscadorPublicacionAdmin)
admin.site.register(Comentario,BuscadorComentarioAdmin)
admin.site.register(ClaseAgendada,BuscadorClaseAgendadaAdmin)

