"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240705 as pkg
import pytest


class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(5, 20, marks=[pytest.mark.slow]),
            pytest.param(1, 10, marks=[]),
            pytest.param(2, 10, marks=[]),
            pytest.param(3, 14, marks=[]),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert len(pkg.dojo(entrance)) == expected
