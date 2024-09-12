"""Dojo module."""

import datetime as dt
from collections.abc import Container
from http import HTTPStatus
from pathlib import Path
from typing import Final
from urllib.parse import urlunparse

import requests
from pytz import timezone

__author__ = '@britodfbr'  # pragma: no cover
_ = (p := Path(__file__).parent.parts)[p.index('incolume') :]
__pkg__ = '.'.join(_).strip('.py')
TIMEOUT = 1
urls = {
    'swapi-people': 'https://swapi.dev/api/people',
    'httpbin-ip': 'https://httpbin.org/ip',
}

TZ: Final[timezone] = timezone('America/Sao_Paulo')


def timestamp():
    """Timestamp."""
    return (
        dt.datetime.now(tz=TZ).year,
        dt.datetime.now(tz=TZ).strftime('%FT%X%z'),
    )


def factorial(n):
    """Factorial recursive."""
    if n < 2:  # noqa: PLR2004
        return 1
    return n * factorial(n - 1)


def consuming_api_httpbin():
    """Consuming API httpbin."""
    response = requests.get(urls['httpbin-ip'], timeout=TIMEOUT)
    if response.status_code == HTTPStatus.OK:
        return response.json()['origin']
    return None


def consuming_api_swapi_one_person(id_person: int) -> str:
    """Swapi one person."""
    response = requests.get(
        f"{urls['swapi-people']}/{id_person}",
        timeout=TIMEOUT,
    )
    return response.json()


def consuming_api_swapi_one_page(nr_page: int) -> str:
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

    def tratativa0(self, nr_page: int) -> str:
        """Swapi Next page."""
        response = requests.get(f'{self.url}/?page={nr_page}', timeout=TIMEOUT)
        return response.next

    def tratativa1(self, nr_page: int) -> any:
        """Swapi Next page."""
        response = requests.get(
            self.url,
            params={'page': nr_page},
            timeout=TIMEOUT,
        )
        if response.ok:
            return response.json()['next']
        return None


def consuming_api_swapi_index_page_0(initial_page: int = 1) -> list[Container]:
    """Swapi index page."""
    check = HTTPStatus.OK.value
    results = []
    while check == HTTPStatus.OK:
        response = requests.get(
            f"{urls['swapi-people']}/?page={initial_page}",
            timeout=TIMEOUT,
        )
        results.append(url := response.url)
        print(url)  #  noqa: T201
        check = response.status_code
        initial_page += 1
    return results


def consuming_api_swapi_index_page_1(initial_page: int = 1) -> list[Container]:
    """Swapi index page."""
    check = True
    results = []
    while check:
        response = requests.get(
            f'{urls["swapi-people"]}/?page={initial_page}',
            timeout=TIMEOUT,
        )
        results.append(url := response.url)
        print(url)  #  noqa: T201
        check = response.ok
        initial_page += 1
    return results


def consuming_api_swapi_index_page_2(initial_page: int = 1) -> list[Container]:
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
