"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241127 as pkg
import pytest


class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                '',
                {
                    'match': 'Quantidade insuficiente de números',
                    'expected_exception': ValueError,
                },
                marks=[],
            ),
            pytest.param(
                '11.222.333',
                {
                    'match': 'Quantidade insuficiente de números',
                    'expected_exception': ValueError,
                },
                marks=[],
            ),
            pytest.param(
                '11222333abcd',
                {
                    'match': 'Quantidade insuficiente de números',
                    'expected_exception': ValueError,
                },
                marks=[],
            ),
            pytest.param('11.222.333/0001', 81, marks=[]),
            pytest.param('112223330001', 81, marks=[]),
            pytest.param(112223330001, 81, marks=[]),
            pytest.param('     112223330001     ', 81, marks=[]),
            pytest.param('     11 222 333 0001     ', 81, marks=[]),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        if isinstance(expected, dict):
            with pytest.raises(**expected):
                pkg.dojo(entrance)
        else:
            assert pkg.dojo(entrance) == expected
