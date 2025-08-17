from django.contrib import admin

# Register your models here.

from .models import Familiar, Curso, Estudiante, Profesor

admin.site.register(Familiar)
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)