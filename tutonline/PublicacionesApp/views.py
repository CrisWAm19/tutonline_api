from django.shortcuts import render, redirect, get_object_or_404
from api.models import *
from .forms import *
from django.contrib import messages
from UsuarioApp.views import Perfil
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ClasesApp.forms import FormularioContacto
from django.core.mail import EmailMessage
from django.urls import reverse
# Create your views here.

def ListPublicaciones(request):
    '''La función ListPublicaciones recupera todas las publicaciones de la base de datos y las representa
    en la plantilla Publicaciones.html.
    
    Parameters
    ----------
    request
        El objeto de solicitud representa la solicitud HTTP que el servidor recibe del cliente. Contiene
    información sobre la solicitud, como el método HTTP (GET, POST, etc.), encabezados y cualquier dato
    enviado con la solicitud.
    
    Returns
    -------
        una plantilla HTML renderizada llamada 'Publicaciones.html' con una variable de contexto
    'dataPublicaciones' que contiene un conjunto de consulta de todos los objetos Publicación y sus
    objetos Estudiante relacionados.
    
    '''
    publicaciones = Publicacion.objects.all().select_related('idEstudiante')
    dataPublicaciones = {'publicaciones' : publicaciones}
    return render (request, 'PublicacionTemplates/Publicaciones.html', dataPublicaciones)

@login_required
def PublicacionEstudiante(request):
    '''La función "PublicaciónEstudiante" es una función de vista en Python que maneja la creación de una
    publicación por parte de un estudiante, con la validación del formulario y el guardado de la
    publicación en la base de datos.
    
    Parameters
    ----------
    request
        El objeto de solicitud representa la solicitud HTTP que el usuario realizó para acceder a la vista.
    Contiene información como la sesión del usuario, el método HTTP utilizado (GET o POST) y cualquier
    dato enviado en la solicitud.
    
    Returns
    -------
        una plantilla HTML renderizada llamada 'AgregarPublicación.html' con el diccionario de datos como
    contexto.
    
    '''
    data = {'form': FormPublicacion(initial={'idEstudiante': request.user.id})}
    if request.method == 'POST':
        form = FormPublicacion(data=request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.idEstudiante_id = request.user.id
            form.save()
            messages.success(request, "Publicacion registrada")
            return redirect(Perfil)
        else: 
            data["form"] = form
    return render (request, 'PublicacionTemplates/AgregarPublicacion.html',data)

@login_required
def EditarPublicacion(request,id):
    '''La función EditarPublicación toma una solicitud y una identificación como parámetros, recupera un
    objeto Publicación con la identificación dada, crea una instancia de formulario con el objeto
    recuperado y, si el método de solicitud es POST, actualiza el formulario con los datos enviados y lo
    guarda. luego redirige a la vista de Perfil, de lo contrario renderiza la plantilla
    EditarPublicación.html con el formulario.
    
    Parameters
    ----------
    request
        El objeto de solicitud representa la solicitud HTTP que el usuario realizó para acceder a la vista.
    Contiene información como la sesión del usuario, el método HTTP utilizado (GET o POST) y cualquier
    dato enviado con la solicitud.
    id
        El parámetro "id" es el identificador único de la publicación (publicación) que el usuario desea
    editar. Se utiliza para recuperar el objeto de publicación específico de la base de datos.
    
    Returns
    -------
        una plantilla HTML renderizada llamada 'EditarPublicación.html' con la variable de contexto que
    contiene el formulario.
    
    '''
    publicacion = get_object_or_404(Publicacion, id=id)
    form  = FormPublicacion(instance=publicacion)
    if request.method == 'POST':
        form = FormPublicacion(request.POST, instance=publicacion) #instance rellena el formulario
        if form.is_valid():
            form.save()
            return redirect(Perfil)
        else:
            context = {'form': form }
    context = {
        'form': form
    }
    return render(request, 'PublicacionTemplates/EditarPublicacion.html', context)

@login_required
def EliminarPublicacion(request,id):
    '''La función "EliminarPublicacion" borra un objeto de publicación específico y redirige a la página
    "Perfil".
    
    Parameters
    ----------
    request
        El objeto de solicitud representa la solicitud HTTP que el usuario realizó para acceder a la vista.
    Contiene información como la sesión del usuario, el método HTTP utilizado (GET, POST, etc.) y
    cualquier dato enviado con la solicitud.
    id
        El parámetro id es el identificador único de la publicación (publicación) que debe eliminarse.
    
    Returns
    -------
        una redirección a la página "Perfil".
    
    '''
    publicacion = Publicacion.objects.get(id=id)
    publicacion.delete()
    return redirect(Perfil)

@login_required
def ResponderPublicacion(request, username=None):
    '''La función `ResponderPublicación` es una función de vista en Python que maneja la lógica para
    responder a una publicación y enviar un correo electrónico al destinatario.
    
    Parameters
    ----------
    request
        El parámetro `request` es un objeto que representa la solicitud HTTP realizada por el usuario.
    Contiene información como la sesión del usuario, el método HTTP utilizado (GET, POST, etc.) y
    cualquier dato enviado con la solicitud.
    username
        El parámetro `username` se utiliza para especificar el nombre de usuario de un usuario. Es un
    parámetro opcional y se utiliza para filtrar las publicaciones del usuario si el nombre de usuario
    proporcionado es diferente del nombre de usuario del usuario que ha iniciado sesión actualmente.
    
    Returns
    -------
        una plantilla HTML renderizada llamada 'Correo.html' con las siguientes variables de contexto:
    'miFormulario', 'usuario', 'publicación' y 'currentUser'.
    
    '''
    currentUser = request.user
    correoRemitente = currentUser.email
    nombreRemitente = f"{currentUser.first_name} {currentUser.last_name}"
    user = None
    publicacion = None
    if username and username != currentUser.username:
        user = User.objects.get(username=username)
        publicacion = user.publicacion.all()
        correoReceptor = user.email

    formulario = FormularioContacto(data=request.POST) 
    if formulario.is_valid():
        nombre = nombreRemitente
        email = correoReceptor
        contenido = request.POST.get("contenido")
        email = EmailMessage("TutOnline",
            "{} te ha ofrecido sus clases.\n\n {}. \nPuedes responderle en el siguiente correo: {}".format(nombre, contenido , correoRemitente), '',
            [email],
            reply_to=[email])
        try:
           email.send()
           return redirect(reverse('Perfil') + '?valido')
        except:
           return redirect(reverse('Perfil') + '?novalido')
        
    return render(request, 'ClasesTemplates/Correo.html', {'miFormulario':formulario,'user':user,'publicacion':publicacion, 'currentUser':currentUser})