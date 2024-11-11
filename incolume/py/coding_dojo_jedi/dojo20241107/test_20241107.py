"""Test module."""

from typing import Any, NoReturn
import httpx
import pytest
from http import HTTPStatus
from dataclasses import asdict, dataclass, field
import datetime as dt
import pytz
import incolume.py.coding_dojo_jedi.dojo20241107 as pkg
from functools import partial
from time_machine import travel
import respx

TZ = pytz.timezone('America/Sao_Paulo')


# ruff: noqa: ERA001


@dataclass
class FJson:
    """Response Fake JSON."""

    code: str
    ask: float
    codein: str = 'BRL'
    name: str = ''
    high: float = 0.0
    low: float = 0.0
    varBid: float = 0.0  # noqa: N815
    pctChange: float = 0.0  # noqa: N815
    bid: float = 0.0
    timestamp: int = field(default=-1, init=False)
    create_date: dt.datetime = field(
        default_factory=lambda: dt.datetime.now(tz=TZ),
    )

    def __post_init__(self):
        """Post init."""
        self.code = self.code.upper()
        self.timestamp = int(dt.datetime.now(tz=TZ).timestamp())

    def to_dict(self) -> dict[str, Any]:
        """Dict."""
        dict_values = {**self.__dict__}
        del dict_values['timestamp']
        o = FJson(**dict_values)
        o.create_date = self.create_date.isoformat(sep=' ')
        return {f'{self.code}{self.codein}': asdict(o)}


def f_resp(
    status: HTTPStatus | None = None,
    json: FJson | dict | None = None,
) -> httpx.Response:
    """Fake response."""
    status = status or HTTPStatus.OK
    try:
        json = json.to_dict()
    except (AttributeError, TypeError):
        json = {'USDBRL': {'ask': 123}}
    return httpx.Response(status_code=status, json=json)


@pytest.fixture()
def fake_response() -> httpx.Response:
    """Fake response."""
    return f_resp()


resp_200 = partial(f_resp, status=HTTPStatus.OK)


class TestCase0:
    """Test case class."""

    # t0: ClassVar = None

    def test_0(self, fake_response):
        """Unit test."""
        assert isinstance(fake_response, httpx.Response)

    def test_1(self, fake_response):
        """Unit test."""
        assert fake_response.json() == {'USDBRL': {'ask': 123}}

    def test_2(self):
        """Unit test."""
        o = FJson('usd', ask=1.234)
        assert set('code ask timestamp create_date'.split()).issubset(
            o.to_dict()['USDBRL'].keys(),
        )

    @travel('2024-11-07 12:34:56')
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {'code': 'usd', 'ask': 1.23},
                {
                    'USDBRL': {
                        'code': 'USD',
                        'ask': 1.23,
                        'codein': 'BRL',
                        'name': '',
                        'high': 0.0,
                        'low': 0.0,
                        'varBid': 0.0,
                        'pctChange': 0.0,
                        'bid': 0.0,
                        'timestamp': 1730993696,
                        'create_date': '2024-11-07 12:34:56-03:00',
                    },
                },
                marks=[
                    # pytest.mark.skip(),
                ],
            ),
            pytest.param(
                {'code': 'eur', 'ask': 1.23},
                {
                    'EURBRL': {
                        'code': 'EUR',
                        'ask': 1.23,
                        'codein': 'BRL',
                        'name': '',
                        'high': 0.0,
                        'low': 0.0,
                        'varBid': 0.0,
                        'pctChange': 0.0,
                        'bid': 0.0,
                        'timestamp': 1730993696,
                        'create_date': '2024-11-07 12:34:56-03:00',
                    },
                },
            ),
            pytest.param(
                {'code': 'eth', 'ask': 1.23},
                {
                    'ETHBRL': {
                        'code': 'ETH',
                        'ask': 1.23,
                        'codein': 'BRL',
                        'name': '',
                        'high': 0.0,
                        'low': 0.0,
                        'varBid': 0.0,
                        'pctChange': 0.0,
                        'bid': 0.0,
                        'timestamp': 1730993696,
                        'create_date': '2024-11-07 12:34:56-03:00',
                    },
                },
                marks=[],
            ),
            pytest.param(
                {'code': 'btc', 'ask': 1.23},
                {
                    'BTCBRL': {
                        'code': 'BTC',
                        'ask': 1.23,
                        'codein': 'BRL',
                        'name': '',
                        'high': 0.0,
                        'low': 0.0,
                        'varBid': 0.0,
                        'pctChange': 0.0,
                        'bid': 0.0,
                        'timestamp': 1730993696,
                        'create_date': '2024-11-07 12:34:56-03:00',
                    },
                },
                marks=[],
            ),
        ],
    )
    def test_3(self, entrance, expected):
        """Unit test."""
        assert FJson(**entrance).to_dict() == expected

    @travel('2024-11-07 12:34:56')
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {'code': 'usd', 'ask': 1.23},
                {
                    'USDBRL': {
                        'code': 'USD',
                        'ask': 1.23,
                        'codein': 'BRL',
                        'name': '',
                        'high': 0.0,
                        'low': 0.0,
                        'varBid': 0.0,
                        'pctChange': 0.0,
                        'bid': 0.0,
                        'timestamp': 1730993696,
                        'create_date': '2024-11-07 12:34:56-03:00',
                    },
                },
                marks=[],
            ),
            pytest.param(
                {'code': 'eur', 'ask': 123},
                {
                    'EURBRL': {
                        'code': 'EUR',
                        'ask': 123,
                        'codein': 'BRL',
                        'name': '',
                        'high': 0.0,
                        'low': 0.0,
                        'varBid': 0.0,
                        'pctChange': 0.0,
                        'bid': 0.0,
                        'timestamp': 1730993696,
                        'create_date': '2024-11-07 12:34:56-03:00',
                    },
                },
                marks=[],
            ),
            pytest.param(
                {'code': 'BTC', 'ask': 123},
                {
                    'BTCBRL': {
                        'code': 'BTC',
                        'ask': 123,
                        'codein': 'BRL',
                        'name': '',
                        'high': 0.0,
                        'low': 0.0,
                        'varBid': 0.0,
                        'pctChange': 0.0,
                        'bid': 0.0,
                        'timestamp': 1730993696,
                        'create_date': '2024-11-07 12:34:56-03:00',
                    },
                },
                marks=[],
            ),
        ],
    )
    def test_4(self, entrance, expected):
        """Unit test."""
        obj = resp_200(json=FJson(**entrance))
        assert obj.status_code.value == HTTPStatus.OK
        assert obj.json() == expected


class TestCase1:
    """Test case class."""

    # __test__ = False

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param({'code': 'usd', 'ask': 1.23}, 'Última cotação: 1.23'),
            pytest.param({'code': 'eth', 'ask': 12.3}, 'Última cotação: 12.3'),
            pytest.param({'code': 'btc', 'ask': 123}, 'Última cotação: 123'),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        url = 'https://economia.awesomeapi.com.br/json/last/{}'.format(
            entrance.get('code'),
        )
        mocked_resp = resp_200(json=FJson(**entrance))
        with respx.mock:
            my_route = respx.get(url)
            my_route.mock(mocked_resp)
            assert pkg.dojo(entrance.get('code')) == expected
