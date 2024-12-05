"""Unittest for dojo."""

from os import environ
from sys import version_info
from http import HTTPStatus
from unittest import mock

import pytest

from incolume.py.coding_dojo_jedi.dojo20220727.star_wars2 import research

from incolume.py.coding_dojo_jedi.utils import genfile


@pytest.mark.skip(reason='replaced for test_research_mock')
@pytest.mark.skipif(
    version_info < (3, 9, 0),
    reason='This run only Python 3.9+',
)
@pytest.mark.webtest()
@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        (
            'Obi-Wan Kenobi',
            [
                {
                    'birth_year': '57BBY',
                    'created': '2014-12-10T16:16:29.192000Z',
                    'edited': '2014-12-20T21:17:50.325000Z',
                    'eye_color': 'blue-gray',
                    'films': [
                        'https://swapi.dev/api/films/1/',
                        'https://swapi.dev/api/films/2/',
                        'https://swapi.dev/api/films/3/',
                        'https://swapi.dev/api/films/4/',
                        'https://swapi.dev/api/films/5/',
                        'https://swapi.dev/api/films/6/',
                    ],
                    'gender': 'male',
                    'hair_color': 'auburn, white',
                    'height': '182',
                    'homeworld': 'https://swapi.dev/api/planets/20/',
                    'mass': '77',
                    'name': 'Obi-Wan Kenobi',
                    'skin_color': 'fair',
                    'species': [],
                    'starships': [
                        'https://swapi.dev/api/starships/48/',
                        'https://swapi.dev/api/starships/59/',
                        'https://swapi.dev/api/starships/64/',
                        'https://swapi.dev/api/starships/65/',
                        'https://swapi.dev/api/starships/74/',
                    ],
                    'url': 'https://swapi.dev/api/people/10/',
                    'vehicles': ['https://swapi.dev/api/vehicles/38/'],
                },
            ],
        ),
        (
            'Luke Skywalker',
            [
                {
                    'birth_year': '19BBY',
                    'created': '2014-12-09T13:50:51.644000Z',
                    'edited': '2014-12-20T21:17:56.891000Z',
                    'eye_color': 'blue',
                    'films': [
                        'https://swapi.dev/api/films/1/',
                        'https://swapi.dev/api/films/2/',
                        'https://swapi.dev/api/films/3/',
                        'https://swapi.dev/api/films/6/',
                    ],
                    'gender': 'male',
                    'hair_color': 'blond',
                    'height': '172',
                    'homeworld': 'https://swapi.dev/api/planets/1/',
                    'mass': '77',
                    'name': 'Luke Skywalker',
                    'skin_color': 'fair',
                    'species': [],
                    'starships': [
                        'https://swapi.dev/api/starships/12/',
                        'https://swapi.dev/api/starships/22/',
                    ],
                    'url': 'https://swapi.dev/api/people/1/',
                    'vehicles': [
                        'https://swapi.dev/api/vehicles/14/',
                        'https://swapi.dev/api/vehicles/30/',
                    ],
                },
            ],
        ),
        (
            'Tion Medon',
            [
                {
                    'birth_year': 'unknown',
                    'created': '2014-12-20T20:35:04.260000Z',
                    'edited': '2014-12-20T21:17:50.498000Z',
                    'eye_color': 'black',
                    'films': ['https://swapi.dev/api/films/6/'],
                    'gender': 'male',
                    'hair_color': 'none',
                    'height': '206',
                    'homeworld': 'https://swapi.dev/api/planets/12/',
                    'mass': '80',
                    'name': 'Tion Medon',
                    'skin_color': 'grey',
                    'species': ['https://swapi.dev/api/species/37/'],
                    'starships': [],
                    'url': 'https://swapi.dev/api/people/83/',
                    'vehicles': [],
                },
            ],
        ),
        (
            'luke skywalker',
            [
                {
                    'birth_year': '19BBY',
                    'created': '2014-12-09T13:50:51.644000Z',
                    'edited': '2014-12-20T21:17:56.891000Z',
                    'eye_color': 'blue',
                    'films': [
                        'https://swapi.dev/api/films/1/',
                        'https://swapi.dev/api/films/2/',
                        'https://swapi.dev/api/films/3/',
                        'https://swapi.dev/api/films/6/',
                    ],
                    'gender': 'male',
                    'hair_color': 'blond',
                    'height': '172',
                    'homeworld': 'https://swapi.dev/api/planets/1/',
                    'mass': '77',
                    'name': 'Luke Skywalker',
                    'skin_color': 'fair',
                    'species': [],
                    'starships': [
                        'https://swapi.dev/api/starships/12/',
                        'https://swapi.dev/api/starships/22/',
                    ],
                    'url': 'https://swapi.dev/api/people/1/',
                    'vehicles': [
                        'https://swapi.dev/api/vehicles/14/',
                        'https://swapi.dev/api/vehicles/30/',
                    ],
                },
            ],
        ),
        ('xpto', []),
        ('skyw', ['Luke Skywalker', 'Anakin Skywalker', 'Shmi Skywalker']),
        (
            'jinn',
            [
                {
                    'birth_year': '92BBY',
                    'created': '2014-12-19T16:54:53.618000Z',
                    'edited': '2014-12-20T21:17:50.375000Z',
                    'eye_color': 'blue',
                    'films': ['https://swapi.dev/api/films/4/'],
                    'gender': 'male',
                    'hair_color': 'brown',
                    'height': '193',
                    'homeworld': 'https://swapi.dev/api/planets/28/',
                    'mass': '89',
                    'name': 'Qui-Gon Jinn',
                    'skin_color': 'fair',
                    'species': [],
                    'starships': [],
                    'url': 'https://swapi.dev/api/people/32/',
                    'vehicles': ['https://swapi.dev/api/vehicles/38/'],
                },
            ],
        ),
    ],
)
def test_research(entrance, expected) -> None:
    """Test research."""
    timeout = float(environ.get('TIMEOUT', '0.8'))
    assert research(entrance, timeout=timeout) == expected


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        (
            'Obi-Wan Kenobi',
            [
                {
                    'birth_year': '57BBY',
                    'created': '2014-12-10T16:16:29.192000Z',
                    'edited': '2014-12-20T21:17:50.325000Z',
                    'eye_color': 'blue-gray',
                    'films': [
                        'https://swapi.dev/api/films/1/',
                        'https://swapi.dev/api/films/2/',
                        'https://swapi.dev/api/films/3/',
                        'https://swapi.dev/api/films/4/',
                        'https://swapi.dev/api/films/5/',
                        'https://swapi.dev/api/films/6/',
                    ],
                    'gender': 'male',
                    'hair_color': 'auburn, white',
                    'height': '182',
                    'homeworld': 'https://swapi.dev/api/planets/20/',
                    'mass': '77',
                    'name': 'Obi-Wan Kenobi',
                    'skin_color': 'fair',
                    'species': [],
                    'starships': [
                        'https://swapi.dev/api/starships/48/',
                        'https://swapi.dev/api/starships/59/',
                        'https://swapi.dev/api/starships/64/',
                        'https://swapi.dev/api/starships/65/',
                        'https://swapi.dev/api/starships/74/',
                    ],
                    'url': 'https://swapi.dev/api/people/10/',
                    'vehicles': ['https://swapi.dev/api/vehicles/38/'],
                },
            ],
        ),
        (
            'Luke Skywalker',
            [
                {
                    'birth_year': '19BBY',
                    'created': '2014-12-09T13:50:51.644000Z',
                    'edited': '2014-12-20T21:17:56.891000Z',
                    'eye_color': 'blue',
                    'films': [
                        'https://swapi.dev/api/films/1/',
                        'https://swapi.dev/api/films/2/',
                        'https://swapi.dev/api/films/3/',
                        'https://swapi.dev/api/films/6/',
                    ],
                    'gender': 'male',
                    'hair_color': 'blond',
                    'height': '172',
                    'homeworld': 'https://swapi.dev/api/planets/1/',
                    'mass': '77',
                    'name': 'Luke Skywalker',
                    'skin_color': 'fair',
                    'species': [],
                    'starships': [
                        'https://swapi.dev/api/starships/12/',
                        'https://swapi.dev/api/starships/22/',
                    ],
                    'url': 'https://swapi.dev/api/people/1/',
                    'vehicles': [
                        'https://swapi.dev/api/vehicles/14/',
                        'https://swapi.dev/api/vehicles/30/',
                    ],
                },
            ],
        ),
        (
            'Tion Medon',
            [
                {
                    'birth_year': 'unknown',
                    'created': '2014-12-20T20:35:04.260000Z',
                    'edited': '2014-12-20T21:17:50.498000Z',
                    'eye_color': 'black',
                    'films': ['https://swapi.dev/api/films/6/'],
                    'gender': 'male',
                    'hair_color': 'none',
                    'height': '206',
                    'homeworld': 'https://swapi.dev/api/planets/12/',
                    'mass': '80',
                    'name': 'Tion Medon',
                    'skin_color': 'grey',
                    'species': ['https://swapi.dev/api/species/37/'],
                    'starships': [],
                    'url': 'https://swapi.dev/api/people/83/',
                    'vehicles': [],
                },
            ],
        ),
        (
            'luke skywalker',
            [
                {
                    'birth_year': '19BBY',
                    'created': '2014-12-09T13:50:51.644000Z',
                    'edited': '2014-12-20T21:17:56.891000Z',
                    'eye_color': 'blue',
                    'films': [
                        'https://swapi.dev/api/films/1/',
                        'https://swapi.dev/api/films/2/',
                        'https://swapi.dev/api/films/3/',
                        'https://swapi.dev/api/films/6/',
                    ],
                    'gender': 'male',
                    'hair_color': 'blond',
                    'height': '172',
                    'homeworld': 'https://swapi.dev/api/planets/1/',
                    'mass': '77',
                    'name': 'Luke Skywalker',
                    'skin_color': 'fair',
                    'species': [],
                    'starships': [
                        'https://swapi.dev/api/starships/12/',
                        'https://swapi.dev/api/starships/22/',
                    ],
                    'url': 'https://swapi.dev/api/people/1/',
                    'vehicles': [
                        'https://swapi.dev/api/vehicles/14/',
                        'https://swapi.dev/api/vehicles/30/',
                    ],
                },
            ],
        ),
        ('xpto', []),
        ('skyw', ['Luke Skywalker', 'Anakin Skywalker', 'Shmi Skywalker']),
        (
            'jinn',
            [
                {
                    'birth_year': '92BBY',
                    'created': '2014-12-19T16:54:53.618000Z',
                    'edited': '2014-12-20T21:17:50.375000Z',
                    'eye_color': 'blue',
                    'films': ['https://swapi.dev/api/films/4/'],
                    'gender': 'male',
                    'hair_color': 'brown',
                    'height': '193',
                    'homeworld': 'https://swapi.dev/api/planets/28/',
                    'mass': '89',
                    'name': 'Qui-Gon Jinn',
                    'skin_color': 'fair',
                    'species': [],
                    'starships': [],
                    'url': 'https://swapi.dev/api/people/32/',
                    'vehicles': ['https://swapi.dev/api/vehicles/38/'],
                },
            ],
        ),
    ],
)
def test_research_mock(entrance, expected) -> None:
    """Test research with mock."""
    cache_file = genfile().with_name('personagens.json')
    cache_file.unlink(missing_ok=True)

    response_mock = mock.MagicMock()
    response_mock.status_code = HTTPStatus.OK
    response_mock.json.return_value = {
        'count': 1,
        'next': None,
        'previous': None,
        'results': [{'name': nome} for nome in expected]
        if len(expected) >= 1 and isinstance(expected[0], str)
        else expected,
    }

    objreq2 = mock.MagicMock()
    objreq2.status_code = HTTPStatus.NOT_FOUND
    objreq2.json.return_value = {'detail': 'Not found'}

    with mock.patch('requests.get', side_effect=[response_mock, objreq2]):
        timeout = float(environ.get('TIMEOUT', '0.8'))
        assert research(entrance, timeout=timeout) == expected
