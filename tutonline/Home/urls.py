from django.urls import path
from Home import views

urlpatterns = [
    path('inicio/',views.home, name='inicio')
]