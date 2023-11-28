"""Dojo."""
from pathlib import Path
import requests
from http import HTTPStatus
import datetime as dt

__author__ = '@britodfbr'  # pragma: no cover
_ = (p := Path(__file__).parts)[p.index('incolume') :]
__package__ = '.'.join(_).strip('.py')


def timestamp():
    return dt.datetime.today().year, dt.datetime.today().strftime('%FT%X%z')


def factorial(n):
    if n <= 2:
        return 1
    else:
        return n * factorial(n - 1)


def consuming_api_httpbin():
    """"""
    response = requests.get('https://httpbin.org/ip')
    if response.status_code == 200:
        return response.json()['origin']


def consuming_api_swapi_one_person(id_person: int):
    """Swapi one person."""
    response = requests.get(f'https://swapi.dev/api/people/{id_person}')
    return response.json()


def consuming_api_swapi_one_page(nr_page: int):
    """Swapi one page."""
    response = requests.get(f'https://swapi.dev/api/people/?page={nr_page}')
    if response.status_code == HTTPStatus.OK:
        return response.json()
    return {}


def consuming_api_swapi_next_page(nr_page: int):
    """Swapi Next page."""
    response = requests.get(f'https://swapi.dev/api/people/?page={nr_page}')
    results = []
    return response.next


def consuming_api_swapi_index_page(initial_page: int = 1):
    """Swapi index page."""
    check = HTTPStatus.OK
    results = []
    while check == HTTPStatus.OK:
        response = requests.get(
            f'https://swapi.dev/api/people/?page={initial_page}'
        )
        results.append(url := response.url)
        print(url)
        check = response.status_code
        initial_page += 1
    return results
