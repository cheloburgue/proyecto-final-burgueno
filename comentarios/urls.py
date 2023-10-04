from django import views
from .views import ComentarioPagina
from django.urls import path

urlpatterns =[
path('detallePost/<pk>/comentario/',ComentarioPagina.as_view(),name='comentario'),
]