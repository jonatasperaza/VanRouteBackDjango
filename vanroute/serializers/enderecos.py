from rest_framework import serializers
from vanroute.models.enderecos import Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'
