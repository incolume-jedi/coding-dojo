"""Test module."""

import http
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241216 as pkg
import pytest
import respx
import tempfile
from pathlib import Path
from icecream import ic
import json
from incolume.py.coding_dojo_jedi.utils import check_connectivity
# ruff: noqa: SIM115


class TestCase:
    """Test case class."""

    t0: ClassVar = None
    client: pkg.httpx.Client()

    def test_image_model_dict(self):
        """Unit test."""
        entrance = {
            'filename': tempfile.NamedTemporaryFile().name,
            'content': 'xpto',
        }
        obj = pkg.ImageFile(**entrance)
        assert isinstance(obj.to_dict(), dict)
        assert entrance == obj.to_dict()

    def test_image_model_json(self):
        """Unit test."""
        entrance = {
            'filename': tempfile.NamedTemporaryFile().name,
            'content': 'xpto',
        }
        obj = pkg.ImageFile(**entrance)
        assert isinstance(obj.to_json(), str)
        assert json.dumps(entrance) == obj.to_json()

    def test_bytes2base64(self):
        """Unittest."""
        entrance = 'nação'.encode()
        expected = 'bmHDp8Ojbw==\n'
        assert pkg.convert_byte_base64(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {'link': 'http://this.is.fake.url/image-fake.png'},
                b'its fake',
                marks=[pytest.mark.skip],
            ),
            pytest.param(
                {'link': pkg.url, 'fout': ''},
                b'its fake',
                marks=[pytest.mark.skip],
            ),
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
        request = respx.get(entrance['link'], content=expected)
        ic(mock_resp)
        with respx.mock:
            response = pkg.download_file(**entrance)
            assert request.called
            assert response.status_code == http.HTTPStatus.OK
            assert response.text == 'foobar'

            assert pkg.download_file(**entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {'link': 'http://this.is.fake.url/image-fake.png'},
                b'its fake',
                marks=[pytest.mark.skip],
            ),
            pytest.param(
                {'link': pkg.url, 'fout': tempfile.NamedTemporaryFile().name},
                b'\x89PNG\r',
                marks=[
                    pytest.mark.skipif(
                        not check_connectivity(),
                        reason='Not web connected.',
                    ),
                ],
            ),
        ],
    )
    def test_downloadfile(self, entrance, expected) -> NoReturn:
        """Unittest."""
        result = pkg.download_file(**entrance)
        assert isinstance(result, pkg.httpx.Response)
        assert expected in result.content

    def test_solution(self):
        """Unittest."""
        filename = Path('xpto.png')
        # filename = Path(tempfile.NamedTemporaryFile(suffix='.png').name)
        entrance = dict(
            link=pkg.url,
            fout=filename,
        )
        expected = filename.with_suffix('.json')
        assert pkg.dojo(**entrance) == expected
