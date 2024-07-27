from django.db import models
from .motoristas import Motorista

class Van(models.Model):
    placa = models.CharField(max_length=7, null=False, unique=True)
    capacidade = models.PositiveIntegerField(null=False)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.placa} - {self.motorista.nome}"

    class Meta:
        verbose_name_plural = 'Vans'
        verbose_name = 'Van'
