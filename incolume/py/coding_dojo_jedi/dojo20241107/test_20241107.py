"""Test module."""

from typing import Any
import httpx
import pytest
from http import HTTPStatus
from dataclasses import dataclass, field
import datetime as dt
import pytz

TZ = pytz.timezone('America/Sao_Paulo')


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
    timestamp: int = field(default=0, init=False)
    create_date: dt.datetime = field(
        default_factory=dt.datetime.now(tz=TZ).isoformat(),
    )

    def __post_init__(self):
        """Post init."""
        self.code = self.code.upper()
        self.timestamp = (
            dt.datetime.strptime(
                self.create_date,
                '%Y-%m-%dT%H:%M:%S.%f',
            )
            .astimezone(dt.timezone.tzname())
            .timestamp()
        )

    def to_dict(self) -> dict[str, Any]:
        """Dict."""
        return {f'{self.code}{self.codein}': {'ask': '1.23'}}


@pytest.fixture()
def fake_response(
    status: HTTPStatus | None = None,
    json: Json | None = None,
) -> httpx.Response:
    """Fake response."""
    status = status or HTTPStatus.OK
    json = json.to_dict() or {}
    return httpx.Response(status_code=status, json=json)


class TestCase:
    """Test case class."""

    # t0: ClassVar = None

    def test_0(self):
        """Unit test."""
        j = Json(code='usd', high=1.11, low=0.01, ask=1.1)
        assert j.to_dict() == {}

    # @pytest.mark.parametrize(
    #     'entrance expected'.split(),
    #     [
    #         ('usd', None),
    #     ],
    # )
    # def test_0(self, entrance, expected) -> NoReturn:
    #     """Unittest."""
    #     assert pkg.dojo(entrance) == expected
