from django.urls import path
from UsuarioApp import views

urlpatterns = [
    path('Perfil/',views.Perfil, name='Perfil'),
    path('Publicacion/',views.PublicacionEstudiante, name='Publicacion'),
]