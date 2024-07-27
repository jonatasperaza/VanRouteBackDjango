from rest_framework import serializers
from vanroute.models.motoristas import Motorista
from vanroute.serializers.enderecos import EnderecoSerializer

class MotoristaSerializer(serializers.ModelSerializer):
    enderecos = EnderecoSerializer(many=True, read_only=True)

    class Meta:
        model = Motorista
        fields = '__all__'
