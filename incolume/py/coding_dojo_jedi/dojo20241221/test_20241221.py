"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241221 as pkg
import pytest


class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param([3], 3, marks=[]),
            pytest.param([3, 1], 5, marks=[]),
            pytest.param([3, 1, 2], 9, marks=[pytest.mark.skip]),
            pytest.param([3, 1, 2, 4], 17, marks=[pytest.mark.skip]),
            pytest.param([11, 81, 94, 43, 3], 444, marks=[]),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param([3], 3, marks=[]),
            pytest.param([3, 1], 5, marks=[]),
            pytest.param([3, 1, 2], 9, marks=[]),
            pytest.param([3, 1, 2, 4], 17, marks=[]),
            pytest.param([11, 81, 94, 43, 3], 444, marks=[]),
        ],
    )
    def test_1(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.sum_subarray_mins(entrance) == expected
