from django.shortcuts import render, get_object_or_404
from .forms import RegistroUsuarioForm, AvatarForm, UserEditForm, AgregarPostForm, EditarPostForm
from.models import Avatar, AgregarPost
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from django.urls import reverse_lazy
from comentarios.models import Comentario

# Create your views here.

def home(request):
    return render(request, "blogApp/home.html",{"avatar":obtenerAvatar(request)})

def acercaDeMi(request):
    mensaje = "Este es un mensaje acerca de mi"
    return render(request,"blogApp/acercaDeMi.html",{"mensaje":mensaje,"avatar":obtenerAvatar(request)})

def login_request(request):
    usuario = request.user
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            info = form.cleaned_data
            user = info["username"]
            clave = info["password"]
            usuario = authenticate(username = user, password = clave)
            if usuario is not None:
                login(request,usuario)
                return render(request, "blogApp/inicio.html", {"formulario":form, "mensaje":f"Bienvenido {usuario.username}!", "avatar":obtenerAvatar(request)})           
        else:
            return render(request,"blogApp/login.html", {"formulario":form,"mensaje":"Datos Invalidos"})    
    else:
        form = AuthenticationForm()
        return render(request, "blogApp/login.html",{"formulario":form,"avatar":obtenerAvatar(request)})
            
def register(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre_usuario = info["username"]
            form.save()
            return render(request, "blogApp/registerok.html", {"mensaje": f"Usuario {nombre_usuario} creado correctamente! Para iniciar sesión ingrese a Login."})
        else:
            return render(request, "blogApp/register.html", { "formulario": form, "mensaje": "Datos invalidos", "avatar":obtenerAvatar(request)})
    else:
        form = RegistroUsuarioForm()
        return render(request,"blogApp/register.html", {"formulario":form})

def obtenerAvatar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if len(avatares) != 0:
        return avatares[0].imagen.url
    else:
        return "/media/avatar/avatarpordefecto.png"
    
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
            return render(request, "blogApp/inicio.html", {"mensaje": f"Avatar agregado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "blogApp/agregarAvatar.html",{"formulario":form, "usuario": request.user, "mensaje":"Error al agregar el avatar", "avatar":obtenerAvatar(request)})
    else:
        form = AvatarForm()
        return render(request, "blogApp/agregarAvatar.html", {"formulario":form, "usuario": request.user, "avatar":obtenerAvatar(request)})

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
            return render(request, "blogApp/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "blogApp/editarPerfil.html",{"formulario":form, "nombreusuario":usuario.username, "mensaje":"Datos invalidos","avatar":obtenerAvatar(request)})
    else:
        form = UserEditForm(instance=usuario)
        return render(request, "blogApp/editarPerfil.html",{"formulario":form,"nombreusuario":usuario.username, "avatar":obtenerAvatar(request)})
    
class UsuarioDetalle(DetailView):
    model = User
    template_name = "blogApp/perfil.html"


@login_required
def agregarPost(request):
    if request.method == "POST":
        form = AgregarPostForm(request.POST,request.FILES)
        if form.is_valid():
            titulo = request.POST["titulo"]
            descripcion = request.POST["descripcion"]
            imagen = request.FILES["imagen"]
            post = AgregarPost(user = request.user, titulo = titulo, descripcion = descripcion, imagen=imagen)
            post.save()
            return render(request, "blogApp/inicio.html", {"mensaje": f"Post agregado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "blogApp/agregarPost.html",{"formulario":form, "usuario": request.user, "mensaje":"Error al agregar Post", "avatar":obtenerAvatar(request)})
    else:
        form = AgregarPostForm()
        return render(request, "blogApp/agregarPost.html", {"formulario":form, "usuario": request.user, "avatar":obtenerAvatar(request)})  

@login_required
def misPost(request,user_id):
    user_post = AgregarPost.objects.filter(user_id = user_id)
    mensaje = ""
    if len(user_post) < 1:
        mensaje = "No tienes Post cargados!"
    return render(request,"blogApp/misPost.html",{"mensaje":mensaje, "user_post":user_post,"avatar":obtenerAvatar(request)})

def listar_post(request):
    mensaje = ""
    user_post = AgregarPost.objects.all()
    if len(user_post) < 1:
        mensaje = "No hay Post cargados!"
    return render(request,"blogApp/misPost.html",{"mensaje":mensaje,"user_post":user_post,"avatar":obtenerAvatar(request)})

def detallePost(request,id):
   post = get_object_or_404(AgregarPost,id=id)
   return render(request,"blogApp/detallePost.html",{"post":post,"avatar":obtenerAvatar(request)})

@login_required
def eliminarPost(request,id):
    post = AgregarPost.objects.get(id=id)
    return render(request, "blogApp/eliminarPost.html", {"post":post,"avatar":obtenerAvatar(request)})

@login_required
def confirmarEliminarPost(request,id):
    post = AgregarPost.objects.get(id=id)
    post.delete()
    mensaje = "Publicacion Elimiada!"
    return render(request, "blogApp/confirmarEliminarPost.html", {"mensaje": mensaje,"avatar":obtenerAvatar(request)})

@login_required
def editarPost(request,id):
    posting = get_object_or_404(AgregarPost,id=id)
    posting.delete()
    posting.save()
    if request.method == "POST":
        form = EditarPostForm(request.POST,request.FILES, instance =posting)
        if form.is_valid():
            titulo = request.POST["titulo"]
            descripcion = request.POST["descripcion"]
            imagen = request.FILES["imagen"]
            post = AgregarPost( id = posting.id, titulo = titulo, descripcion = descripcion, imagen=imagen, user_id = posting.user_id)
            post.save()
            return render(request, "blogApp/confirmaEdicion.html", {"mensaje": f"Post editado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "blogApp/editarPost.html",{"form":form, "mensaje":"Error al editar Post", "avatar":obtenerAvatar(request)})
    else:
        form = EditarPostForm()
        return render(request, "blogApp/editarPost.html", {"form":form,"post":posting,"avatar":obtenerAvatar(request)}) 
    
def listar_comentarios(request,id):
    comentarios = Comentario.objects.filter(comentario_id=id)
    posts = AgregarPost.objects.filter(id=id)
    return render(request,"blogApp/detallePostComentario.html",{"comentarios":comentarios,"posts":posts, "avatar":obtenerAvatar(request)})

    

