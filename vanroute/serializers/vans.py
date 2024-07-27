from rest_framework import serializers
from vanroute.models.vans import Van
from vanroute.serializers.motoristas import MotoristaSerializer

class VanSerializer(serializers.ModelSerializer):
    motorista = MotoristaSerializer()

    class Meta:
        model = Van
        fields = '__all__'
