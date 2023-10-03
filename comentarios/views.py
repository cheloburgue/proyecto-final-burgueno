from django.shortcuts import render
from django.views.generic import  CreateView
from .forms import FormularioComentario
from .models import Comentario
from django.urls import reverse_lazy
from blogApp.views import obtenerAvatar

# Create your views here.

class ComentarioPagina(CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'comentarios/comentario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        resultado = super(ComentarioPagina, self).form_valid(form)
        return resultado
