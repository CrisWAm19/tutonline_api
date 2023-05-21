from django.shortcuts import render
from api.models import *
# Create your views here.

def ListClases(request):
    clases = Clase.objects.all().select_related('rutProf')
    dataClases = {'clases' : clases}
    return render (request, 'ClasesTemplates/Clases.html', dataClases)

