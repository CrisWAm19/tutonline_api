from django.shortcuts import render, redirect
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
