from django.shortcuts import render
from django.http import HttpResponse
from . import context_processors
# Create your views here.

def inicio(request):
    return render(request, 'HomeTemplates/Inicio.html')
