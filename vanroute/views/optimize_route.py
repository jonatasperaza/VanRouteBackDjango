import requests
from django.shortcuts import render, get_object_or_404
from vanroute.models import Van, Aluno
from django.conf import settings
from django.http import HttpResponse
from urllib.parse import quote

def optimize_route(request, van_id):
    print("Fetching van...")
    van = get_object_or_404(Van, pk=van_id)
    print("Van found:", van)
    motorista = van.motorista
    motorista_endereco = motorista.enderecos.first()

    if motorista_endereco is None:
        return HttpResponse('Motorista não possui endereço', status=400)
    print("Motorista address:", motorista_endereco)

    alunos = Aluno.objects.all()
    enderecos_alunos = [aluno.enderecos.first() for aluno in alunos if aluno.enderecos.exists()]
    if not enderecos_alunos:
        return HttpResponse('Nenhum aluno possui endereço', status=400)
    print("Aluno addresses:", enderecos_alunos)

    addresses = [f"{motorista_endereco.rua}, {motorista_endereco.numero}, {motorista_endereco.cidade}"] + \
                [f"{end.rua}, {end.numero}, {end.cidade}" for end in enderecos_alunos]
    encoded_addresses = [quote(address) for address in addresses]
    api_key = settings.GOOGLE_MAPS_API_KEY
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={encoded_addresses[0]}&destination={encoded_addresses[0]}&waypoints=optimize:true|{'|'.join(encoded_addresses[1:])}&key={api_key}"
    print("Request URL:", url)

    response = requests.get(url)
    print("API Response Status Code:", response.status_code)
    print("API Response Text:", response.text)
    directions = response.json()

    return render(request, 'rota_otimizada.html', {'directions': directions})
