from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Familiar, Curso, Estudiante, Profesor, Avatar
from .forms import CursoForm, EstudianteForm, ProfesorForm, UserEditForm, AvatarForm
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

# Create your views here.

@login_required
def editar_perfil(request):
    usuario = request.user
    
    # Intentamos obtener el avatar existente. Si no existe, es None.
    try:
        avatar = usuario.avatar
    except Avatar.DoesNotExist:
        avatar = None

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=usuario)
        # Pasamos el avatar existente (o None) como instancia
        avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)

        # Verificamos si ambos formularios son válidos
        if form.is_valid() and avatar_form.is_valid():
            # Guardamos los datos del usuario
            form.save()
            
            # Guardamos el avatar
            avatar_instance = avatar_form.save(commit=False)
            avatar_instance.user = usuario # Asignamos el usuario al avatar
            avatar_instance.save()

            messages.success(request, '¡Perfil actualizado correctamente!')
            return redirect('perfil')

    else: # Si es un método GET
        form = UserEditForm(instance=usuario)
        avatar_form = AvatarForm(instance=avatar)

    return render(request, 'mi_primer_app/editar-perfil.html', {'form': form, 'avatar_form': avatar_form})

@login_required
def inicio(request):
    # Agrega la ruta completa al template
    return render(request, 'mi_primer_app/inicio.html')



def perfil(request):
    return render(request, 'mi_primer_app/perfil.html')

def home(request):
    return render(request, 'mi_primer_app/home.html')

def about(request):
    return render(request, 'mi_primer_app/about.html')

def crear_familiar(request, nombre):
    if nombre is not None:
        Familiar.objects.create(
            nombre=nombre, edad=30, fecha_nacimiento="1991-01-01", parentesco="Hermano")
    return render(request, 'mi_primer_app/crear-familiar.html', {"familiar": nombre})


def listar_familiares(request):
    familiares = Familiar.objects.all()
    return render(request, 'mi_primer_app/listar-familiares.html', {"familiares": familiares})


def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = Curso(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                duracion_semanas=form.cleaned_data['duracion_semanas'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                fecha_fin=form.cleaned_data['fecha_fin'],
                activo=form.cleaned_data['activo']
            )
            curso.save()
            return redirect('listar-cursos')

    form = CursoForm()
    return render(request, 'mi_primer_app/crear-curso.html', {"form": form})


def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'mi_primer_app/listar-cursos.html', {"cursos": cursos})


def buscar_cursos(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/listar-cursos.html', {"cursos": cursos, "nombre": nombre})
    
# Vista para ver los detalles de un curso
def ver_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'mi_primer_app/ver_curso.html', {'curso': curso})

# Vista para editar un curso
def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar-cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'mi_primer_app/editar_curso.html', {'form': form})

# Vista para eliminar un curso
def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
    return redirect('listar-cursos')


def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            try:
                # Intenta guardar el nuevo estudiante
                form.save()
                return redirect('listar-estudiantes')
            except IntegrityError:
                # Si el email ya existe, añade un error al campo 'email' del formulario
                form.add_error('email', 'Este correo electrónico ya está registrado.')
    else:
        # Si la petición es GET (al cargar la página por primera vez), crea un formulario vacío
        form = EstudianteForm()
        
    # Renderiza la plantilla, pasándole el formulario (ya sea con datos y errores, o vacío)
    return render(request, 'mi_primer_app/crear-estudiante.html', {"form": form})

def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'mi_primer_app/listar-estudiantes.html', {"estudiantes": estudiantes})

# Vista para ver los detalles de un estudiante
def ver_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'mi_primer_app/ver_estudiante.html', {'estudiante': estudiante})

# Vista para editar un estudiante
def editar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('listar-estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'mi_primer_app/editar_estudiante.html', {'form': form})

def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
    return redirect('listar-estudiantes')

def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = Profesor(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                fecha_contratacion=form.cleaned_data['fecha_contratacion']
            )
            profesor.save()
            return redirect('listar-profesores')

    form = ProfesorForm()
    return render(request, 'mi_primer_app/crear-profesor.html', {"form": form})

def listar_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'mi_primer_app/listar-profesores.html', {"profesores": profesores})

def ver_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    return render(request, 'mi_primer_app/ver_profesor.html', {'profesor': profesor})

# Vista para editar un profesor
def editar_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('listar-profesores')
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'mi_primer_app/editar_profesor.html', {'form': form})

# Vista para eliminar un profesor
def eliminar_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        profesor.delete()
    return redirect('listar-profesores')

def logout_view(request):
    logout(request)
    return redirect('login')