from django.shortcuts import render, HttpResponse,redirect, resolve_url, get_object_or_404
from api.models import User,Comentario,ClaseAgendada
from .forms import *
from UsuarioApp.views import calcular_anios_pasados, Perfil
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def ComentariosPerfilVisita(request, username=None):
    '''La función `ComentariosPerfilVisita` recupera y muestra comentarios relacionados con el perfil de un
    usuario, permite a los usuarios enviar nuevos comentarios y comprueba si un usuario tiene clases
    programadas con el propietario del perfil.
    
    Parameters
    ----------
    request
        El objeto de solicitud representa la solicitud HTTP realizada por el usuario.
    username
        El parámetro de nombre de usuario se utiliza para especificar el nombre de usuario del usuario cuyo
    perfil se visita. Si se proporciona el nombre de usuario y no es el mismo que el nombre de usuario
    del usuario actual, se recupera el objeto de usuario correspondiente a ese nombre de usuario. De lo
    contrario, se utiliza el objeto de usuario actual.
    
    Returns
    -------
        una plantilla HTML renderizada con los datos de contexto.
    
    '''
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user
    
    profesion = user.profesion.all()
    descripcion = user.descripcion.all()
    #recupera el comentario del usuario logeado
    comentario_current_user = Comentario.objects.filter(idProfesorReceptor=user, idEstudianteEmisor=current_user)
    #recupera todos los comentarios, excluyendo el del usuario logeado
    comentarios_otros = Comentario.objects.filter(idProfesorReceptor=user).exclude(idEstudianteEmisor=current_user)
    # Verificar si existe el comentario
    existe_comentario = Comentario.objects.filter(idEstudianteEmisor=current_user, idProfesorReceptor=user).exists()
    existe_clase_agendada = ClaseAgendada.objects.filter(idEstudiante=current_user, idProfesor=user).exists()
    
    #manda el formulario si es que el estudiante no ha realizado un comentario y si el estudiante
    #tiene alguna clase agendada con dicho tutor
    if not existe_comentario and existe_clase_agendada:
        data = {'form' : FormComentario}
        if request.method == 'POST':
            form = FormComentario(data=request.POST) #rellena formulario
            if form.is_valid():
                comentario = form.save(commit=False) # Obtener instancia del modelo sin guardarla aún
                comentario.idEstudianteEmisor = current_user  # Asignar valor al campo idEstudianteEmisor
                comentario.idProfesorReceptor = user
                form.save()
                current_url = resolve_url(request.path)
                return redirect(current_url)
            else: #si no es valido sobreescribe el form
                data["form"] = form

    context = {
        'user': user,
        'profesion': profesion,
        'descripcion': descripcion,
        'comentario_current_user': comentario_current_user,
        'comentarios_otros': comentarios_otros,
        'current_user': current_user,
        'existe_comentario':existe_comentario,
        'existe_clase_agendada':existe_clase_agendada,
        'form' : FormComentario,
    } 
    return render(request,"ComentariosTemplates/Comentarios.html",context)

@login_required
def ComentariosPerfilLogeado(request):
    '''La función "ComentariosPerfilLogeado" recupera comentarios, profesión y descripción relacionados con
    el usuario registrado y los presenta en una plantilla.
    
    Parameters
    ----------
    request
        El parámetro `request` es un objeto que representa la solicitud HTTP realizada por el usuario.
    Contiene información sobre la solicitud, como el usuario que realiza la solicitud, el método
    utilizado (GET, POST, etc.) y cualquier dato enviado con la solicitud.
    
    Returns
    -------
        una plantilla HTML renderizada con los datos de contexto.
    
    '''
    current_user = request.user.id
    comentarios = Comentario.objects.filter(idProfesorReceptor=current_user)
    profesion = Profesion.objects.filter(idProfesor_id=current_user)
    descripcion = Descripcion.objects.filter(idProfesor_id=current_user)
    def ObtenerAnios(request):
        profesion = Profesion.objects.filter(idProfesor=request.user.id).first()
        anio_egreso = profesion.anioEgreso if profesion else None
        anios_pasados = calcular_anios_pasados(anio_egreso) if anio_egreso else None
        return {'anios_pasados':anios_pasados}
    print(comentarios)
    context = {
        **ObtenerAnios(request),
        'comentarios':comentarios,
        'profesion':profesion,
        'descripcion':descripcion
    }
    return render(request,"ComentariosTemplates/ComentariosPerfilLog.html",context)

@login_required
def EditarComentario (request,id):
    '''La función `EditarComentario` se utiliza para editar un comentario recuperando el objeto de
    comentario, creando un formulario con los datos del comentario y guardando el comentario actualizado
    si el formulario es válido.
    
    Parameters
    ----------
    request
        El objeto de solicitud representa la solicitud HTTP realizada por el usuario. Contiene información
    como el navegador del usuario, la dirección IP y cualquier dato enviado con la solicitud.
    id
        El parámetro "id" es el identificador único del comentario que debe editarse. Se utiliza para
    recuperar el comentario específico de la base de datos.
    
    Returns
    -------
        una plantilla HTML renderizada llamada 'EditarComentario.html' con la variable de contexto que
    contiene el formulario.
    
    '''
    comentario = get_object_or_404(Comentario, id=id)
    form  = FormComentario(instance=comentario)
    if request.method == 'POST':
        form = FormComentario(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            current_url = resolve_url(request.path)
            return redirect(current_url)
        else:
            context = {'form': form }
    context = {
        'form': form
    }
    return render(request, 'ComentariosTemplates/EditarComentario.html', context)


@login_required
def EliminarComentario(request,id):
    '''La función "EliminarComentario" elimina un objeto de comentario con una identificación específica y
    redirige a la página "Perfil".
    
    Parameters
    ----------
    request
        El objeto de solicitud representa la solicitud HTTP que se realizó al servidor. Contiene
    información como la sesión del usuario, el método HTTP utilizado (GET, POST, etc.) y cualquier dato
    que se envió con la solicitud.
    id
        El parámetro id es el identificador único del comentario que debe eliminarse.
    
    Returns
    -------
        una redirección a la página "Perfil".
    
    '''
    comentario = Comentario.objects.get(id=id)
    comentario.delete()
    return redirect(Perfil)