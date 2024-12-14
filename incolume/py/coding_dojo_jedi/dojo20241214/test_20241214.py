"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241214 as pkg
import pytest


class TestCase:
    """Test case class."""

    obj: pkg.Solutions = pkg.Solutions()
    t0: ClassVar = [
        [2, 2, 2, 1, 1, 3, 3, 3, 3],
        [1],
        [1, 1, 1, 2, 2, 3],
        [
            7,
            1,
            1,
            8,
            0,
            1,
            1,
            1,
            1,
            9,
            2,
            2,
            2,
            6,
            6,
            2,
            3,
            3,
            5,
            5,
            5,
            5,
            5,
            5,
            5,
            4,
        ],
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param({'nums': t0[0], 'k': 2}, [3, 2]),
            pytest.param({'nums': t0[1], 'k': 1}, [1]),
            pytest.param({'nums': t0[2], 'k': 2}, [1, 2]),
            pytest.param({'nums': t0[3], 'k': 3}, [5, 1, 2]),
            pytest.param({'nums': t0[3], 'k': 4}, [5, 1, 2, 6]),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert self.obj.dojo(**entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param({'nums': t0[0], 'k': 2}, [3, 2]),
            pytest.param({'nums': t0[1], 'k': 1}, [1]),
            pytest.param({'nums': t0[2], 'k': 2}, [1, 2]),
            pytest.param({'nums': t0[3], 'k': 3}, [5, 1, 2]),
            pytest.param({'nums': t0[3], 'k': 4}, [5, 1, 2, 6]),
        ],
    )
    def test_1(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert self.obj.dojo1(**entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param({'nums': t0[0], 'k': 2}, [3, 2]),
            pytest.param({'nums': t0[1], 'k': 1}, [1]),
            pytest.param({'nums': t0[2], 'k': 2}, [1, 2]),
            pytest.param({'nums': t0[3], 'k': 3}, [5, 1, 2]),
            pytest.param({'nums': t0[3], 'k': 4}, [5, 1, 2, 6]),
        ],
    )
    def test_2(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert self.obj.dojo2(**entrance) == expected
