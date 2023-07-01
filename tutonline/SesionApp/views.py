from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from UsuarioApp.views import Perfil
from django.contrib.auth.decorators import login_required


# Create your views here.
def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    data = {
        'form' : CustomUserCreationForm(),
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        print(user_creation_form)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect(Perfil)
    return render(request, 'registration/register.html',data)

@login_required
def EditarPerfil(request):
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
