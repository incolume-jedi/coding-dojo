"""Test module."""

from typing import ClassVar
import incolume.py.coding_dojo_jedi.dojo20250104 as pkg
import pytest
import tempfile
from pathlib import Path
import tarfile


class TestCase:
    """Test case class."""

    t0: ClassVar = None
    expected_content: ClassVar[bytes] = b'3.141592'

    with tarfile.open(
        Path(*pkg.__package__.split('.')) / 'pi-1M.tgz',
        mode='r:gz',
    ) as handler:
        file = handler.extractfile(handler.getnames()[0])
        expected_content = file.read()

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
                    'url': pkg.URL_RAW_FILE,
                    'fout': Path(tempfile.gettempdir()) / 'pi-1M.txt',
                },
                'pi-1M.txt',
                marks=[],
            ),
            pytest.param(
                {
                    'url': pkg.URL_TAR_FILE,
                    'fout': Path(*pkg.__package__.split('.')) / 'pi-1M.tgz',
                },
                'pi-1M.tgz',
                marks=[
                    # pytest.mark.skip
                ],
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
    def test_download(self, entrance, expected):
        """Unittest."""
        result = pkg.download_file(**entrance)
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
            pytest.param(
                {
                    'chunk': -1,
                },
                expected_content,
                marks=[
                    # pytest.mark.skip(reason='Big File.')
                ],
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
            pytest.param(
                {
                    'chunk': -1,
                },
                expected_content,
                marks=[pytest.mark.skip(reason='Big File.')],
            ),
            pytest.param(
                {'chunk': 1.0},
                expected_content,
                marks=[pytest.mark.skip(reason='Big File.')],
            ),
            pytest.param(
                {'chunk': 'a'},
                expected_content,
                marks=[pytest.mark.skip(reason='Big File.')],
            ),
        ],
    )
    def test_handler_stream(self, entrance, expected):
        """Unittest."""
        assert pkg.handler_stream(**entrance) == expected
