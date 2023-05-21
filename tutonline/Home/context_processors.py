from django.urls import resolve

def navbar(request):
    current_url = request.path_info
    resolved_url = resolve(current_url)
    url_name = resolved_url.url_name
    if url_name == 'inicio':
        navbar_items = ['Inicio', 'Clases', 'Registrarse', 'Iniciar sesión']
    elif url_name == 'clases':
        navbar_items = ['Otra vista', 'Otro enlace']
    else:
        navbar_items = []
    context = {
        'navbar_items': navbar_items,
    }
    return context
