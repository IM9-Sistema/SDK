import requests
from os import environ


def get_reverse_address(lat: float, lon: float) -> str:
    try:
        request = requests.get(environ.get('NOMINATIM_HOST', 'http://10.15.1.102:8080/')+'/reverse', params={
            'lat': lat, 'lon': lon, 'format': 'jsonv2'
        })
    except:
        return get_reverse_address(lat, lon)

    if request.status_code == 500:
        return get_reverse_address(lat, lon)

    if request.status_code == 404:
        return environ.get('NOT_FOUND_ADDRESS', 'Endereço não encontrado')

    data = request.json()
    return data['display_name']