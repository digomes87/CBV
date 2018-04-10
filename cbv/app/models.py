from django.db import models
from django.urls import reverse

class Task(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    descricao = models.CharField(max_length=5000, blank=True, null=True)


    # def get_absolute_url(self):
    #     view_name = "editar"
    #     return reverse(view_name, kwargs={"pk": self.id})
