from django.shortcuts import render, HttpResponse,redirect, resolve_url
from api.models import User,Comentario,ClaseAgendada
from .forms import *
# Create your views here.

def ComentariosPerfilVisita(request, username=None):
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


def ComentariosPerfilLogeado(request):
    current_user = request.user.id
    comentarios = Comentario.objects.filter(idProfesorReceptor=current_user)
    profesion = Profesion.objects.filter(idProfesor_id=current_user)
    descripcion = Descripcion.objects.filter(idProfesor_id=current_user)
    print(comentarios)
    context = {
        'comentarios':comentarios,
        'profesion':profesion,
        'descripcion':descripcion
    }
    return render(request,"ComentariosTemplates/ComentariosPerfilLog.html",context)