import requests
from django.shortcuts import render, get_object_or_404
from vanroute.models import Van, Aluno, Motorista
from django.conf import settings
from django.http import HttpResponse

def optimize_route(request, van_id):
    van = get_object_or_404(Van, pk=van_id)
    motorista = van.motorista
    motorista_endereco = motorista.enderecos.first()

    if motorista_endereco is None:
        return HttpResponse('Motorista não possui endereço', status=400)

    alunos = Aluno.objects.all()
    enderecos_alunos = [aluno.enderecos.first() for aluno in alunos if aluno.enderecos.exists()]

    if not enderecos_alunos:
        return HttpResponse('Nenhum aluno possui endereço', status=400)

    addresses = [f"{motorista_endereco.rua}, {motorista_endereco.numero}, {motorista_endereco.cidade}"] + \
                [f"{end.rua}, {end.numero}, {end.cidade}" for end in enderecos_alunos]

    api_key = settings.GOOGLE_MAPS_API_KEY
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={addresses[0]}&destination={addresses[0]}&waypoints=optimize:true|{'|'.join(addresses[1:])}&key={api_key}"

    response = requests.get(url)
    directions = response.json()

    return render(request, 'rota_otimizada.html', {'directions': directions})
