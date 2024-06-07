"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20240606 as pkg
import pytest


class TestCase:
    """Test case class."""

    case_test_square: ClassVar = [
        (range(5), [pow(x, 2) for x in range(5)]),
    ]

    case_test_cube: ClassVar = [
        (list(range(5)), [pow(x, 3) for x in range(5)]),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        case_test_square,
    )
    def test_square_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.calc_square0(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        case_test_cube,
    )
    def test_cube_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.calc_cube0(entrance) == expected
