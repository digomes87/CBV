from django.contrib import admin
from django.urls import path
from app.views import VisualizarHome, Registrar,Listar, Editar, Deletar

urlpatterns = [
    path('', VisualizarHome.as_view(), name="home"),
    path('lista/', Listar.as_view(), name="lista"),
    path('cadastro/', Registrar.as_view(), name="cadastro"),
    path('editar/<int:pk>', Editar.as_view(), name="editar"),
    path('editar/<int:pk>/deletar', Deletar.as_view(), name='deletar'),
]
