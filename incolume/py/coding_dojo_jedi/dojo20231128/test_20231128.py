"""Test dojo."""

from http import HTTPStatus
from typing import ClassVar
from unittest import mock

import pytest

from incolume.py.coding_dojo_jedi.dojo20231128.dojo import (
    TIMEOUT,
    ConsumingNextPageSWAPI,
    __pkg__,
    consuming_api_httpbin,
    consuming_api_swapi_index_page_0,
    consuming_api_swapi_index_page_1,
    consuming_api_swapi_index_page_2,
    consuming_api_swapi_one_page,
    consuming_api_swapi_one_person,
    dt,
    factorial,
    requests,
    timestamp,
)

__author__ = '@britodfbr'  # pragma: no cover


def test_package_name() -> None:
    """Test package name."""
    assert __pkg__ == 'incolume.py.coding_dojo_jedi.dojo20231128.dojo'


# @pytest.mark.skip
class TestDateTime:
    """Class DateTime."""

    @mock.patch(f'{__pkg__}.dt.datetime')
    def test_datetime_0(self, m_dt) -> None:
        """Test it."""
        time_stamp = dt.datetime(2000, 1, 2, 3, 4, 56)
        m_dt.today.return_value = time_stamp
        assert dt.datetime.today() == time_stamp
        assert m_dt.call_args_list == [mock.call(2000, 1, 2, 3, 4, 56)]

    @mock.patch(f'{__pkg__}.dt.datetime')
    def test_datetime_1(self, m_dt) -> None:
        """Test it."""
        time_stamp = dt.datetime(2000, 1, 2, 3, 4, 56)
        m_dt.now.return_value = time_stamp
        assert dt.datetime.now() == time_stamp

    def test_datetime_2(self) -> None:
        """Test it."""
        time_stamp = dt.datetime(2000, 1, 2, 3, 4, 56)
        with mock.patch(f'{__pkg__}.dt.datetime') as m_dt:
            m_dt.today.return_value = time_stamp
            assert dt.datetime.today() == time_stamp

    def test_datetime_3(self) -> None:
        """Test it."""
        time_stamp = dt.datetime(2000, 1, 2, 3, 4, 56)
        with mock.patch(f'{__pkg__}.dt.datetime') as m_dt:
            m_dt.now.return_value = time_stamp
            assert dt.datetime.now() == time_stamp


@mock.patch(f'{__pkg__}.dt.datetime')
def test_timestamp(m_dt) -> None:
    """Test it."""
    time_stamp = dt.datetime(2000, 1, 2, 3, 4, 56)
    expected = (a := time_stamp.year, b := time_stamp.strftime('%FT%T%z'))
    m_dt.today.return_value.year = a
    m_dt.today.return_value.strftime.return_value = b
    assert timestamp() == expected


# @pytest.mark.skip
def test_factorial():
    """Test factorial."""
    entrance = 4
    with mock.patch(f'{__pkg__}.factorial', autospec=True) as m_fact:
        factorial(entrance)
        assert m_fact.call_args_list == [mock.call(3)]


@mock.patch(f'{__pkg__}.requests.get')
def test_consuming_api_httpbin(mock_requests_get) -> None:
    """Test it."""
    mock_requests_get.return_value = mock.Mock(
        **{
            'status_code': HTTPStatus.OK,
            'json.return_value': {'origin': '1.1.1.1'},
        },
    )
    assert consuming_api_httpbin() == '1.1.1.1'
    mock_requests_get.assert_called_once_with(
        'https://httpbin.org/ip',
        timeout=TIMEOUT,
    )
    mock_requests_get.assert_called_with(
        'https://httpbin.org/ip',
        timeout=TIMEOUT,
    )


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (
            1,
            {
                'name': 'Luke Skywalker',
                'height': '172',
                'mass': '77',
                'hair_color': 'blond',
                'skin_color': 'fair',
                'eye_color': 'blue',
                'birth_year': '19BBY',
                'gender': 'male',
                'homeworld': 'https://swapi.dev/api/planets/1/',
                'films': [
                    'https://swapi.dev/api/films/2/',
                    'https://swapi.dev/api/films/6/',
                    'https://swapi.dev/api/films/3/',
                    'https://swapi.dev/api/films/1/',
                    'https://swapi.dev/api/films/7/',
                ],
                'species': ['https://swapi.dev/api/species/1/'],
                'vehicles': [
                    'https://swapi.dev/api/vehicles/14/',
                    'https://swapi.dev/api/vehicles/30/',
                ],
                'starships': [
                    'https://swapi.dev/api/starships/12/',
                    'https://swapi.dev/api/starships/22/',
                ],
                'created': '2014-12-09T13:50:51.644000Z',
                'edited': '2014-12-20T21:17:56.891000Z',
                'url': 'https://swapi.dev/api/people/1/',
            },
        ),
        (
            82,
            {
                'name': 'Sly Moore',
                'height': '178',
                'mass': '48',
                'hair_color': 'none',
                'skin_color': 'pale',
                'eye_color': 'white',
                'birth_year': 'unknown',
                'gender': 'female',
                'homeworld': 'https://swapi.dev/api/planets/60/',
                'films': [
                    'https://swapi.dev/api/films/5/',
                    'https://swapi.dev/api/films/6/',
                ],
                'species': [],
                'vehicles': [],
                'starships': [],
                'created': '2014-12-20T20:18:37.619000Z',
                'edited': '2014-12-20T21:17:50.496000Z',
                'url': 'https://swapi.dev/api/people/82/',
            },
        ),
    ],
)
@mock.patch(f'{__pkg__}.requests.get', autospec=True)
def test_consuming_api_swapi_one_person(m_req, entrance, expected) -> None:
    """Test it."""
    m_req.return_value.json.return_value = expected
    assert consuming_api_swapi_one_person(entrance) == expected
    m_req.assert_called_once_with(
        f'https://swapi.dev/api/people/{entrance}',
        timeout=TIMEOUT,
    )


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (
            1,
            {
                'count': 82,
                'next': 'https://swapi.dev/api/people/?page=2&format=json',
                'previous': None,
                'results': [
                    {
                        'name': 'Luke Skywalker',
                        'height': '172',
                        'mass': '77',
                        'hair_color': 'blond',
                        'skin_color': 'fair',
                        'eye_color': 'blue',
                        'birth_year': '19BBY',
                        'gender': 'male',
                        'homeworld': 'https://swapi.dev/api/planets/1/',
                        'films': [
                            'https://swapi.dev/api/films/1/',
                            'https://swapi.dev/api/films/2/',
                            'https://swapi.dev/api/films/3/',
                            'https://swapi.dev/api/films/6/',
                        ],
                        'species': [],
                        'vehicles': [
                            'https://swapi.dev/api/vehicles/14/',
                            'https://swapi.dev/api/vehicles/30/',
                        ],
                        'starships': [
                            'https://swapi.dev/api/starships/12/',
                            'https://swapi.dev/api/starships/22/',
                        ],
                        'created': '2014-12-09T13:50:51.644000Z',
                        'edited': '2014-12-20T21:17:56.891000Z',
                        'url': 'https://swapi.dev/api/people/1/',
                    },
                    {
                        'name': 'C-3PO',
                        'height': '167',
                        'mass': '75',
                        'hair_color': 'n/a',
                        'skin_color': 'gold',
                        'eye_color': 'yellow',
                        'birth_year': '112BBY',
                        'gender': 'n/a',
                        'homeworld': 'https://swapi.dev/api/planets/1/',
                        'films': [
                            'https://swapi.dev/api/films/1/',
                            'https://swapi.dev/api/films/2/',
                            'https://swapi.dev/api/films/3/',
                            'https://swapi.dev/api/films/4/',
                            'https://swapi.dev/api/films/5/',
                            'https://swapi.dev/api/films/6/',
                        ],
                        'species': ['https://swapi.dev/api/species/2/'],
                        'vehicles': [],
                        'starships': [],
                        'created': '2014-12-10T15:10:51.357000Z',
                        'edited': '2014-12-20T21:17:50.309000Z',
                        'url': 'https://swapi.dev/api/people/2/',
                    },
                    {
                        'name': 'R2-D2',
                        'height': '96',
                        'mass': '32',
                        'hair_color': 'n/a',
                        'skin_color': 'white, blue',
                        'eye_color': 'red',
                        'birth_year': '33BBY',
                        'gender': 'n/a',
                        'homeworld': 'https://swapi.dev/api/planets/8/',
                        'films': [
                            'https://swapi.dev/api/films/1/',
                            'https://swapi.dev/api/films/2/',
                            'https://swapi.dev/api/films/3/',
                            'https://swapi.dev/api/films/4/',
                            'https://swapi.dev/api/films/5/',
                            'https://swapi.dev/api/films/6/',
                        ],
                        'species': ['https://swapi.dev/api/species/2/'],
                        'vehicles': [],
                        'starships': [],
                        'created': '2014-12-10T15:11:50.376000Z',
                        'edited': '2014-12-20T21:17:50.311000Z',
                        'url': 'https://swapi.dev/api/people/3/',
                    },
                    {
                        'name': 'Darth Vader',
                        'height': '202',
                        'mass': '136',
                        'hair_color': 'none',
                        'skin_color': 'white',
                        'eye_color': 'yellow',
                        'birth_year': '41.9BBY',
                        'gender': 'male',
                        'homeworld': 'https://swapi.dev/api/planets/1/',
                        'films': [
                            'https://swapi.dev/api/films/1/',
                            'https://swapi.dev/api/films/2/',
                            'https://swapi.dev/api/films/3/',
                            'https://swapi.dev/api/films/6/',
                        ],
                        'species': [],
                        'vehicles': [],
                        'starships': ['https://swapi.dev/api/starships/13/'],
                        'created': '2014-12-10T15:18:20.704000Z',
                        'edited': '2014-12-20T21:17:50.313000Z',
                        'url': 'https://swapi.dev/api/people/4/',
                    },
                    {
                        'name': 'Leia Organa',
                        'height': '150',
                        'mass': '49',
                        'hair_color': 'brown',
                        'skin_color': 'light',
                        'eye_color': 'brown',
                        'birth_year': '19BBY',
                        'gender': 'female',
                        'homeworld': 'https://swapi.dev/api/planets/2/',
                        'films': [
                            'https://swapi.dev/api/films/1/',
                            'https://swapi.dev/api/films/2/',
                            'https://swapi.dev/api/films/3/',
                            'https://swapi.dev/api/films/6/',
                        ],
                        'species': [],
                        'vehicles': ['https://swapi.dev/api/vehicles/30/'],
                        'starships': [],
                        'created': '2014-12-10T15:20:09.791000Z',
                        'edited': '2014-12-20T21:17:50.315000Z',
                        'url': 'https://swapi.dev/api/people/5/',
                    },
                    {
                        'name': 'Owen Lars',
                        'height': '178',
                        'mass': '120',
                        'hair_color': 'brown, grey',
                        'skin_color': 'light',
                        'eye_color': 'blue',
                        'birth_year': '52BBY',
                        'gender': 'male',
                        'homeworld': 'https://swapi.dev/api/planets/1/',
                        'films': [
                            'https://swapi.dev/api/films/1/',
                            'https://swapi.dev/api/films/5/',
                            'https://swapi.dev/api/films/6/',
                        ],
                        'species': [],
                        'vehicles': [],
                        'starships': [],
                        'created': '2014-12-10T15:52:14.024000Z',
                        'edited': '2014-12-20T21:17:50.317000Z',
                        'url': 'https://swapi.dev/api/people/6/',
                    },
                    {
                        'name': 'Beru Whitesun lars',
                        'height': '165',
                        'mass': '75',
                        'hair_color': 'brown',
                        'skin_color': 'light',
                        'eye_color': 'blue',
                        'birth_year': '47BBY',
                        'gender': 'female',
                        'homeworld': 'https://swapi.dev/api/planets/1/',
                        'films': [
                            'https://swapi.dev/api/films/1/',
                            'https://swapi.dev/api/films/5/',
                            'https://swapi.dev/api/films/6/',
                        ],
                        'species': [],
                        'vehicles': [],
                        'starships': [],
                        'created': '2014-12-10T15:53:41.121000Z',
                        'edited': '2014-12-20T21:17:50.319000Z',
                        'url': 'https://swapi.dev/api/people/7/',
                    },
                    {
                        'name': 'R5-D4',
                        'height': '97',
                        'mass': '32',
                        'hair_color': 'n/a',
                        'skin_color': 'white, red',
                        'eye_color': 'red',
                        'birth_year': 'unknown',
                        'gender': 'n/a',
                        'homeworld': 'https://swapi.dev/api/planets/1/',
                        'films': ['https://swapi.dev/api/films/1/'],
                        'species': ['https://swapi.dev/api/species/2/'],
                        'vehicles': [],
                        'starships': [],
                        'created': '2014-12-10T15:57:50.959000Z',
                        'edited': '2014-12-20T21:17:50.321000Z',
                        'url': 'https://swapi.dev/api/people/8/',
                    },
                    {
                        'name': 'Biggs Darklighter',
                        'height': '183',
                        'mass': '84',
                        'hair_color': 'black',
                        'skin_color': 'light',
                        'eye_color': 'brown',
                        'birth_year': '24BBY',
                        'gender': 'male',
                        'homeworld': 'https://swapi.dev/api/planets/1/',
                        'films': ['https://swapi.dev/api/films/1/'],
                        'species': [],
                        'vehicles': [],
                        'starships': ['https://swapi.dev/api/starships/12/'],
                        'created': '2014-12-10T15:59:50.509000Z',
                        'edited': '2014-12-20T21:17:50.323000Z',
                        'url': 'https://swapi.dev/api/people/9/',
                    },
                    {
                        'name': 'Obi-Wan Kenobi',
                        'height': '182',
                        'mass': '77',
                        'hair_color': 'auburn, white',
                        'skin_color': 'fair',
                        'eye_color': 'blue-gray',
                        'birth_year': '57BBY',
                        'gender': 'male',
                        'homeworld': 'https://swapi.dev/api/planets/20/',
                        'films': [
                            'https://swapi.dev/api/films/1/',
                            'https://swapi.dev/api/films/2/',
                            'https://swapi.dev/api/films/3/',
                            'https://swapi.dev/api/films/4/',
                            'https://swapi.dev/api/films/5/',
                            'https://swapi.dev/api/films/6/',
                        ],
                        'species': [],
                        'vehicles': ['https://swapi.dev/api/vehicles/38/'],
                        'starships': [
                            'https://swapi.dev/api/starships/48/',
                            'https://swapi.dev/api/starships/59/',
                            'https://swapi.dev/api/starships/64/',
                            'https://swapi.dev/api/starships/65/',
                            'https://swapi.dev/api/starships/74/',
                        ],
                        'created': '2014-12-10T16:16:29.192000Z',
                        'edited': '2014-12-20T21:17:50.325000Z',
                        'url': 'https://swapi.dev/api/people/10/',
                    },
                ],
            },
        ),
        (
            2,
            {
                'count': 82,
                'next': 'https://swapi.dev/api/people/?page=3',
                'previous': 'https://swapi.dev/api/people/?page=1',
                'results': [
                    {
                        'name': 'Anakin Skywalker',
                        'height': '188',
                        'mass': '84',
                        'hair_color': 'blond',
                        'skin_color': 'fair',
                        'eye_color': 'blue',
                        'birth_year': '41.9BBY',
                        'gender': 'male',
                        'homeworld': 'https://swapi.dev/api/planets/1/',
                        'films': [
                            'https://swapi.dev/api/films/4/',
                            'https://swapi.dev/api/films/5/',
                            'https://swapi.dev/api/films/6/',
                        ],
                        'species': [],
                        'vehicles': [
                            'https://swapi.dev/api/vehicles/44/',
                            'https://swapi.dev/api/vehicles/46/',
                        ],
                        'starships': [
                            'https://swapi.dev/api/starships/39/',
                            'https://swapi.dev/api/starships/59/',
                            'https://swapi.dev/api/starships/65/',
                        ],
                        'created': '2014-12-10T16:20:44.310000Z',
                        'edited': '2014-12-20T21:17:50.327000Z',
                        'url': 'https://swapi.dev/api/people/11/',
                    },
                    {
                        'name': 'Wilhuff Tarkin',
                        'height': '180',
                        'mass': 'unknown',
                        'hair_color': 'auburn, grey',
                        'skin_color': 'fair',
                        'eye_color': 'blue',
                        'birth_year': '64BBY',
                        'gender': 'male',
                        'homeworld': 'https://swapi.dev/api/planets/21/',
                        'films': [
                            'https://swapi.dev/api/films/1/',
                            'https://swapi.dev/api/films/6/',
                        ],
                        'species': [],
                        'vehicles': [],
                        'starships': [],
                        'created': '2014-12-10T16:26:56.138000Z',
                        'edited': '2014-12-20T21:17:50.330000Z',
                        'url': 'https://swapi.dev/api/people/12/',
                    },
                    {
                        'name': 'Chewbacca',
                        'height': '228',
                        'mass': '112',
                        'hair_color': 'brown',
                        'skin_color': 'unknown',
                        'eye_color': 'blue',
                        'birth_year': '200BBY',
                        'gender': 'male',
                        'homeworld': 'https://swapi.dev/api/planets/14/',
                        'films': [
                            'https://swapi.dev/api/films/1/',
                            'https://swapi.dev/api/films/2/',
                            'https://swapi.dev/api/films/3/',
                            'https://swapi.dev/api/films/6/',
                        ],
                        'species': ['https://swapi.dev/api/species/3/'],
                        'vehicles': ['https://swapi.dev/api/vehicles/19/'],
                        'starships': [
                            'https://swapi.dev/api/starships/10/',
                            'https://swapi.dev/api/starships/22/',
                        ],
                        'created': '2014-12-10T16:42:45.066000Z',
                        'edited': '2014-12-20T21:17:50.332000Z',
                        'url': 'https://swapi.dev/api/people/13/',
                    },
                    {
                        'name': 'Han Solo',
                        'height': '180',
                        'mass': '80',
                        'hair_color': 'brown',
                        'skin_color': 'fair',
                        'eye_color': 'brown',
                        'birth_year': '29BBY',
                        'gender': 'male',
                        'homeworld': 'https://swapi.dev/api/planets/22/',
                        'films': [
                            'https://swapi.dev/api/films/1/',
                            'https://swapi.dev/api/films/2/',
                            'https://swapi.dev/api/films/3/',
                        ],
                        'species': [],
                        'vehicles': [],
                        'starships': [
                            'https://swapi.dev/api/starships/10/',
                            'https://swapi.dev/api/starships/22/',
                        ],
                        'created': '2014-12-10T16:49:14.582000Z',
                        'edited': '2014-12-20T21:17:50.334000Z',
                        'url': 'https://swapi.dev/api/people/14/',
                    },
                    {
                        'name': 'Greedo',
                        'height': '173',
                        'mass': '74',
                        'hair_color': 'n/a',
                        'skin_color': 'green',
                        'eye_color': 'black',
                        'birth_year': '44BBY',
                        'gender': 'male',
                        'homeworld': 'https://swapi.dev/api/planets/23/',
                        'films': ['https://swapi.dev/api/films/1/'],
                        'species': ['https://swapi.dev/api/species/4/'],
                        'vehicles': [],
                        'starships': [],
                        'created': '2014-12-10T17:03:30.334000Z',
                        'edited': '2014-12-20T21:17:50.336000Z',
                        'url': 'https://swapi.dev/api/people/15/',
                    },
                    {
                        'name': 'Jabba Desilijic Tiure',
                        'height': '175',
                        'mass': '1,358',
                        'hair_color': 'n/a',
                        'skin_color': 'green-tan, brown',
                        'eye_color': 'orange',
                        'birth_year': '600BBY',
                        'gender': 'hermaphrodite',
                        'homeworld': 'https://swapi.dev/api/planets/24/',
                        'films': [
                            'https://swapi.dev/api/films/1/',
                            'https://swapi.dev/api/films/3/',
                            'https://swapi.dev/api/films/4/',
                        ],
                        'species': ['https://swapi.dev/api/species/5/'],
                        'vehicles': [],
                        'starships': [],
                        'created': '2014-12-10T17:11:31.638000Z',
                        'edited': '2014-12-20T21:17:50.338000Z',
                        'url': 'https://swapi.dev/api/people/16/',
                    },
                    {
                        'name': 'Wedge Antilles',
                        'height': '170',
                        'mass': '77',
                        'hair_color': 'brown',
                        'skin_color': 'fair',
                        'eye_color': 'hazel',
                        'birth_year': '21BBY',
                        'gender': 'male',
                        'homeworld': 'https://swapi.dev/api/planets/22/',
                        'films': [
                            'https://swapi.dev/api/films/1/',
                            'https://swapi.dev/api/films/2/',
                            'https://swapi.dev/api/films/3/',
                        ],
                        'species': [],
                        'vehicles': ['https://swapi.dev/api/vehicles/14/'],
                        'starships': ['https://swapi.dev/api/starships/12/'],
                        'created': '2014-12-12T11:08:06.469000Z',
                        'edited': '2014-12-20T21:17:50.341000Z',
                        'url': 'https://swapi.dev/api/people/18/',
                    },
                    {
                        'name': 'Jek Tono Porkins',
                        'height': '180',
                        'mass': '110',
                        'hair_color': 'brown',
                        'skin_color': 'fair',
                        'eye_color': 'blue',
                        'birth_year': 'unknown',
                        'gender': 'male',
                        'homeworld': 'https://swapi.dev/api/planets/26/',
                        'films': ['https://swapi.dev/api/films/1/'],
                        'species': [],
                        'vehicles': [],
                        'starships': ['https://swapi.dev/api/starships/12/'],
                        'created': '2014-12-12T11:16:56.569000Z',
                        'edited': '2014-12-20T21:17:50.343000Z',
                        'url': 'https://swapi.dev/api/people/19/',
                    },
                    {
                        'name': 'Yoda',
                        'height': '66',
                        'mass': '17',
                        'hair_color': 'white',
                        'skin_color': 'green',
                        'eye_color': 'brown',
                        'birth_year': '896BBY',
                        'gender': 'male',
                        'homeworld': 'https://swapi.dev/api/planets/28/',
                        'films': [
                            'https://swapi.dev/api/films/2/',
                            'https://swapi.dev/api/films/3/',
                            'https://swapi.dev/api/films/4/',
                            'https://swapi.dev/api/films/5/',
                            'https://swapi.dev/api/films/6/',
                        ],
                        'species': ['https://swapi.dev/api/species/6/'],
                        'vehicles': [],
                        'starships': [],
                        'created': '2014-12-15T12:26:01.042000Z',
                        'edited': '2014-12-20T21:17:50.345000Z',
                        'url': 'https://swapi.dev/api/people/20/',
                    },
                    {
                        'name': 'Palpatine',
                        'height': '170',
                        'mass': '75',
                        'hair_color': 'grey',
                        'skin_color': 'pale',
                        'eye_color': 'yellow',
                        'birth_year': '82BBY',
                        'gender': 'male',
                        'homeworld': 'https://swapi.dev/api/planets/8/',
                        'films': [
                            'https://swapi.dev/api/films/2/',
                            'https://swapi.dev/api/films/3/',
                            'https://swapi.dev/api/films/4/',
                            'https://swapi.dev/api/films/5/',
                            'https://swapi.dev/api/films/6/',
                        ],
                        'species': [],
                        'vehicles': [],
                        'starships': [],
                        'created': '2014-12-15T12:48:05.971000Z',
                        'edited': '2014-12-20T21:17:50.347000Z',
                        'url': 'https://swapi.dev/api/people/21/',
                    },
                ],
            },
        ),
    ],
)
@mock.patch(f'{__pkg__}.requests.get', autospec=True)
def test_consuming_api_swapi_one_page(m_req_get, entrance, expected) -> None:
    """Test it."""
    m_req_get.return_value = mock.Mock(
        **{
            'name': 'Mock response',
            'status_code': 200,
            'json.return_value': expected,
        },
    )
    assert consuming_api_swapi_one_page(entrance) == expected
    m_req_get.assert_called_once_with(
        url := f'https://swapi.dev/api/people/?page={entrance}',
        timeout=TIMEOUT,
    )
    m_req_get.assert_called_with(url, timeout=TIMEOUT)


class TestConsumingNextPageSWAPI:
    """Class test it."""

    obj = ConsumingNextPageSWAPI()

    @pytest.mark.skip(reason='Fail. This dont ran.')
    @mock.patch(f'{__pkg__}.requests.get', autospec=True)
    def test_consuming_api_swapi_next_page_0(self, m_req_get) -> None:
        """Test it."""
        entrance = 1
        expected = ''
        assert m_req_get
        assert self.obj.tratativa0(entrance) == expected

    def test_consuming_api_swapi_next_page_1(self) -> None:
        """Test it."""
        entrance = 1
        expected = f'{self.obj.url}/?page={entrance + 1}'
        with mock.patch(f'{__pkg__}.requests.get') as m_req:
            m_req.return_value.json.return_value = {'next': expected}
            assert self.obj.tratativa1(entrance) == expected

    @pytest.mark.parametrize(
        'entrance n_page'.split(),
        [
            (1, 2),
            (0, 7),
            (9, None),
        ],
    )
    def test_consuming_api_swapi_next_page_2(self, entrance, n_page) -> None:
        """Test it."""
        expected = f'{self.obj.url}/?page={n_page}' if n_page else n_page
        with mock.patch(f'{__pkg__}.requests.get', autospec=True) as m_req:
            m_req.return_value.json.return_value = {'next': expected}
            assert self.obj.tratativa1(entrance) == expected


class TestRequests:
    """Test requests."""

    headers: ClassVar = {
        'date': 'Wed, 29 Nov 2023 14:29:06 GMT',
        'content-type': 'application/json',
        'content-length': '34',
        'connection': 'keep-alive',
        'server': 'gunicorn/19.9.0',
        'access-control-allow-origin': '*',
        'access-control-allow-credentials': 'true',
    }

    @mock.patch(f'{__pkg__}.requests.get', autospec=True)
    def test_other_0(self, m_req_get):
        """Test it."""
        url = 'http://example.org'
        m_req_get.return_value.url = url

        u = requests.get('abc', timeout=TIMEOUT)
        assert u.url == url
        assert m_req_get.call_args_list == [mock.call('abc', timeout=TIMEOUT)]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('ok', True),
            ('status_code', HTTPStatus.OK),
            ('status_code', HTTPStatus.FORBIDDEN),
            ('status_code', HTTPStatus.NOT_FOUND),
            ('status_code', HTTPStatus.MOVED_PERMANENTLY),
            ('url', 'https://httpbin.org/ip'),
        ],
    )
    @mock.patch(f'{__pkg__}.requests.get', autospec=True)
    def test_other_1(self, m_req_get, entrance, expected):
        """Test it."""
        url = 'http://example.org'
        m_req_get.return_value = mock.Mock(
            **{
                entrance: expected,
            },
        )
        req = requests.get(url, timeout=TIMEOUT)
        assert getattr(req, entrance) == expected

    @pytest.mark.parametrize(
        'entrance mocking expected'.split(),
        [
            ('ok', {'ok': True, 'status_code': HTTPStatus.OK}, True),
            (
                'status_code',
                {'ok': True, 'status_code': HTTPStatus.OK},
                HTTPStatus.OK,
            ),
            (
                'status_code',
                {'ok': False, 'status_code': HTTPStatus.FORBIDDEN},
                HTTPStatus.FORBIDDEN,
            ),
            (
                'status_code',
                {'ok': False, 'status_code': HTTPStatus.NOT_FOUND},
                HTTPStatus.NOT_FOUND,
            ),
            (
                'status_code',
                {'ok': False, 'status_code': HTTPStatus.MOVED_PERMANENTLY},
                HTTPStatus.MOVED_PERMANENTLY,
            ),
            (
                'url',
                {
                    'ok': True,
                    'status_code': HTTPStatus.OK,
                    'url': 'https://httpbin.org/ip',
                },
                'https://httpbin.org/ip',
            ),
        ],
    )
    @mock.patch(f'{__pkg__}.requests.get', autospec=True)
    def test_other_2(self, m_req_get, entrance, mocking, expected):
        """Test it."""
        url = 'http://example.org'
        m_req_get.return_value = mock.Mock(**mocking)
        req = requests.get(url, timeout=TIMEOUT)
        assert getattr(req, entrance) == expected

    def test_other_3(self):
        """Test it."""
        url = 'http://httpbin.org/ip'
        with mock.patch(f'{__pkg__}.requests.get') as rq:
            rq.return_value.headers = self.headers
            r = requests.get(url, timeout=TIMEOUT)
            assert r.headers == self.headers

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('Content-Type', 'application/json'),
            ('content-type', 'application/json'),
            ('Date', 'Wed, 29 Nov 2023 14:29:06 GMT'),
            ('Server', 'gunicorn/19.9.0'),
            ('Content-Length', '34'),
            ('Connection', 'keep-alive'),
        ],
    )
    def test_other_4(self, entrance, expected):
        """Test it."""
        url = 'http://httpbin.org/ip'
        with mock.patch(f'{__pkg__}.requests.get') as rq:
            rq.return_value.headers = self.headers
            r = requests.get(url, timeout=TIMEOUT)
            assert r.headers.get(entrance.casefold()) == expected


@pytest.mark.skip(reason='Falha na chamada WEB; Necessário mock.')
class TestConsumingIndexPageSWAPI:
    """TestConsumingIndexPageSWAPI class."""

    # __test__ = False  # noqa: ERA001
    values: ClassVar = [
        'https://swapi.dev/api/people/?page=1',
        'https://swapi.dev/api/people/?page=2',
        'https://swapi.dev/api/people/?page=3',
        'https://swapi.dev/api/people/?page=4',
        'https://swapi.dev/api/people/?page=5',
        'https://swapi.dev/api/people/?page=6',
        'https://swapi.dev/api/people/?page=7',
        'https://swapi.dev/api/people/?page=8',
        'https://swapi.dev/api/people/?page=9',
        'https://swapi.dev/api/people/?page=10',
    ]

    # @pytest.mark.skip
    @pytest.mark.webtest()
    def test_case_1(self) -> None:
        """Test it."""
        assert consuming_api_swapi_index_page_0() == self.values

    def test_case_2(self) -> None:
        """Test it with mock.

        Test de apenas uma página.
        """
        with mock.patch(f'{__pkg__}.requests.get') as m_req_get:
            m_req_get.return_value.url = self.values[0]
            assert consuming_api_swapi_index_page_0() == self.values[:1]
            assert m_req_get.call_args_list == [
                mock.call(self.values[0], timeout=TIMEOUT),
            ]

    @pytest.mark.webtest()
    def test_case_3(self) -> None:
        """Test it with mock."""
        assert consuming_api_swapi_index_page_1() == self.values

    @pytest.mark.skip()
    def test_case_4(self) -> None:
        """Test it with mock."""
        with mock.patch(f'{__pkg__}.requests.get') as m_req_get:
            m_req_get.status_code = HTTPStatus.OK
            m_req_get.ok = True
            m_req_get.return_value.url.side_effect = self.values
            assert consuming_api_swapi_index_page_1() == self.values
            assert m_req_get.call_args_list == []

    @pytest.mark.webtest()
    def test_case_5(self) -> None:
        """Test it with mock."""
        assert consuming_api_swapi_index_page_2() == self.values
