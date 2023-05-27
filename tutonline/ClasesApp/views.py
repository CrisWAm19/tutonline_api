from django.shortcuts import render
from api.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def ListClases(request):
    clases = Clase.objects.all().select_related('rutProf')
    dataClases = {'clases' : clases}
    return render (request, 'ClasesTemplates/Clases.html', dataClases)

