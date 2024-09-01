"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20240904 as pkg
import pytest


class TestCase:
    """Test case class."""

    tests: ClassVar = [
        ('mississipi', '>:DD:DD:A:'),
        ('Só Jesus salva.', '$ó y6DFD D2=G2]'),
        (
            'Tudo é difício até fácil se tornar!',
            '%F5@ é 5:7í4:@ 2Eé 7á4:= D6 E@C?2CP',
        ),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        tests,
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.rot47_0(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        tests,
    )
    def test_1(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.rot47_1(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        tests,
    )
    def test_2(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.rot47(entrance) == expected
