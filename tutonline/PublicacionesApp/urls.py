from django.urls import path
from PublicacionesApp import views

urlpatterns = [
    path('AgregarPublicacion/',views.PublicacionEstudiante, name='Agregar Publicacion'),
    path('Publicaciones/',views.ListPublicaciones, name='Publicaciones'),
]


