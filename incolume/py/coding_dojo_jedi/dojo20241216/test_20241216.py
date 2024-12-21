"""Test module."""

import http
from typing import ClassVar, NoReturn

import httpx
import incolume.py.coding_dojo_jedi.dojo20241216 as pkg
import pytest
import respx


class TestCase:
    """Test case class."""

    t0: ClassVar = None
    client: httpx.Client()

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {'link': 'http://this.is.fake.url/image-fake.png'},
                b'its fake',
            ),
            pytest.param({'link': pkg.url, 'fout': ''}, b'its fake'),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        headers = {
            'Content-Type': 'image/png',
        }
        mock_resp = pkg.httpx.Response(
            201,
            content=b'its fake.',
            text='its fake.',
            headers=headers,
        )
        with respx.mock:
            request = respx.get(entrance['link'], content=expected)
            pkg.download_file(**entrance)
            response = pkg.download_file(**entrance)
            assert request.called
            assert response.status_code == http.HTTPStatus.OK
            assert response.text == 'foobar'

            # assert pkg.download_file(**entrance) == expected
