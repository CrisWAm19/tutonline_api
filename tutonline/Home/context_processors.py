from django.urls import resolve
from django.urls import reverse

def navbar(request):
    current_url = request.path_info
    resolved_url = resolve(current_url)
    url_name = resolved_url.url_name
    if url_name == 'inicio' or url_name == 'clases' or url_name == 'Perfil' or url_name == 'Agregar clases':
        if request.user.is_authenticated:
            navbar_items = {
                'Inicio': reverse('inicio'),
                'Clases': reverse('clases'),
                'Perfil': reverse('Perfil'),
                'Cerrar sesión': reverse('logout')
            }
        else:
            navbar_items = {
                'Inicio': reverse('inicio'),
                'Clases': reverse('clases'),
                'Iniciar sesión': reverse('login'),
                'Registrarse': reverse('register'),
        }
    elif url_name == 'profesor':
        navbar_items = {
            'Inicio': reverse('inicio'),
            'Publicaciones': reverse('publicaciones'),
        }
    else:
        navbar_items = {}
    context = {
        'navbar_items': navbar_items,
    }
    return context
