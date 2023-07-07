from django.shortcuts import render,redirect, get_object_or_404
from api.models import *
from datetime import date
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def calcular_anios_pasados(anio):
    '''La función calcula el número de años que han pasado desde un año determinado.
    
    Parameters
    ----------
    anio
        El parámetro "año" es un objeto de fecha que representa un año específico.
    
    Returns
    -------
        el número de años que han pasado desde el año de entrada.
    
    '''
    anio_actual = date.today().year
    anios_pasados = anio_actual - anio.year
    return anios_pasados

@login_required
def Perfil(request):
    '''La función "Perfil" recupera información sobre la profesión de un usuario, años desde la graduación,
    descripción, clases y publicaciones, y la presenta en una plantilla llamada "Perfil.html".
    
    Parameters
    ----------
    request
        El parámetro `request` es un objeto que representa la solicitud HTTP realizada por el usuario.
    Contiene información como la sesión del usuario, la URL solicitada y cualquier dato enviado con la
    solicitud.
    
    Returns
    -------
        a rendered HTML template called 'Perfiles/Perfil.html' with a context dictionary containing the
    following variables: 'profesion', 'anios_pasados', 'descripcion', 'clases', and 'publicaciones'.
    
    '''
    user_id = request.user.id
    
    profesion = Profesion.objects.filter(idProfesor_id=user_id)
    anio_egreso = profesion.first().anioEgreso if profesion else None
    anios_pasados = calcular_anios_pasados(anio_egreso) if anio_egreso else None
    
    descripcion = Descripcion.objects.filter(idProfesor_id=user_id)
    clases = Clase.objects.filter(idProfesor_id=user_id)
    publicaciones = Publicacion.objects.filter(idEstudiante_id=user_id)
    
    context = {
        'profesion': profesion,
        'anios_pasados': anios_pasados,
        'descripcion': descripcion,
        'clases': clases,
        'publicaciones': publicaciones
    }
    return render(request, 'Perfiles/Perfil.html', context)

def PerfilTutor(request, username=None):
    '''La función `PerfilTutor` recupera información sobre la profesión, descripción y clases de un tutor,
    y la presenta en una plantilla.
    
    Parameters
    ----------
    request
        El objeto de solicitud representa la solicitud HTTP realizada por el cliente. Contiene información
    sobre la solicitud, como el método (GET, POST, etc.), los encabezados y la sesión del usuario.
    username
        El parámetro de nombre de usuario es un parámetro opcional que le permite especificar el perfil de
    un usuario específico para mostrar. Si se proporciona un nombre de usuario y no es el mismo que el
    nombre de usuario del usuario que ha iniciado sesión actualmente, la función recupera el objeto de
    usuario con el nombre de usuario especificado. De lo contrario, utiliza el usuario conectado
    actualmente
    
    Returns
    -------
        una plantilla HTML renderizada llamada 'PerfilTutor.html' con los datos de contexto.
    
    '''
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user
    profesion = user.profesion.all()
    descripcion = user.descripcion.all()
    clase = user.clase.all()
    context = {
        'user': user,
        'profesion': profesion,
        'descripcion': descripcion,
        'clase': clase,
        'current_user': current_user
    } 
    return render(request, 'Perfiles/PerfilTutor.html', context)


def PerfilEstudiante(request, username=None):
    '''La función `PerfilEstudiante` recupera la información del perfil y las publicaciones de un usuario,
    y renderiza una plantilla con el perfil y las publicaciones del usuario.
    
    Parameters
    ----------
    request
        El objeto de solicitud representa la solicitud HTTP realizada por el usuario. Contiene información
    como la sesión del usuario, la URL solicitada y cualquier dato enviado con la solicitud.
    username
        El parámetro de nombre de usuario se utiliza para especificar el nombre de usuario del usuario a
    cuyo perfil se accede. Si se proporciona el parámetro de nombre de usuario y no es el mismo que el
    nombre de usuario del usuario actual, el código recupera el objeto de usuario con el nombre de
    usuario especificado mediante el método User.objects.get(). De lo contrario, utiliza
    
    Returns
    -------
        una plantilla HTML renderizada llamada 'PerfilEstudiante.html' con las variables de contexto
    'user', 'publicaciones' y 'current_user'.
    
    '''
    current_user = request.user

    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user

    publicaciones = user.publicacion.all()

    context = {
        'user': user,
        'publicaciones': publicaciones,
        'current_user': current_user
    }

    return render(request, 'Perfiles/PerfilEstudiante.html', context)

@login_required
def ProfesionTutor(request):
    '''La función "ProfesionTutor" es una función de vista en Python que maneja una solicitud para crear
    una profesión para un tutor y guarda los datos en la base de datos.
    
    Parameters
    ----------
    request
        El parámetro "solicitud" es un objeto que representa la solicitud HTTP realizada por el usuario.
    Contiene información como la sesión del usuario, el método HTTP utilizado (GET, POST, etc.) y
    cualquier dato enviado con la solicitud.
    
    Returns
    -------
        una plantilla HTML renderizada llamada 'Perfiles/Profesion.html' con el diccionario de datos como
    contexto.
    
    '''
    data = {'form': FormProfesion(initial={'idProfesor': request.user,'tituloValidado':"En Proceso"})}
    if request.method == 'POST':
        form = FormProfesion(data=request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.idProfesor = request.user
            form.save()
            return redirect(Perfil)
        else: 
            data["form"] = form
    return render (request, 'Perfiles/Profesion.html',data)

@login_required
def EditarProfesion(request):
    '''La función "EditarProfesión" se utiliza para editar la profesión de un usuario y guardar los cambios
    en la base de datos.
    
    Parameters
    ----------
    request
        El objeto de solicitud contiene información sobre la solicitud HTTP actual, como el usuario que
    realiza la solicitud, el método utilizado (GET o POST) y cualquier dato enviado con la solicitud.
    
    Returns
    -------
        una plantilla HTML renderizada llamada 'EditarProfesion.html' con una variable de contexto
    'formulario'.
    
    '''
    profesion = Profesion.objects.filter(idProfesor=request.user).first()
    if request.method == 'POST':
        form = FormProfesion(request.POST, instance=profesion)
        if form.is_valid():
            form.save()
            return redirect(Perfil)
    else:
        form = FormProfesion(instance=profesion)
    context = {
        'form': form
    }
    return render(request, 'Perfiles/EditarProfesion.html', context)


