"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20250104 as pkg
import pytest
import tempfile
from pathlib import Path


class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param({}, None, marks=[pytest.mark.skip]),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        result = pkg.dojo(**entrance)
        assert result == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {'url': pkg.URL, 'dir_output': Path(tempfile.gettempdir())},
                'pi-1M.tar.gz',
                marks=[],
            ),
            pytest.param(
                {'dir_output': Path(tempfile.gettempdir())},
                'pi-1M.tar.gz',
                marks=[],
            ),
            pytest.param({}, 'pi-1M.tar.gz', marks=[]),
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
                b'3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067',
                marks=[pytest.mark.skip(reason='Big File.')],
            ),
        ],
    )
    def test_handler_file(self, entrance, expected):
        """Unittest."""
        assert pkg.handler_file(**entrance) == expected
