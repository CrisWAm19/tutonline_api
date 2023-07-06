from django.shortcuts import render, redirect, get_object_or_404
from api.models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from UsuarioApp.views import Perfil
from django.core.mail import EmailMessage
from django.urls import reverse
from api.models import User
from api.models import Clase
from UsuarioApp.views import calcular_anios_pasados
# Create your views here.

# @login_required
def ListClases(request):
    clases = Clase.objects.all().select_related('idProfesor')
    dataClases = {'clases' : clases}
    return render (request, 'ClasesTemplates/Clases.html', dataClases)

@login_required
def AgregarClase(request):
    data = {'form': FormClase(initial={'idProfesor': request.user.id})}
    if request.method == 'POST':
        form = FormClase(data=request.POST)
        if form.is_valid():
            clase = form.save(commit=False)
            clase.idProfesor_id = request.user.id
            form.save()
            messages.success(request, "Clase Registrada")
            return redirect(Perfil)
        else: 
            data["form"] = form
    return render (request, 'ClasesTemplates/AgregarClase.html',data)

@login_required
def ListaClasesAgendadas(request):
    user_id = request.user.id
    clasesAgendadas = ClaseAgendada.objects.filter(idProfesor_id=user_id)
    profesion = Profesion.objects.filter(idProfesor_id=user_id)
    descripcion = Descripcion.objects.filter(idProfesor_id=user_id)
    def ObtenerAnios(request):
        profesion = Profesion.objects.filter(idProfesor=request.user.id).first()
        anio_egreso = profesion.anioEgreso if profesion else None
        anios_pasados = calcular_anios_pasados(anio_egreso) if anio_egreso else None
        return {'anios_pasados':anios_pasados}
    context ={
        **ObtenerAnios(request),
        'clasesAgendadas':clasesAgendadas,
        'profesion':profesion,
        'descripcion':descripcion
    }
    return render(request,'ClasesTemplates/ClasesAgendadas.html',context)

@login_required
def AgendarClase(request):
    data = {'form': FormClaseAgendada(initial={'idProfesor': request.user.id})}
    if request.method == 'POST':
        form = FormClaseAgendada(data=request.POST)
        if form.is_valid():
            clase = form.save(commit=False)
            clase.idProfesor_id = request.user.id
            form.save()
            messages.success(request, "Clase agendada registrada")
            return redirect(Perfil)
        else: 
            data["form"] = form
    return render (request, 'ClasesTemplates/AgendarClase.html',data)

def EditarClaseAgendada (request,id):
    claseAgendada = get_object_or_404(ClaseAgendada, id=id)
    form  = FormClaseAgendada(instance=claseAgendada)
    if request.method == 'POST':
        form = FormClaseAgendada(request.POST, instance=claseAgendada)
        if form.is_valid():
            form.save()
            return redirect(ListaClasesAgendadas)
        else:
            context = {'form': form }
    context = {
        'form': form
    }
    return render(request, 'registration/update.html', context)
    

@login_required
def EditarClase(request,id):
    clase = get_object_or_404(Clase, id=id)
    form  = FormClase(instance=clase)
    if request.method == 'POST':
        form = FormClase(request.POST, instance=clase)
        if form.is_valid():
            form.save()
            return redirect(Perfil)
        else:
            context = {'form': form }
    context = {
        'form': form
    }
    return render(request, 'registration/update.html', context)

@login_required
def EliminarClase(request,id):
    clase = Clase.objects.get(id=id)
    clase.delete()
    return redirect(Perfil)

@login_required
def correo(request):
    current_user = request.user
    correos_qs = User.objects.filter(clase__isnull=False).values_list('email', flat=True).distinct()
    correos = list(correos_qs) 
    correos_string = ', '.join(correos)
    formulario = FormularioContacto(data=request.POST) 
    nombreCompleto = f"{current_user.first_name} {current_user.last_name}"
    if formulario.is_valid():
        nombre = nombreCompleto
        email = correos_string
        contenido = request.POST.get("contenido")
        email = EmailMessage("Mensaje de tutOnline",
            "El usuario {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre, email, contenido), '',
            correos,
            reply_to=correos)
        try:
           email.send()
           return redirect(reverse('Perfil') + '?valido')
        except:
           return redirect(reverse('Perfil') + '?novalido')
       
    return render(request, 'ClasesTemplates/Correo.html', {'miFormulario':formulario, 'current_user':current_user})



def CrearSolicitud(request, clase_id=None):

    profesor_username = request.GET.get('profesor_username')
    id_clase = clase_id
    profesor = User.objects.get(username=profesor_username)  # Obtén la instancia del profesor
    id_estudiante = request.user  # Obtén la instancia del estudiante actual
    clase = Clase.objects.get(id=id_clase)  # Obtén la instancia de la clase correspondiente al ID proporcionado
    solicitud = Solicitud.objects.create(
        estadoSolicitud='Pendiente',
        idEstudiante=id_estudiante,
        idProfesor=profesor,
        idClase=clase  # Asigna la instancia de la clase
    )
    return redirect(Solicitudes)

def Solicitudes(request):
    usuario = request.user
    profesion = None 
    descripcion = None
    if usuario.tipoDeUsuario == "Estudiante":
        solicitudes = usuario.estudiante_solicitante.all()
    elif usuario.tipoDeUsuario == "Tutor":
        solicitudes = usuario.profesor_solicitado.all()
        profesion = Profesion.objects.filter(idProfesor_id=usuario)
        descripcion = Descripcion.objects.filter(idProfesor_id=usuario)
    def ObtenerAnios(request):
        profesion = Profesion.objects.filter(idProfesor=request.user.id).first()
        anio_egreso = profesion.anioEgreso if profesion else None
        anios_pasados = calcular_anios_pasados(anio_egreso) if anio_egreso else None
        return {'anios_pasados':anios_pasados}
    context ={
        **ObtenerAnios(request),
        'solicitudes': solicitudes,
        'profesion':profesion,
        'descripcion':descripcion
    }
    return render(request, 'SolicitudesTemplates/Solicitudes.html',context)

def EliminarSolicitud(request,id):
    solicitud = Solicitud.objects.get(id=id)
    solicitud.delete()
    return redirect(Solicitudes)

def EditarSolicitudA(request, id):

    solicitud = get_object_or_404(Solicitud, id=id)
    # Actualizar el campo estadoSolicitud a "Aceptada"
    solicitud.estadoSolicitud = 'Aceptada'
    solicitud.save()
    return redirect('Solicitudes')

def EditarSolicitudR(request, id):
    solicitud = get_object_or_404(Solicitud, id=id)
    # Actualizar el campo estadoSolicitud a "Aceptada"
    solicitud.estadoSolicitud = 'Rechazada'
    solicitud.save()
    return redirect('Solicitudes')