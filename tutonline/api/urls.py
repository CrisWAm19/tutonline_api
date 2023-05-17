from django.urls import path
from .views import *


urlpatterns = [
    path('profesores/', ProfesorView.as_view(),name='profesores_list'),
    path('profesores/<str:rutProf>', ProfesorView.as_view(),name='profesores_process'),
    
    path('estudiantes/', EstudianteView.as_view(),name='estudiantes_list'),
    path('estudiantes/<str:rutEst>', EstudianteView.as_view(),name='estudiantes_process'),

    path('profesiones/', ProfesionView.as_view(),name='profesiones_list'),
    path('profesiones/<str:codigoVerificador>', ProfesionView.as_view(),name='profesiones_process'),

    path('asignaturas/', AsignaturaView.as_view(),name='asignaturas_list'),
    path('asignaturas/<int:id>', AsignaturaView.as_view(),name='asignaturas_process'),

    path('publicaciones/', PublicacionView.as_view(),name='publicaciones_list'),
    path('publicaciones/<int:id>', PublicacionView.as_view(),name='publicaciones_process'),

    path('descripciones/', DescripcionView.as_view(),name='descripciones_list'),
    path('descripciones/<int:id>', DescripcionView.as_view(),name='descripciones_process'),

    path('clases/', ClaseView.as_view(),name='clases_list'),
    path('clases/<int:id>', ClaseView.as_view(),name='clases_process'),

    path('comentarios/', ComentarioView.as_view(),name='comentarios_list'),
    path('comentarios/<int:id>', ComentarioView.as_view(),name='comentarios_process'),

    path('clasesagendadas/', ClaseAgendadaView.as_view(),name='clasesagendadas_list'),
    path('clasesagendadas/<int:id>', ClaseAgendadaView.as_view(),name='clasesagendadas_process'),

    path('notificaciones/', NotificacionView.as_view(),name='notificaciones_list'),
    path('notificaciones/<int:id>', NotificacionView.as_view(),name='notificaciones_process'),


]