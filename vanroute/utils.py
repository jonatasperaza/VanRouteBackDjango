# utils.py

import requests
from django.conf import settings

def optimize_route(addresses):
    """
    Otimiza a rota usando a API do Google Maps.

    :param addresses: Lista de endereços.
    :return: Rota otimizada.
    """
    api_key = settings.GOOGLE_MAPS_API_KEY
    url = 'https://maps.googleapis.com/maps/api/directions/json'

    # Parâmetros para a requisição
    params = {
        'origin': addresses[0],  # Endereço de partida
        'destination': addresses[-1],  # Endereço de destino
        'waypoints': '|'.join(addresses[1:-1]),  # Endereços intermediários
        'optimizeWaypoints': 'true',
        'key': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        optimized_order = data['routes'][0]['waypoint_order']
        optimized_addresses = [addresses[i] for i in optimized_order]
        return optimized_addresses
    else:
        raise Exception('Erro na API do Google Maps: {}'.format(data))

