from django import forms 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

from .models import AgregarPost



class RegistroUsuarioForm(UserCreationForm):
    email = forms.CharField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        help_texts = { k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Imagen")


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Email Usuario")
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Modificar Nombre")
    last_name = forms.CharField(label="Mofificar Apellido")

    class Meta:
        model = User
        fields = ["email","password1","password2","first_name","last_name"]
        help_texts = { k:"" for k in fields} 

class AgregarPostForm(forms.ModelForm):

        user = forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'})
        titulo = forms.TextInput(attrs={'class': 'form-control'})
        descripcion = forms.CharField(widget=forms.Textarea)
        imagen = forms.ImageField(label="Imagen")

        class Meta:
            model = AgregarPost 
            fields = ['titulo','descripcion','imagen']
