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
    publicaciones = Publicacion.objects.all().select_related('idEstudiante')
    dataPublicaciones = {'publicaciones' : publicaciones}
    return render (request, 'PublicacionTemplates/Publicaciones.html', dataPublicaciones)

@login_required
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

@login_required
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

@login_required
def EliminarPublicacion(request,id):
    publicacion = Publicacion.objects.get(id=id)
    publicacion.delete()
    return redirect(Perfil)

@login_required
def ResponderPublicacion(request, username=None):
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
        email = EmailMessage("Mensaje de tutOnline",
            "El usuario {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre, correoRemitente, contenido), '',
            [email],
            reply_to=[email])
        try:
           email.send()
           return redirect(reverse('Perfil') + '?valido')
        except:
           return redirect(reverse('Perfil') + '?novalido')
        
    return render(request, 'ClasesTemplates/Correo.html', {'miFormulario':formulario,'user':user,'publicacion':publicacion, 'currentUser':currentUser})