from rest_framework import serializers
from vanroute.models.alunos import Aluno
from vanroute.serializers.enderecos import EnderecoSerializer

class AlunoSerializer(serializers.ModelSerializer):
    enderecos = EnderecoSerializer(many=True, read_only=True)

    class Meta:
        model = Aluno
        fields = '__all__'
