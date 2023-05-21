from django.urls import path
from ClasesApp import views

urlpatterns = [
    path('clases/',views.ListClases, name='clases')
]