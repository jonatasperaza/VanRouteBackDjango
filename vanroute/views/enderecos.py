from rest_framework import viewsets
from vanroute.models.enderecos import Endereco
from vanroute.serializers.enderecos import EnderecoSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
