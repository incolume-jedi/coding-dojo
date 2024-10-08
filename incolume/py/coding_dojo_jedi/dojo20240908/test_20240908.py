"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20240908 as pkg
import pytest


class TestCase:
    """Test case class."""

    test5: ClassVar = [
        (5061, 5),
        (5062, 0),
    ]
    test7: ClassVar = [
        (1, 7),
        (2, 9),
        (3, 3),
        (4, 1),
        (7063, 3),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (12, True),
            (123, False),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.is_even(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test5,
    )
    def test_1(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.last_digit_for_pow5(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test5,
    )
    def test_2(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.last_digit_for_pow5(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test7,
    )
    def test_3(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.last_digit_for_pow7_0(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test7,
    )
    def test_4(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.last_digit_for_pow7(entrance) == expected
