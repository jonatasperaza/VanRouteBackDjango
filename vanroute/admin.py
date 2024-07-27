from django.contrib import admin
from .models import Aluno, Motorista, Endereco, Van

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data_nascimento', 'cpf')

@admin.register(Motorista)
class MotoristaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data_nascimento', 'cpf')

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('rua', 'numero', 'bairro', 'cidade', 'estado', 'cep')

@admin.register(Van)
class VanAdmin(admin.ModelAdmin):
    list_display = ('placa', 'capacidade', 'motorista')
