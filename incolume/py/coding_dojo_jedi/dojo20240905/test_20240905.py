"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20240905 as pkg
import pytest


class TestCase:
    """Test case class."""

    entrances: ClassVar = [
        pytest.param('79927398713', True),
        pytest.param(79927398713, True),
        pytest.param(17893729974, True),
        pytest.param(98765432103, True),
        pytest.param(98765432104, False),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param('79927398713', True),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.check_luhn_0(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        entrances,
    )
    def test_1(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.check_luhn_1(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        entrances,
    )
    def test_2(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.check_luhn(entrance) == expected
