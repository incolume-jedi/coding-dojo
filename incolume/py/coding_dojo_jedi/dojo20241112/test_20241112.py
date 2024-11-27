"""Test module."""

from pathlib import Path
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241112 as pkg
import pytest
import asyncio
from tempfile import gettempdir

pkg.ic.enable()


# ruff: noqa: ERA001
class TestCase0:
    """Test case class."""

    path_out: ClassVar = Path(gettempdir()) / 'files'
    url: ClassVar = 'https://download.freebsd.org/ftp/releases/amd64/amd64/ISO-IMAGES/12.0/FreeBSD-12.0-RELEASE-amd64-mini-memstick.img'

    def test_0(self):
        """Unittest."""
        assert pkg.async_stream(
            pkg.URLS[0],
            output_path=self.path_out,
        )


class TestCase1:
    """Test case class."""

    path_out: ClassVar = Path(gettempdir()) / 'files'
    t0: ClassVar = None
    t1: ClassVar = [
        'https://httpbin.org',
    ]

    def test_0(self, respx_mock):
        """Unittest."""
        url_test = pkg.URLS[0]
        response = pkg.httpx.Response(
            200,
            content=b'xpto',
            headers={
                'date': 'Tue, 26 Nov 2024 16:20:24 GMT',
                'server': 'gunicorn/19.9.0',
                'x-cache': 'MISS from 172.27.32.103',
                'access-control-allow-origin': '*',
                'access-control-allow-credentials': 'true',
                'content-type': 'text/html; charset=utf-8',
                'content-length': '9593',
                'proxy-connection': 'Keep-Alive',
                'location': url_test,
            },
            request=pkg.httpx.Request('GET', url=url_test),
        )
        respx_mock.get(url_test).mock(
            side_effect=response,
        )
        assert pkg.sync_download(
            url_test,
            output_path=self.path_out,
        ).is_file()

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                'https://bd-rest.camara.leg.br/server/api/core/bitstreams/1d479a9f-1fb5-4fdf-ad7b-d635382a6cfd/content',
                True,
                marks=[],
            ),
            pytest.param(pkg.URLS[0], True, marks=[]),
            pytest.param(pkg.URLS[1], True, marks=[]),
            pytest.param(pkg.URLS[2], True, marks=[]),
        ],
    )
    def test_1(self, entrance, expected):
        """Unittest."""
        assert (
            asyncio.run(
                pkg.stream_download(entrance, output_path=self.path_out),
            )
            .absolute()
            .is_file()
            == expected
        )

    @pytest.mark.parametrize(
        'entrance',
        [
            pytest.param(x, marks=[pytest.mark.offci, pytest.mark.webtest])
            for x in pkg.URLS
        ],
    )
    def test_2(self, entrance) -> NoReturn:
        """Unittest."""
        assert asyncio.run(
            pkg.stream_download(entrance, output_path=self.path_out),
        ).is_file()

    @pytest.mark.parametrize(
        'entrance',
        [
            pytest.param(x, marks=[pytest.mark.offci, pytest.mark.webtest])
            for x in pkg.URLS
        ],
    )
    def test_3(self, entrance) -> NoReturn:
        """Unittest."""
        assert pkg.async_download(entrance)


pkg.ic.disable()
