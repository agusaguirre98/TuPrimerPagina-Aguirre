from django import forms
from .models import Estudiante, Profesor, Avatar, Curso
from django.contrib.auth.forms import UserCreationForm  , UserChangeForm
from django.contrib.auth.models import User

class UserEditForm(UserChangeForm):
    # Limpiamos los campos de contraseña del formulario base
    password = None 
    class Meta:
        model = User
        # Definimos explícitamente los campos que queremos en el formulario
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'
    fecha_contratacion = forms.DateField(
        widget=forms.SelectDateWidget, label='Fecha de Contratación')

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        # Cambiamos esto para que solo pida la imagen
        fields = ['imagen']