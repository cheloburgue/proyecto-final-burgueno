from django.shortcuts import render
from .forms import RegistroUsuarioForm, AvatarForm, UserEditForm
from.models import Avatar
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 

# Create your views here.

def home(request):
    return render(request, "blogApp/home.html",{"avatar":obtenerAvatar(request)})

def acercaDeMi(request):
    mensaje = "Este es un mensaje acerca de mi"
    return render(request,"blogApp/acercaDeMi.html",{"mensaje":mensaje, "avatar":obtenerAvatar(request)})

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
                return render(request, "blogApp/inicio.html", {"formulario":form,"mensaje":"Usuario logueado correctamente!", "avatar":obtenerAvatar(request)})           
        else:
            return render(request,"blogApp/login.html", {"formulario":form,"mensaje":"Datos Invalidos", "avatar":obtenerAvatar(request)})    
    else:
        form = AuthenticationForm()
        return render(request, "blogApp/login.html",{"formulario":form, "avatar":obtenerAvatar(request)})
            
def register(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre_usuario = info["username"]
            form.save()
            return render(request, "blogApp/registerok.html", {"mensaje": f"Usuario {nombre_usuario} creado correctaente!. Por favor inicie sesión ingresando a Login.", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "blogApp/register.html", { "formulario": form, "mensaje": "Datos invalidos", "avatar":obtenerAvatar(request)})
    else:
        form = RegistroUsuarioForm()
        return render(request,"blogApp/register.html", {"formulario":form})

def obtenerAvatar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    print(f"len(avatares): {len(avatares)}")
    if len(avatares) != 0:
        return avatares[0].imagen.url
    else:
        return "/media/avatarpordefecto.png"
    
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info["email"]
            usuario.password1 = info["password1"]
            usuario.password2 = info["password2"]
            usuario.first_name = info["first_name"] 
            usuario.last_name = info["last_name"]
            usuario.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "AppCoder/editarPerfil.html",{"formulario":form, "nombreusuario":usuario.username, "mensaje":"Datos invalidos", "avatar":obtenerAvatar(request)})
    else:
        form = UserEditForm(instance=usuario)
        return render(request, "AppCoder/editarPerfil.html",{"formulario":form,"nombreusuario":usuario.username,"avatar":obtenerAvatar(request)})
    
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES) #Traigo request.FILES porque se que tiene archivos
        if form.is_valid():
            avatar = Avatar(user = request.user, imagen = request.FILES["imagen"]) #Antes de guardarlo tengo que hacer algo
            #Busco si ya tengo un avatar cargado y si tengo lo borro. De esta manera siempre tengo 1 solo avatar por usuario
            avatarViejo = Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0 :
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": f"Avatar agregado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "AppCoder/agregarAvatar.html",{"formulario":form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form = AvatarForm()
        return render(request, "AppCoder/agregarAvatar.html", {"formulario":form, "usuario": request.user, "avatar":obtenerAvatar(request)})
