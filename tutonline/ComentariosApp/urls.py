from django.urls import path, include
from ComentariosApp import views

urlpatterns = [
    path('Comentarios/<str:username>',views.ComentariosPerfilVisita, name='Comentarios'),
    path('ComentariosPerfilLogeado/',views.ComentariosPerfilLogeado, name='Comentarios Tutor'),
    
]