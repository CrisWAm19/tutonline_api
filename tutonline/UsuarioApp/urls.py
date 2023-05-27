from django.urls import path
from UsuarioApp import views

urlpatterns = [
    path('Perfil/',views.Perfil, name='Perfil')
]