"""Test module."""

from typing import ClassVar
import incolume.py.coding_dojo_jedi.dojo20250104 as pkg
import pytest
import tempfile
from pathlib import Path
import tarfile
import httpx
import respx
from http import HTTPStatus
from incolume.py.coding_dojo_jedi.utils import check_connectivity


class TestCase:
    """Test case class."""

    t0: ClassVar = None
    expected_content: ClassVar[bytes] = b'3.141592'

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {
                    'url': pkg.URL_TAR_FILE,
                    'dir_output': Path(tempfile.gettempdir()),
                },
                'pi-1M.tar.gz',
                marks=[
                    pytest.mark.offci,
                    pytest.mark.webtest,
                    pytest.mark.xpass(
                        reason='failing web connection (but shoulded ran)',
                    ),
                    pytest.mark.skipif(
                        not check_connectivity(),
                        reason='failing web connection (but shoulded ran)',
                    ),
                ],
            ),
            pytest.param(
                {'dir_output': Path(tempfile.gettempdir())},
                'pi-1M.tar.gz',
                marks=[
                    pytest.mark.offci,
                    pytest.mark.webtest,
                    pytest.mark.xpass(
                        reason='failing web connection (but shoulded ran)',
                    ),
                    pytest.mark.skipif(
                        not check_connectivity(),
                        reason='failing web connection (but shoulded ran)',
                    ),
                ],
            ),
            pytest.param(
                {},
                'pi-1M.tar.gz',
                marks=[
                    pytest.mark.offci,
                    pytest.mark.webtest,
                    pytest.mark.xpass(
                        reason='failing web connection (but shoulded ran)',
                    ),
                    pytest.mark.skipif(
                        not check_connectivity(),
                        reason='failing web connection (but shoulded ran)',
                    ),
                ],
            ),
            pytest.param(
                {
                    'url': pkg.URL_RAW_FILE,
                    'fout': Path(tempfile.gettempdir()) / 'pi-1M.txt',
                },
                'pi-1M.txt',
                marks=[
                    pytest.mark.offci,
                    pytest.mark.webtest,
                    pytest.mark.xpass(
                        reason='failing web connection (but shoulded ran)',
                    ),
                    pytest.mark.skipif(
                        not check_connectivity(),
                        reason='failing web connection (but shoulded ran)',
                    ),
                ],
            ),
            pytest.param(
                {
                    'url': pkg.URL_TAR_FILE,
                    'fout': Path(tempfile.gettempdir()) / 'pi-1M.tgz',
                },
                'pi-1M.tgz',
                marks=[
                    pytest.mark.skip,
                    pytest.mark.offci,
                    pytest.mark.webtest,
                    pytest.mark.xpass(
                        reason='failing web connection (but shoulded ran)',
                    ),
                    pytest.mark.skipif(
                        not check_connectivity(),
                        reason='failing web connection (but shoulded ran)',
                    ),
                ],
            ),
        ],
    )
    def test_download(self, entrance, expected):
        """Unittest."""
        result = pkg.download_file(**entrance)
        assert expected in result.parts
        assert result.is_file()

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {'dir_output': Path(tempfile.gettempdir())},
                'pi-1M.tar.gz',
                marks=[],
            ),
            pytest.param({}, 'pi-1M.tar.gz', marks=[]),
            pytest.param(
                {
                    'url': pkg.URL_RAW_FILE,
                    'fout': Path(tempfile.gettempdir()) / 'pi-1M.txt',
                },
                'pi-1M.txt',
                marks=[],
            ),
            pytest.param(
                {
                    'url': pkg.URL_RAW_FILE,
                    'fout': Path(*pkg.__package__.split('.')) / 'pi-1M.txt',
                },
                'pi-1M.txt',
                marks=[
                    # pytest.mark.skip
                ],
            ),
        ],
    )
    def test_download_mock_raw(self, entrance, expected):
        """Unittest."""
        fmock = Path(*pkg.__package__.split('.')) / 'pi-1M.tgz'
        with (
            respx.mock() as rmock,
            tarfile.open(
                fmock,
                mode='r:gz',
            ) as handler,
        ):
            file = handler.extractfile(handler.getnames()[0])
            content = file.read()
            test_route = rmock.get(entrance.get('url')).mock(
                return_value=httpx.Response(
                    HTTPStatus.OK,
                    content=content,
                ),
            )
            result = pkg.download_file(**entrance)
            assert test_route.called
            assert expected in result.parts
            assert result.is_file()

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {
                    'url': pkg.URL_TAR_FILE,
                    'dir_output': Path(tempfile.gettempdir()),
                },
                'pi-1M.tar.gz',
                marks=[],
            ),
            pytest.param(
                {'dir_output': Path(tempfile.gettempdir())},
                'pi-1M.tar.gz',
                marks=[],
            ),
            pytest.param({}, 'pi-1M.tar.gz', marks=[]),
            pytest.param(
                {
                    'url': pkg.URL_TAR_FILE,
                    'fout': Path(tempfile.gettempdir()) / 'pi-1M.tgz',
                },
                'pi-1M.tgz',
                marks=[
                    # pytest.mark.skip
                ],
            ),
        ],
    )
    def test_download_mock_tgz(self, entrance, expected):
        """Unittest."""
        fmock = Path(*pkg.__package__.split('.')) / 'pi-1M.tgz'
        with respx.mock() as rmock:
            test_route = rmock.get(entrance.get('url')).mock(
                return_value=httpx.Response(
                    HTTPStatus.OK,
                    content=fmock.read_bytes(),
                ),
            )
            result = pkg.download_file(**entrance)
            assert test_route.called
            assert expected in result.parts
            assert result.is_file()

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {},
                b'3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706',
            ),
            pytest.param(
                {'fin': Path(tempfile.gettempdir()) / 'pi-1M.tar.gz'},
                b'3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706',
            ),
            pytest.param(
                {
                    'chunk': 101,
                    'fin': Path(tempfile.gettempdir()) / 'pi-1M.tar.gz',
                },
                b'3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067',
            ),
        ],
    )
    def test_handler_file(self, entrance, expected):
        """Unittest."""
        assert pkg.handler_file(**entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {},
                b'3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706',
            ),
            pytest.param(
                {
                    'chunk': 101,
                },
                b'3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067',
            ),
        ],
    )
    def test_handler_stream(self, entrance, expected):
        """Unittest."""
        fmock = Path(*pkg.__package__.split('.')) / 'pi-1M.tgz'
        with (
            tarfile.open(fmock, mode='r:gz') as handler,
            respx.mock() as rmock,
        ):
            file = handler.extractfile(handler.getnames()[0])
            content = file.readline()

            test_route = rmock.get(entrance.get('url', pkg.URL_RAW_FILE)).mock(
                return_value=httpx.Response(
                    HTTPStatus.OK,
                    content=content,
                ),
            )

            assert pkg.handler_stream(**entrance) == expected
            assert test_route.called

    @pytest.mark.parametrize(
        'cmd entrance'.split(),
        [
            pytest.param(
                pkg.handler_file,
                {'chunk': 1.6180},
                marks=[pytest.mark.xpass(reason='bigger file.')],
            ),
            pytest.param(
                pkg.handler_file,
                {'chunk': 'a'},
                marks=[pytest.mark.xpass(reason='bigger file.')],
            ),
            pytest.param(
                pkg.handler_file,
                {'chunk': -1},
                marks=[pytest.mark.xpass(reason='bigger file.')],
            ),
        ],
    )
    def test_handler_bigger_mock(self, cmd, entrance):
        """Unittest."""
        with tarfile.open(
            Path(*pkg.__package__.split('.')) / 'pi-1M.tgz',
            mode='r:gz',
        ) as handler:
            file = handler.extractfile(handler.getnames()[0])
            expected = file.readline()
            result = cmd(**entrance).strip()

            assert result == expected

    @pytest.mark.parametrize(
        'cmd entrance'.split(),
        [
            pytest.param(
                pkg.handler_stream,
                {'chunk': 1.6180},
                marks=[pytest.mark.xpass(reason='bigger file.')],
            ),
            pytest.param(
                pkg.handler_stream,
                {'chunk': '1k'},
                marks=[pytest.mark.xpass(reason='bigger file.')],
            ),
            pytest.param(
                pkg.handler_stream,
                {'chunk': -1},
                marks=[pytest.mark.xpass(reason='bigger file.')],
            ),
        ],
    )
    def test_handler_bigger_mock_raw(self, cmd, entrance):
        """Unittest."""
        with (
            tarfile.open(
                Path(*pkg.__package__.split('.')) / 'pi-1M.tgz',
                mode='r:gz',
            ) as handler,
            respx.mock() as mresp,
        ):
            file = handler.extractfile(handler.getnames()[0])
            expected = file.readline()

            test_route = mresp.get(entrance.get('url', pkg.URL_RAW_FILE)).mock(
                return_value=httpx.Response(
                    HTTPStatus.OK,
                    content=expected,
                ),
            )

            result = cmd(**entrance).strip()
            assert test_route.called
            assert result == expected
