from django.urls import path
from ClasesApp import views

urlpatterns = [
    path('clases/',views.ListClases, name='clases'),
    path('agregarClase/',views.AgregarClase, name='Agregar clases'),
    path('agendarClase/',views.AgendarClase, name='Agendar clases'),
    path('ClasesAgendadas/',views.ListaClasesAgendadas, name='Clases agendadas'),
    path('EditarClase/<int:id>',views.EditarClase, name='Editar Clase'),
    path('EliminarClase/<int:id>',views.EliminarClase, name='Eliminar Clase'),
    
]