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
    '''La función ListClases recupera todos los objetos Clase y sus objetos Profesor asociados, y luego
    genera una plantilla con los datos recuperados.
    
    Parameters
    ----------
    request
        El objeto de solicitud representa la solicitud HTTP que el usuario realizó para acceder a la página
    web. Contiene información como el navegador del usuario, la dirección IP y cualquier dato que se
    haya enviado con la solicitud.
    
    Returns
    -------
        una plantilla HTML renderizada llamada 'Clases.html' con los datos 'dataClases' pasados a ella.
    
    '''
    clases = Clase.objects.all().select_related('idProfesor')
    dataClases = {'clases' : clases}
    return render (request, 'ClasesTemplates/Clases.html', dataClases)

@login_required
def AgregarClase(request):
    '''La función "AgregarClase" se usa para agregar una nueva clase a la base de datos y mostrar un
    mensaje de éxito si la clase se registró correctamente.
    
    Parameters
    ----------
    request
        El parámetro `request` es un objeto que representa la solicitud HTTP realizada por el usuario.
    Contiene información sobre la solicitud, como la sesión del usuario, el método HTTP utilizado (GET,
    POST, etc.) y cualquier dato enviado con la solicitud.
    
    Returns
    -------
        una plantilla HTML renderizada llamada 'ClassesTemplates/AgregarClase.html' con el diccionario de
    datos como contexto.
    
    '''
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
    def ObtenerAnios(request):
        profesion = Profesion.objects.filter(idProfesor=request.user.id).first()
        anio_egreso = profesion.anioEgreso if profesion else None
        anios_pasados = calcular_anios_pasados(anio_egreso) if anio_egreso else None
        return {'anios_pasados':anios_pasados}
    context ={
        **ObtenerAnios(request),
        'clasesAgendadas':clasesAgendadas,
        'profesion':profesion
    }
    return render(request,'ClasesTemplates/ClasesAgendadas.html',context)

@login_required
def AgendarClase(request):
    '''La función "AgendarClase" se usa para manejar el proceso de programar una clase, incluida la
    validación del formulario y guardar la información de la clase.
    
    Parameters
    ----------
    request
        El parámetro "solicitud" es un objeto que representa la solicitud HTTP realizada por el usuario.
    Contiene información sobre la solicitud, como la sesión del usuario, el método HTTP utilizado (GET,
    POST, etc.) y cualquier dato enviado con la solicitud.
    
    Returns
    -------
        una plantilla HTML renderizada llamada 'AgendarClase.html' con el diccionario de datos como
    contexto.
    
    '''
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
    '''La función "EditarClase" se utiliza para editar un objeto de clase y guardar los cambios en la base
    de datos.
    
    Parameters
    ----------
    request
        El objeto de solicitud representa la solicitud HTTP que el usuario realizó para acceder a la vista.
    Contiene información como la sesión del usuario, el método HTTP utilizado (GET o POST) y cualquier
    dato enviado en la solicitud.
    id
        El parámetro id es el identificador único del objeto Clase que debe editarse.
    
    Returns
    -------
        una plantilla HTML renderizada llamada 'registro/actualización.html' con la variable de contexto
    que contiene el objeto 'formulario'.
    
    '''
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
    '''La función "EliminarClase" elimina un objeto de clase con una identificación específica y redirige a
    la página "Perfil".
    
    Parameters
    ----------
    request
        El objeto de solicitud contiene información sobre la solicitud HTTP actual, como el usuario que
    realiza la solicitud, el método utilizado (GET o POST) y cualquier dato enviado con la solicitud.
    id
        El parámetro id es el identificador único del objeto Clase que debe eliminarse.
    
    Returns
    -------
        una redirección a la vista "Perfil".
    
    '''
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
    '''La función crea una nueva instancia de un objeto Solicitud con la información proporcionada y
    redirige a la página de Solicitudes.
    
    Parameters
    ----------
    request
        El objeto de solicitud representa la solicitud HTTP que el usuario realizó al servidor. Contiene
    información como la sesión del usuario, el método HTTP utilizado (GET, POST, etc.) y cualquier dato
    que se envió con la solicitud.
    clase_id
        El parámetro `clase_id` es un parámetro opcional que representa el ID de una clase. Se utiliza para
    recuperar la instancia de la clase correspondiente al ID proporcionado.
    
    Returns
    -------
        una redirección a la vista "Solicitudes".
    
    '''
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
    '''La función "Solicitudes" recupera y muestra las solicitudes realizadas por un usuario, en función de
    su tipo de usuario (estudiante o tutor), junto con información adicional como profesión y años de
    egreso.
    
    Parameters
    ----------
    request
        El parámetro `request` es un objeto que representa la solicitud HTTP realizada por el usuario.
    Contiene información como la sesión del usuario, la URL solicitada y cualquier dato enviado con la
    solicitud.
    
    Returns
    -------
        una plantilla HTML renderizada con los datos de contexto.
    
    '''
    usuario = request.user
    profesion = None 
    if usuario.tipoDeUsuario == "Estudiante":
        solicitudes = usuario.estudiante_solicitante.all()
    elif usuario.tipoDeUsuario == "Tutor":
        solicitudes = usuario.profesor_solicitado.all()
        profesion = Profesion.objects.filter(idProfesor_id=usuario)
    def ObtenerAnios(request):
        '''La función `ObtenerAnios` recupera el año de graduación de un determinado usuario y calcula el
        número de años que han pasado desde entonces.
        
        Parameters
        ----------
        request
            El parámetro "solicitud" es un objeto que representa la solicitud HTTP realizada por el
        usuario. Contiene información como la sesión del usuario, la URL solicitada y cualquier dato
        enviado con la solicitud. En este caso, se utiliza para identificar al usuario actual y
        recuperar su información de profesión.
        
        Returns
        -------
            un diccionario con la clave 'años_pasados' y el valor de la variable 'años_pasados'.
        
        '''
        profesion = Profesion.objects.filter(idProfesor=request.user.id).first()
        anio_egreso = profesion.anioEgreso if profesion else None
        anios_pasados = calcular_anios_pasados(anio_egreso) if anio_egreso else None
        return {'anios_pasados':anios_pasados}
    context ={
        **ObtenerAnios(request),
        'solicitudes': solicitudes,
        'profesion':profesion
    }
    return render(request, 'SolicitudesTemplates/Solicitudes.html',context)

def EliminarSolicitud(request,id):
    '''La función "EliminarSolicitud" borra un objeto específico de "Solicitud" y redirige a la página de
    "Solicitudes".
    
    Parameters
    ----------
    request
        El objeto de solicitud representa la solicitud HTTP que la función de vista recibió del cliente.
    Contiene información sobre la solicitud, como el método HTTP (GET, POST, etc.), encabezados y
    cualquier dato enviado con la solicitud.
    id
        El parámetro id es el identificador único del objeto Solicitud que debe eliminarse.
    
    Returns
    -------
        una redirección a la página "Solicitudes".
    
    '''
    solicitud = Solicitud.objects.get(id=id)
    solicitud.delete()
    return redirect(Solicitudes)

def EditarSolicitudA(request, id):
    '''La función `EditarSolicitudA` actualiza el campo `estadoSolicitud` de un objeto `Solicitud` a
    "Aceptada" y redirige a la página "Solicitudes".
    
    Parameters
    ----------
    request
        El objeto de solicitud representa la solicitud HTTP que realizó el usuario. Contiene información
    sobre la solicitud, como el método utilizado (GET o POST), los encabezados y el cuerpo de la
    solicitud.
    id
        El parámetro id es el identificador único del objeto Solicitud que necesita ser editado.
    
    Returns
    -------
        una redirección a la URL de 'Solicitudes'.
    
    '''
    solicitud = get_object_or_404(Solicitud, id=id)
    # Actualizar el campo estadoSolicitud a "Aceptada"
    solicitud.estadoSolicitud = 'Aceptada'
    solicitud.save()
    return redirect('Solicitudes')

def EditarSolicitudR(request, id):
    '''La función `EditarSolicitudR` actualiza el campo `estadoSolicitud` de un objeto `Solicitud` a
    "Rechazada" y redirige a la página "Solicitudes".
    
    Parameters
    ----------
    request
        El objeto de solicitud representa la solicitud HTTP que realizó el cliente. Contiene información
    como el usuario que realiza la solicitud, el método utilizado (GET, POST, etc.) y cualquier dato que
    se haya enviado con la solicitud.
    id
        El parámetro id es el identificador único del objeto Solicitud que necesita ser editado.
    
    Returns
    -------
        una redirección a la URL de 'Solicitudes'.
    
    '''
    solicitud = get_object_or_404(Solicitud, id=id)
    # Actualizar el campo estadoSolicitud a "Aceptada"
    solicitud.estadoSolicitud = 'Rechazada'
    solicitud.save()
    return redirect('Solicitudes')