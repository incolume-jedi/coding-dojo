"""Test module."""

from typing import NoReturn, ClassVar
import incolume.py.coding_dojo_jedi.dojo20240608 as pkg
import pytest


class TestCase:
    """Test case class."""

    case_test_0: ClassVar = [
        (1_125_721, 1061),
        (1, 1),
        (4, 2),
        (9, 3),
        (121, 11),
        (144, 12),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        case_test_0,
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        case_test_0,
    )
    def test_1(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.raiz(entrance) == expected
