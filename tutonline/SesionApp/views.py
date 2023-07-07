from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from UsuarioApp.views import Perfil
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required
def exit(request):
    '''La función cierra la sesión del usuario y lo redirige a la página de inicio.
    
    Parameters
    ----------
    request
        El parámetro `request` es un objeto que representa la solicitud HTTP realizada por el usuario.
    Contiene información sobre la solicitud, como la URL, los encabezados y cualquier dato enviado con
    la solicitud. En este fragmento de código, el parámetro `request` se usa para cerrar la sesión del
    usuario y luego redirigirlo
    
    Returns
    -------
        una redirección a la página de 'inicio'.
    
    '''
    logout(request)
    return redirect('home')

def register(request):
    '''La función `registrar` maneja el registro de usuarios mediante la validación de los datos del
    formulario, la creación de un nuevo usuario, la autenticación del usuario y la redirección a la
    página de perfil del usuario.
    
    Parameters
    ----------
    request
        El objeto de solicitud representa la solicitud HTTP que el usuario realizó al servidor. Contiene
    información como los detalles del navegador del usuario, la URL solicitada y cualquier dato enviado
    con la solicitud.
    
    Returns
    -------
        una plantilla HTML renderizada llamada 'register.html' con el diccionario de datos como contexto.
    
    '''
    data = {
        'form' : CustomUserCreationForm(),
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect(Perfil)
        else:
            data['form'] = user_creation_form
    return render(request, 'registration/register.html',data)

@login_required
def EditarPerfil(request):
    '''La función "EditarPerfil" se utiliza para actualizar la información del perfil del usuario mediante
    un formulario.
    
    Parameters
    ----------
    request
        El objeto de solicitud representa la solicitud HTTP realizada por el usuario. Contiene información
    como la sesión del usuario, el método HTTP utilizado (GET, POST, etc.) y cualquier dato enviado con
    la solicitud.
    
    Returns
    -------
        una plantilla HTML renderizada llamada 'update.html' con una variable de contexto que contiene un
    formulario.
    
    '''
    user = request.user
    if request.method == 'POST':
        form = FormActualizarPerfil(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(Perfil)
    else:
        form = FormActualizarPerfil(instance=user)
    context = {
        'form': form
    }
    return render(request, 'registration/update.html', context)
