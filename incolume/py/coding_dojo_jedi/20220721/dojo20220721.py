"""Dojo."""
import requests


def saudacao(timeout=1) -> None:
    """Saudação com nome extraído da API swapi."""
    r = requests.get('https://swapi.dev/api/people/1/', timeout=timeout)

    name = r.json()['name']
    print('Hello,', name + '!')
