"""Dojo."""

import datetime as dt
from http import HTTPStatus
from pathlib import Path
from urllib.parse import urlunparse

import requests

__author__ = '@britodfbr'  # pragma: no cover
_ = (p := Path(__file__).parts)[p.index('incolume') :]
__pkg__ = '.'.join(_).strip('.py')
TIMEOUT = 1
urls = {
    'swapi-people': 'https://swapi.dev/api/people',
    'httpbin-ip': 'https://httpbin.org/ip',
}


def timestamp():
    """Timestamp."""
    return dt.datetime.today().year, dt.datetime.today().strftime('%FT%X%z')


def factorial(n):
    """Factorial recursive."""
    if n < 2:
        return 1
    return n * factorial(n - 1)


def consuming_api_httpbin():
    """Consuming API httpbin."""
    response = requests.get(urls['httpbin-ip'], timeout=TIMEOUT)
    if response.status_code == 200:
        return response.json()['origin']
    return None


def consuming_api_swapi_one_person(id_person: int):
    """Swapi one person."""
    response = requests.get(
        f"{urls['swapi-people']}/{id_person}",
        timeout=TIMEOUT,
    )
    return response.json()


def consuming_api_swapi_one_page(nr_page: int):
    """Swapi one page."""
    response = requests.get(
        f'https://swapi.dev/api/people/?page={nr_page}',
        timeout=TIMEOUT,
    )
    if response.status_code == HTTPStatus.OK:
        return response.json()
    return {}


class ConsumingNextPageSWAPI:
    """Class Next page SWAPI."""

    url = urls['swapi-people']

    def tratativa0(self, nr_page: int):
        """Swapi Next page."""
        response = requests.get(f'{self.url}/?page={nr_page}', timeout=TIMEOUT)
        return response.next

    def tratativa1(self, nr_page: int):
        """Swapi Next page."""
        response = requests.get(
            self.url,
            params={'page': nr_page},
            timeout=TIMEOUT,
        )
        if response.ok:
            return response.json()['next']
        return None


def consuming_api_swapi_index_page_0(initial_page: int = 1):
    """Swapi index page."""
    check = HTTPStatus.OK.value
    results = []
    while check == HTTPStatus.OK:
        response = requests.get(
            f"{urls['swapi-people']}/?page={initial_page}",
            timeout=TIMEOUT,
        )
        results.append(url := response.url)
        print(url)
        check = response.status_code
        initial_page += 1
    return results


def consuming_api_swapi_index_page_1(initial_page: int = 1):
    """Swapi index page."""
    check = True
    results = []
    while check:
        response = requests.get(
            f'{urls["swapi-people"]}/?page={initial_page}',
            timeout=TIMEOUT,
        )
        results.append(url := response.url)
        print(url)
        check = response.ok
        initial_page += 1
    return results


def consuming_api_swapi_index_page_2(initial_page: int = 1):
    """Swapi index page."""
    check = True
    url = urlunparse((urls['swapi-people'], f'?page={initial_page}'))
    results = set()
    while check:
        response = requests.get(url, timeout=TIMEOUT)
        check = response.ok
        url = response.json()['next']
        results.add(url)
    return list(results)
