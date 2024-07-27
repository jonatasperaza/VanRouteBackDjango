from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from .enderecos import Endereco

class Motorista(models.Model):
    nome = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    telefone = models.CharField(max_length=15, null=False)
    data_nascimento = models.DateField(null=False)
    cpf = models.CharField(max_length=11, null=False)
    enderecos = GenericRelation(Endereco)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Motoristas'
        verbose_name = 'Motorista'
