from django.urls import path
from UsuarioApp import views

urlpatterns = [
    path('Perfil/',views.Perfil, name='Perfil'),
    path('PerfilTutor/<str:username>',views.PerfilTutor, name='Perfil Tutor'),
    path('PerfilEstudiante/<str:username>',views.PerfilEstudiante, name='Perfil Estudiante'),
    path('ProfesionTutor/',views.ProfesionTutor, name='Profesion Tutor'),
    path('EditarProfesion/',views.EditarProfesion, name='Editar Profesion')
]