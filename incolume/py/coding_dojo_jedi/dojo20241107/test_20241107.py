"""Test module."""

from typing import ClassVar, NoReturn

import httpx
import incolume.py.coding_dojo_jedi.dojo20241107 as pkg
import pytest
from http import HTTPStatus


@pytest.fixture()
def fake_response(status: HTTPStatus | None = None, json: dict | None = None):
    """Fake response."""
    status = status or HTTPStatus.OK
    json = json or {}
    return httpx.Response(status_code=status, json=json)


class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (None, None),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(entrance) == expected
