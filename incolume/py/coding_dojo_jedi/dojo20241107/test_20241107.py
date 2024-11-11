"""Test module."""

from typing import Any, NoReturn
import httpx
import pytest
from http import HTTPStatus
from dataclasses import asdict, dataclass, field
import datetime as dt
import pytz
import incolume.py.coding_dojo_jedi.dojo20241107 as pkg

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
        o.create_date = self.create_date.isoformat()
        return {f'{self.code}{self.codein}': asdict(o)}


@pytest.fixture
def fake_response(
    status: HTTPStatus | None = None,
    json: Json | dict | None = None,
) -> httpx.Response:
    """Fake response."""
    status = status or HTTPStatus.OK
    json = {'USDBRL': {'ask': 123}}
    return httpx.Response(status_code=status, json=json)


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
