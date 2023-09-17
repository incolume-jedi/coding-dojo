from sys import version_info

import pytest
from star_wars import research


@pytest.mark.skipif(
    version_info < (3, 8, 0), reason='This run only Python 3.8+',
)
@pytest.mark.parametrize(
    ('entrance', 'expected'),
    (
        (
            'Obi-Wan Kenobi',
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
        ),
        (
            'Luke Skywalker',
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
        ),
        (
            'Tion Medon',
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
        ),
    ),
)
def test_research(entrance, expected):
    assert research(entrance) == expected
