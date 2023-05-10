from django.urls import path
from .views import *


urlpatterns = [
    path('profesores/', ProfesorView.as_view(),name='profesores_list'),
    path('profesores/<str:rutProf', ProfesorView.as_view(),name='profesores_process'),
    path('estudiantes/', ProfesorView.as_view(),name='estudiantes_list'),
    path('estudiantes/<str:rutEst>', ProfesorView.as_view(),name='estudiantes_list'),
]