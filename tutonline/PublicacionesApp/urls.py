from django.urls import path
from PublicacionesApp import views

urlpatterns = [
    path('AgregarPublicacion/',views.PublicacionEstudiante, name='Agregar Publicacion'),
    path('Publicaciones/',views.ListPublicaciones, name='Publicaciones'),
    path('EditarPublicacion/<int:id>',views.EditarPublicacion, name='Editar Publicacion'),
    path('EliminarPublicacion/<int:id>',views.EliminarPublicacion, name='Eliminar Publicacion'),
    path('Responder/<str:username>', views.ResponderPublicacion, name="mail")
]


