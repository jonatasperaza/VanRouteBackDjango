from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from .enderecos import Endereco

class Aluno(models.Model):
    nome = models.CharField(max_length=100, null=False)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    enderecos = GenericRelation(Endereco)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Alunos'
        verbose_name = 'Aluno'
