"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241106 as pkg
import pytest
import respx
import httpx
from http import HTTPStatus

class TestRESPX:
    """Examples for respx."""
    @respx.mock
    def test_decorator(self):
        """Example."""
        my_route = respx.get("https://example.org/")
        response = httpx.get("https://example.org/")
        assert my_route.called
        assert response.status_code == HTTPStatus.OK

    def test_ctx_manager(self):
        """Example."""
        with respx.mock:
            my_route = respx.get("https://example.org/")
            response = httpx.get("https://example.org/")
            assert my_route.called
            assert response.status_code == HTTPStatus.OK

    def test_fixture(self, respx_mock):
        """Example."""
        my_route = respx_mock.get("https://example.org/")
        response = httpx.get("https://example.org/")
        assert my_route.called
        assert response.status_code == HTTPStatus.OK

    @pytest.mark.respx(base_url="https://foo.bar")
    def test_with_marker(self, respx_mock):
        """Example."""
        respx_mock.get("/baz/").mock(return_value=httpx.Response(204))
        response = httpx.get("https://foo.bar/baz/")
        assert response.status_code == HTTPStatus.NO_CONTENT


class TestCase:
    """Test case class."""

    t0: ClassVar=None

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
             (None, None),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(entrance) == expected
