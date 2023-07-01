from django.urls import path
from ClasesApp import views

urlpatterns = [
    path('clases/',views.ListClases, name='clases'),
    path('agregarClase/',views.AgregarClase, name='Agregar clases'),
    path('agendarClase/',views.AgendarClase, name='Agendar clases'),
    path('ClasesAgendadas/',views.ListaClasesAgendadas, name='Clases agendadas'),
    path('EditarClasesAgendadas/<int:id>',views.EditarClaseAgendada, name='Editar clases agendadas'),
    path('EditarClase/<int:id>',views.EditarClase, name='Editar Clase'),
    path('EliminarClase/<int:id>',views.EliminarClase, name='Eliminar Clase'),
    path('mail/', views.correo, name="mail"),
    path('Solicitud/<int:clase_id>/', views.CrearSolicitud, name="CrearSolicitud"),
    path('Solicitudes/', views.Solicitudes, name="Solicitudes"),
    path('EliminarSolicitud/<int:id>',views.EliminarSolicitud, name='Eliminar Solicitud'),
    path('EditarSolicitudA/<int:id>',views.EditarSolicitudA, name='Editar Solicitud'),
    path('EditarSolicitudR/<int:id>',views.EditarSolicitudR, name='Rechazar Solicitud'),
    
    ]