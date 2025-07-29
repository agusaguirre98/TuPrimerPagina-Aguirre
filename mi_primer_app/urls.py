from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hola-mundo/', views.hola_mundo, name='hola-mundo'),
    path('crear-familiar/<str:nombre>/',
         views.crear_familiar, name='crear-familiar'),
    path('listar-familiares/', views.listar_familiares, name="listar-familiares"),
    path('crear-curso/',
         views.crear_curso, name='crear-curso'),
    path('listar-cursos/', views.listar_cursos, name="listar-cursos"),
    path('cursos/buscar', views.buscar_cursos, name="buscar-cursos"),
    path('crear-estudiante/',
         views.crear_estudiante, name='crear-estudiante'),
    path('listar-estudiantes/', views.listar_estudiantes,
         name="listar-estudiantes"),
     path('crear-profesor/', views.crear_profesor, name='crear-profesor'),
]
