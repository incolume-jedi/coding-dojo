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

TZ = pytz.timezone('America/Sao_Paulo')


# ruff: noqa: ERA001


@dataclass
class Json:
    """Response JSON."""

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
        o = Json(**dict_values)
        o.create_date = self.create_date.isoformat(sep=' ')
        return {f'{self.code}{self.codein}': asdict(o)}


@pytest.fixture()
def fake_response(
    status: HTTPStatus | None = None,
    json: Json | dict | None = None,
) -> httpx.Response:
    """Fake response."""
    status = status or HTTPStatus.OK
    json = Json.to_dict() or {'USDBRL': {'ask': 123}}
    return httpx.Response(status_code=status, json=json)


resp_200 = partial(fake_response, status=HTTPStatus.OK)


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
        o = Json('usd', ask=1.234)
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
        assert Json(**entrance).to_dict() == expected


class TestCase1:
    """Test case class."""

    __test__ = False

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('usd', ''),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(entrance) == expected
