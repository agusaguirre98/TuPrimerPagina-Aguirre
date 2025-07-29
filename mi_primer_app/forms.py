from django import forms


class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del Curso')
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción')
    duracion_semanas = forms.IntegerField(label='Duración (semanas)')
    fecha_inicio = forms.DateField(
        widget=forms.SelectDateWidget, label='Fecha de Inicio')
    fecha_fin = forms.DateField(
        widget=forms.SelectDateWidget, label='Fecha de Fin')
    activo = forms.BooleanField(
        required=False, initial=True, label='Activo')  # Campo opcional


class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    apellido = forms.CharField(max_length=100, label='Apellido')
    email = forms.EmailField(label='Email')
    edad = forms.IntegerField(label='Edad')

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    apellido = forms.CharField(max_length=100, label='Apellido')
    email = forms.EmailField(label='Email')
    fecha_contratacion = forms.DateField(
        widget=forms.SelectDateWidget, label='Fecha de Contratación')