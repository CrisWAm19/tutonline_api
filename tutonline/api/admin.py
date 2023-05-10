# from django.contrib import admin
# from .models import *
# # Register your models here.

# admin.site.register(Administrador)

from django.contrib import admin
from .models import *

# Obtener todos los modelos de la aplicación
modelos = [model for model in vars().values() if isinstance(model, type)]

# Registrar todos los modelos en el admin
for modelo in modelos:
    admin.site.register(modelo)
