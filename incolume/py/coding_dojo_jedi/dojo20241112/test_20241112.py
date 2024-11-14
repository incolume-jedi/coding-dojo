"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241112 as pkg
import pytest
import asyncio

pkg.ic.enable()


class TestCase0:
    """Test case class."""

    url: ClassVar = 'https://download.freebsd.org/ftp/releases/amd64/amd64/ISO-IMAGES/12.0/FreeBSD-12.0-RELEASE-amd64-mini-memstick.img'

    def test_0(self):
        """Unittest."""
        assert pkg.async_stream(pkg.URLS[0])


class TestCase1:
    """Test case class."""

    t0: ClassVar = None
    t1: ClassVar = [
        'https://httpbin.org',
    ]

    def test_0(self):
        """Unittest."""
        assert pkg.sync_download(pkg.URLS[0]).is_file()

    def test_1(self):
        """Unittest."""
        assert asyncio.run(pkg.stream_download(pkg.URLS[2])).absolute() == ''

    @pytest.mark.parametrize(
        'entrance',
        pkg.URLS,
    )
    def test_2(self, entrance) -> NoReturn:
        """Unittest."""
        assert pkg.sync_download(entrance).is_file()

    @pytest.mark.skip
    @pytest.mark.parametrize(
        'entrance',
        pkg.URLS,
    )
    def test_3(self, entrance) -> NoReturn:
        """Unittest."""
        assert pkg.async_download(entrance)


# pkg.ic.disable()  # noqa: ERA001
