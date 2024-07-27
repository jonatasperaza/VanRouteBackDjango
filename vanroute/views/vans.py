from rest_framework import viewsets
from vanroute.models.vans import Van
from vanroute.serializers.vans import VanSerializer

class VanViewSet(viewsets.ModelViewSet):
    queryset = Van.objects.all()
    serializer_class = VanSerializer
