from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout,get_user_model
from .forms import CustomUserCreationForm
from UsuarioApp.views import Perfil
# User = get_user_model()

# Create your views here.

def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    data = {
        'form' : CustomUserCreationForm()
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