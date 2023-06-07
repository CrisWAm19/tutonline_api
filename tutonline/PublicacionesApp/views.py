from django.shortcuts import render, redirect, get_object_or_404
from api.models import *
from .forms import *
from django.contrib import messages
from UsuarioApp.views import Perfil
from django.shortcuts import render

# Create your views here.

def ListPublicaciones(request):
    publicaciones = Publicacion.objects.all().select_related('idEstudiante')
    dataPublicaciones = {'publicaciones' : publicaciones}
    return render (request, 'PublicacionTemplates/Publicaciones.html', dataPublicaciones)

def PublicacionEstudiante(request):
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

def EditarPublicacion(request,id):
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

def EliminarPublicacion(request,id):
    publicacion = Publicacion.objects.get(id=id)
    publicacion.delete()
    return redirect(Perfil)