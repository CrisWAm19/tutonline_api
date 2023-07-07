from django.shortcuts import render
from django.http import HttpResponse
from . import context_processors
# Create your views here.

def home(request):
    '''La función "inicio" devuelve una plantilla HTML renderizada llamada "inicio.html" cuando se realiza
    una solicitud.
    
    Parameters
    ----------
    request
        El parámetro `request` es un objeto que representa la solicitud HTTP realizada por el cliente.
    Contiene información sobre la solicitud, como el método HTTP (GET, POST, etc.), encabezados y
    cualquier dato enviado con la solicitud. Por lo general, se pasa para ver funciones en Django para
    manejar la solicitud
    
    Returns
    -------
        la plantilla renderizada 'home.html'.
    
    '''
    return render(request, 'HomeTemplates/home.html')
