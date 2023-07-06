from django.shortcuts import render,redirect, get_object_or_404
from api.models import *
from datetime import date
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def calcular_anios_pasados(anio):
    anio_actual = date.today().year
    anios_pasados = anio_actual - anio.year
    return anios_pasados

@login_required
def Perfil(request):
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


def ProfesionTutor(request):
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

# def EditarProfesion(request,codigoVerificador):
#     profesion = get_object_or_404(Profesion, codigoVerificador=codigoVerificador)
#     form  = FormProfesion(instance=profesion)
#     if request.method == 'POST':
#         form = FormProfesion(request.POST, instance=profesion) #instance rellena el formulario
#         if form.is_valid():
#             form.save()
#             return redirect(Perfil)
#         else:
#             data = {'form': form }
#     data = {
#         'form': form
#     }
#     return render (request, 'Perfiles/EditarProfesion.html',data)
def EditarProfesion(request):
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


