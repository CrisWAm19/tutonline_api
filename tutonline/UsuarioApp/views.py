from django.shortcuts import render
from api.models import *
# Create your views here.

def Perfil(request):
    return render(request,'Perfiles/PerfilTutor.html')