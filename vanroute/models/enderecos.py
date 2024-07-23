from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Enderecos(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=False)
    content_object = GenericForeignKey('content_type', 'object_id')
    rua = models.CharField(max_length=100, null=False)
    numero = models.CharField(max_length=10, null=False)
    bairro = models.CharField(max_length=50, null=False)
    cidade = models.CharField(max_length=50, null=False)
    estado = models.CharField(max_length=2, null=False)
    cep = models.CharField(max_length=8, null=False)

    def __str__(self):
        return self.rua

    class Meta:
        verbose_name_plural = 'Endereços'
        verbose_name = 'Endereço'