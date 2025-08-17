from django.urls import path
from . import views
# Importamos las vistas de login y logout de Django
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
# Al entrar a la raíz del sitio (''), se muestra la vista de login
    path('', LoginView.as_view(template_name='mi_primer_app/login.html'), name='login'),
    
    # La página de bienvenida ahora está en /inicio/
    path('inicio/', views.inicio, name='inicio'),

# Cambiamos esta línea para que apunte a nuestra nueva vista
    path('logout/', views.logout_view, name='logout'),
    path('crear-familiar/<str:nombre>/',
         views.crear_familiar, name='crear-familiar'),
    path('listar-familiares/', views.listar_familiares, name="listar-familiares"),
    path('crear-curso/',
         views.crear_curso, name='crear-curso'),
    path('listar-cursos/', views.listar_cursos, name="listar-cursos"),
    path('cursos/buscar', views.buscar_cursos, name="buscar-cursos"),
    path('curso/<int:pk>/', views.ver_curso, name='ver-curso'),
    path('curso/<int:pk>/editar/', views.editar_curso, name='editar-curso'),
    path('curso/<int:pk>/eliminar/', views.eliminar_curso, name='eliminar-curso'),

    path('crear-estudiante/',
         views.crear_estudiante, name='crear-estudiante'),
    path('listar-estudiantes/', views.listar_estudiantes,
         name="listar-estudiantes"),
     path('estudiante/<int:pk>/', views.ver_estudiante, name='ver-estudiante'),
    path('estudiante/<int:pk>/editar/', views.editar_estudiante, name='editar-estudiante'),
    path('estudiante/<int:pk>/eliminar/', views.eliminar_estudiante, name='eliminar-estudiante'),

     path('crear-profesor/', views.crear_profesor, name='crear-profesor'),
     path('listar-profesores/', views.listar_profesores, name='listar-profesores'),
         path('profesor/<int:pk>/', views.ver_profesor, name='ver-profesor'),
    path('profesor/<int:pk>/editar/', views.editar_profesor, name='editar-profesor'),
    path('profesor/<int:pk>/eliminar/', views.eliminar_profesor, name='eliminar-profesor'),

     path('perfil/', views.perfil, name='perfil'),
     path('editar-perfil/', views.editar_perfil, name='editar-perfil'),
     path('about/', views.about, name='about')
]