from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns =[
    path("",listar_post, name = "home"),
    path("acercaDeMi/",acercaDeMi ,name="acercaDeMi"),

    # LOGIN LOGOUT REGISTER

    path("login/", login_request, name="login"),
    path("register/", register, name="register"),
    path("logout/", LogoutView.as_view(),name="logout"),
    path("perfil/<pk>", UsuarioDetalle.as_view(), name="perfil"),
    path("editarPerfil/", editarPerfil, name="editarPerfil"),
    path("agregarAvatar/", agregarAvatar, name = "agregarAvatar"),
    path("misPost/<int:user_id>/",misPost, name = "misPost"),
    path("agregarPost/", agregarPost, name = "agregarPost"), 
    path("detallePost/<id>/", detallePost, name = "detallePost"),
    path("detallePostComentario/<id>", listar_comentarios, name = "comentarios"),
    path("eliminarPost/<id>/", eliminarPost, name = "eliminarPost"),
    path("confirmarEliminarPost/<id>/", confirmarEliminarPost, name = "confirmarEliminarPost"),
    path("editarPost/<id>/", editarPost, name = "editarPost"),
] 

