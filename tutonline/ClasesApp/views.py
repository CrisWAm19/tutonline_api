from django.shortcuts import render, redirect, get_object_or_404
from api.models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from UsuarioApp.views import Perfil

# Create your views here.

# @login_required
def ListClases(request):
    clases = Clase.objects.all().select_related('idProfesor')
    dataClases = {'clases' : clases}
    return render (request, 'ClasesTemplates/Clases.html', dataClases)

def AgregarClase(request):
    data = {'form': FormClase(initial={'idProfesor': request.user.id})}
    if request.method == 'POST':
        form = FormClase(data=request.POST)
        if form.is_valid():
            clase = form.save(commit=False)
            clase.idProfesor_id = request.user.id
            form.save()
            messages.success(request, "Clase Registrada")
            return redirect(Perfil)
        else: 
            data["form"] = form
    return render (request, 'ClasesTemplates/AgregarClase.html',data)

def ListaClasesAgendadas(request):
    user_id = request.user.id
    clasesAgendadas = ClaseAgendada.objects.filter(idProfesor_id=user_id)
    dataClaseAgendada = {'clasesAgendadas':clasesAgendadas}
    return render(request,'ClasesTemplates/ClasesAgendadas.html',dataClaseAgendada)

def AgendarClase(request):
    data = {'form': FormClaseAgendada(initial={'idProfesor': request.user.id})}
    if request.method == 'POST':
        form = FormClaseAgendada(data=request.POST)
        if form.is_valid():
            clase = form.save(commit=False)
            clase.idProfesor_id = request.user.id
            form.save()
            messages.success(request, "Clase agendada registrada")
            return redirect(Perfil)
        else: 
            data["form"] = form
    return render (request, 'ClasesTemplates/AgendarClase.html',data)

def EditarClase(request,id):
    clase = get_object_or_404(Clase, id=id)
    form  = FormClase(instance=clase)
    if request.method == 'POST':
        form = FormClase(request.POST, instance=clase)
        if form.is_valid():
            form.save()
            return redirect(Perfil)
        else:
            context = {'form': form }
    context = {
        'form': form
    }
    return render(request, 'registration/update.html', context)

def EliminarClase(request,id):
    clase = Clase.objects.get(id=id)
    clase.delete()
    return redirect(Perfil)