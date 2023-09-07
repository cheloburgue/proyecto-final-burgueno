from django.shortcuts import render
from .forms import RegistroUsuarioForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 

# Create your views here.

def home(request):
    return render(request, "blogApp/home.html")

def acercaDeMi(request):
    mensaje = "Este es un mensaje acerca de mi"
    return render(request,"blogApp/acercaDeMi.html",{"mensaje":mensaje})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            info = form.cleaned_data
            user = info["username"]
            clave = info["password"]
            usuario = authenticate(username = user, password = clave)
            if usuario is not None:
                login(request,usuario)
                return render(request, "blogApp/inicio.html", {"formulario":form,"mensaje":"Usuario logueado correctamente!"})           
        else:
            return render(request,"blogApp/login.html", {"formulario":form,"mensaje":"Datos Invalidos"})    
    else:
        form = AuthenticationForm()
        return render(request, "blogApp/login.html",{"formulario":form})
            
def register(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre_usuario = info["username"]
            form.save()
            return render(request, "blogApp/registerok.html", {"mensaje": f"Usuario {nombre_usuario} creado correctaente!. Por favor inicie sesión ingresando a Login."})
        else:
            return render(request, "blogApp/register.html", { "formulario": form, "mensaje": "Datos invalidos"})
    else:
        form = RegistroUsuarioForm()
        return render(request,"blogApp/register.html", {"formulario":form})
