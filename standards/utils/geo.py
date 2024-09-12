import logging

import requests
from os import environ
from random import choice
import time

logger = logging.getLogger(__name__)

def get_reverse_address(lat: float, lon: float, hosts: list[str] = None, retry_wait: float = 0) -> str:
    if not hosts:
        hosts = environ.get('NOMINATIM_HOST', 'http://10.15.1.102:8080/').split(';')
    host = choice(hosts)
    try:
        request = requests.get(host+'/reverse', params={
            'lat': lat, 'lon': lon, 'format': 'jsonv2'
        })
    except:
        time.sleep(retry_wait)
        return get_reverse_address(lat, lon, hosts=hosts, retry_wait=retry_wait+1)

    if request.status_code == 500:
        time.sleep(retry_wait)
        return get_reverse_address(lat, lon, hosts=hosts, retry_wait=retry_wait+1.5)

    if request.status_code == 404:
        return environ.get('NOT_FOUND_ADDRESS', 'Endereço não encontrado')

    data = request.json()
    logger.debug(f'Got response from {host}: {data}')
    return data['display_name']