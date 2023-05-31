from django.shortcuts import render, redirect
from api.models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

@login_required
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
            return redirect(ListClases)
        else: 
            data["form"] = form
    return render (request, 'ClasesTemplates/AgregarClase.html',data)

def AgendarClase(request):
    data = {'form': FormClaseAgendada(initial={'idProfesor': request.user.id})}
    if request.method == 'POST':
        form = FormClaseAgendada(data=request.POST)
        if form.is_valid():
            clase = form.save(commit=False)
            clase.idProfesor_id = request.user.id
            form.save()
            messages.success(request, "Clase agendada registrada")
            return redirect(ListClases)
        else: 
            data["form"] = form
    return render (request, 'ClasesTemplates/AgendarClase.html',data)
