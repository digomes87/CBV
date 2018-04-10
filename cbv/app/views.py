from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cadastro
from .forms import form_cadastro
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import redirect

"""
O uso do CBV deixa a view o mais simples possivel
E existem oturas formas mais avançadas ainda de usara
"""
class VisualizarHome(TemplateView):
    """
    Aqui display pra exibir apenas
    """
    template_name = "app/home.html"
    def get_context_data(self,*args, **kwargs):
        context = super(VisualizarHome, self).get_context_data(*args, **kwargs)
        return context

class Registrar(CreateView):
    """
    Aqui Display para cadastrar
    """
    form_class = form_cadastro
    template_name = "app/cadastro.html"

    def get_success_url(self):
        return reverse("lista")

class Listar(ListView):
    """
    ListView reponsavel por buscar no banco os dados
    """
    model = Cadastro
    def get_queryset(self, *args, **kwargs):
        r = super(Listar, self).get_queryset(*args, **kwargs)
        return r

class Editar(UpdateView):
    model = Cadastro
    form_class = form_cadastro
    template_name = "app/cadastro_editar.html"

    def get_success_url(self):
        return reverse("lista")
#

class Deletar(DeleteView):
    model = Cadastro
    success_url = reverse_lazy("app/cadastro_confirm_delete.html")

    def get_success_url(self):
        return reverse("lista")
