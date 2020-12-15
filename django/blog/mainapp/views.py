from django.shortcuts import render, redirect
# Formulario por defecto de Django
from django.contrib.auth.forms import UserCreationForm
# Mensajes flash
from django.contrib import messages
# Importar del módulo de formularios
from mainapp.forms import FormularioRegistro
# Importar módulo de autenticación
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html', {
        'titulo': 'Inicio'
    })

def about(request):
    return render(request, 'mainapp/about.html', {
        'titulo': 'Sobre mí'
    })

def registro(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        formulario_registro = FormularioRegistro()

        if request.method == 'POST':
            # Pasar los datos del formulario enviado
            formulario_registro = FormularioRegistro(request.POST)
            
            if formulario_registro.is_valid():
                formulario_registro.save()
                # Crear mensaje flash
                messages.success(request, 'Usuario registrado correctamente')

                return redirect('login')

        return render(request, 'usuarios/registro.html', {
            'titulo': 'Registro',
            'formulario_registro': formulario_registro
        })

def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            # Recoger los datos del formulario
            username = request.POST.get('username')
            password = request.POST.get('password')

            usuario = authenticate(request, username=username, password=password)

            # Si la autenticación es correcta
            if usuario is not None:
                # Crear la sesión de usuario
                login(request, usuario)
                return redirect('home')
            else:
                # Crear mensaje flash
                messages.error(request, 'No te has identificado correctamente')

        return render(request, 'usuarios/login.html', {
            'titulo': 'Identifícate'
        })

def cerrar_sesion(request):
    logout(request)
    return redirect('login')