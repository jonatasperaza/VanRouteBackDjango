from rest_framework import viewsets
from vanroute.models.alunos import Aluno
from vanroute.serializers.alunos import AlunoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
