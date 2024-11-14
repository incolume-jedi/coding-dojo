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

    def test_0(self):
        """Unittest."""
        assert pkg.sync_download(
            pkg.URLS[0],
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
        pkg.URLS,
    )
    def test_2(self, entrance) -> NoReturn:
        """Unittest."""
        assert asyncio.run(
            pkg.stream_download(entrance, output_path=self.path_out),
        ).is_file()

    @pytest.mark.parametrize(
        'entrance',
        pkg.URLS,
    )
    def test_3(self, entrance) -> NoReturn:
        """Unittest."""
        assert pkg.async_download(entrance)


pkg.ic.disable()
