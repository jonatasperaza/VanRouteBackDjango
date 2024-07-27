from rest_framework import viewsets
from vanroute.models.motoristas import Motorista
from vanroute.serializers.motoristas import MotoristaSerializer

class MotoristaViewSet(viewsets.ModelViewSet):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer
