from django.urls import path
from SesionApp import views

urlpatterns = [
    path('logout/',views.exit, name='exit'),
    path('register/',views.register, name='register')
]