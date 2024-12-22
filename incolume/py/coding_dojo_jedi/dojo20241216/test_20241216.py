"""Test module."""

import http
from typing import ClassVar, NoReturn

import httpx
import incolume.py.coding_dojo_jedi.dojo20241216 as pkg
import pytest
import respx
import tempfile
from icecream import ic

# ruff: noqa: SIM115


class TestCase:
    """Test case class."""

    t0: ClassVar = None
    client: pkg.httpx.Client()

    def test_image_model(self):
        """Unit test."""
        entrance = {
            'filename': tempfile.NamedTemporaryFile().name,
            'content': 'xpto',
        }
        obj = pkg.ImageFile(**entrance)
        assert isinstance(obj.to_dict(), dict)
        assert entrance == obj.to_dict()

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
