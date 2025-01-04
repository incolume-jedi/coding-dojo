"""Dojo."""

import httpx

url: str = 'https://swapi.dev/api/people/1/'


def saudacao(timeout: float = 9) -> None:
    """Saudação com nome extraído da API swapi."""
    r = httpx.get(url, timeout=timeout)

    name = r.json()['name']
    print('Hello,', name + '!')  #  noqa: T201
