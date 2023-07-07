from django.urls import path, include
from ComentariosApp import views

urlpatterns = [
    path('Comentarios/<str:username>',views.ComentariosPerfilVisita, name='Comentarios'),
    path('ComentariosPerfilLogeado/',views.ComentariosPerfilLogeado, name='Comentarios Tutor'),
    path('EditarComentario/<int:id>',views.EditarComentario, name='Editar Comentario'),
    path('EliminarComentario/<int:id>',views.EliminarComentario, name='Eliminar Comentario'),
    
]