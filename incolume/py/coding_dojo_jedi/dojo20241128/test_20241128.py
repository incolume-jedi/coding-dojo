"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241128 as pkg
import pytest
import numpy as np
from icecream import ic
from itertools import chain


class TestCase0:
    """Test case class."""

    t0: ClassVar = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0],
    ]
    t1: ClassVar = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    obj = pkg.Solution1()

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                (t0, 1, 1),
                [[3, 0, 6], [5, 2, 0], [0, 8, 7]],
                marks=[],
            ),
            pytest.param((t0, 1, 4), [5, 0, 8, 0, 0, 0, 0, 0, 0], marks=[]),
            pytest.param((t0, 3, 3), [4, 0, 0, 0, 0, 0, 0, 3, 1], marks=[]),
            pytest.param((t0, 5, 5), [5, 0, 8, 0, 0, 0, 0, 0, 0], marks=[]),
            pytest.param((t0, 1, 1), [2, 5, 0, 0, 7, 4, 3, 0, 0], marks=[]),
        ],
    )
    def test_solution1_quadrant(self, entrance, expected) -> NoReturn:
        """Unittest."""
        expected = np.array(expected)
        r = self.obj.quadrant(*entrance)
        assert isinstance(expected, np.ndarray)
        assert isinstance(r, np.ndarray)
        assert r.all() == expected.all()

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param((t0, 0, 1, 1), True, marks=[]),
            pytest.param((t0, 2, 1, 8), False, marks=[]),
            pytest.param((t0, 1, 4, 1), False, marks=[]),
            pytest.param((t0, 3, 3, 1), False, marks=[]),
            pytest.param((t0, 5, 5, 1), False, marks=[]),
            pytest.param((t0, 7, 1, 1), False, marks=[]),
        ],
    )
    def test_solution1_is_valid(self, entrance, expected) -> NoReturn:
        """Unittest."""
        ic()
        ic(entrance[0])
        assert self.obj.is_valid(*entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param((t0, 0, 1), [1, 9], marks=[]),
            pytest.param((t0, 2, 1), [4, 9], marks=[]),
            pytest.param((t0, 1, 4), [3, 4, 7], marks=[]),
            pytest.param((t0, 3, 3), [4, 7], marks=[]),
            pytest.param((t0, 5, 5), [2, 4, 7], marks=[]),
            pytest.param((t0, 7, 1), [6, 9], marks=[]),
        ],
    )
    def test_solution1_possibilities(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert self.obj.possibilities(*entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 2, 6, 7, 5, 1, 4, 9, 3],
                    [4, 5, 9, 8, 6, 3, 7, 2, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 0],
                ],
                [
                    np.array([
                        [5, 3, 4, 6, 7, 8, 9, 1, 2],
                        [6, 7, 2, 1, 9, 5, 3, 4, 8],
                        [1, 9, 8, 3, 4, 2, 5, 6, 7],
                        [8, 2, 6, 7, 5, 1, 4, 9, 3],
                        [4, 5, 9, 8, 6, 3, 7, 2, 1],
                        [7, 1, 3, 9, 2, 4, 8, 5, 6],
                        [9, 6, 1, 5, 3, 7, 2, 8, 4],
                        [2, 8, 7, 4, 1, 9, 6, 3, 5],
                        [3, 4, 5, 2, 8, 6, 1, 7, 9],
                    ]),
                ],
                marks=[],
            ),
            pytest.param(
                [
                    [
                        [5, 3, 4, 6, 7, 8, 9, 1, 0],
                        [6, 7, 2, 1, 9, 5, 3, 4, 8],
                        [1, 9, 8, 3, 4, 2, 5, 6, 7],
                        [8, 5, 9, 7, 0, 1, 4, 2, 3],
                        [4, 2, 6, 8, 5, 3, 7, 9, 1],
                        [7, 1, 3, 9, 2, 4, 8, 5, 6],
                        [9, 6, 1, 5, 3, 7, 2, 8, 4],
                        [2, 8, 7, 4, 1, 9, 6, 3, 5],
                        [3, 4, 5, 2, 8, 6, 1, 7, 9],
                    ],
                ],
                [
                    np.array([
                        [5, 3, 4, 6, 7, 8, 9, 1, 2],
                        [6, 7, 2, 1, 9, 5, 3, 4, 8],
                        [1, 9, 8, 3, 4, 2, 5, 6, 7],
                        [8, 5, 9, 7, 6, 1, 4, 2, 3],
                        [4, 2, 6, 8, 5, 3, 7, 9, 1],
                        [7, 1, 3, 9, 2, 4, 8, 5, 6],
                        [9, 6, 1, 5, 3, 7, 2, 8, 4],
                        [2, 8, 7, 4, 1, 9, 6, 3, 5],
                        [3, 4, 5, 2, 8, 6, 1, 7, 9],
                    ]),
                ],
                marks=[],
            ),
        ],
    )
    def test_solution1_solver(self, entrance, expected) -> NoReturn:
        """Unittest."""
        result = self.obj.solver(entrance)
        assert len(result) == len(expected)
        result1 = [list(chain(*x)) for x in result]
        assert result1 == [list(chain(*x)) for x in expected]


class TestCase1:
    """Test case class."""

    __test__ = False

    t0: ClassVar = [
        pytest.param(
            [
                [3, 0, 6, 5, 0, 8, 4, 0, 0],
                [5, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 8, 7, 0, 0, 0, 0, 3, 1],
                [0, 0, 3, 0, 1, 0, 0, 8, 0],
                [9, 0, 0, 8, 6, 3, 0, 0, 5],
                [0, 5, 0, 0, 9, 0, 6, 0, 0],
                [1, 3, 0, 0, 0, 0, 2, 5, 0],
                [0, 0, 0, 0, 0, 0, 0, 7, 4],
                [0, 0, 5, 2, 0, 6, 3, 0, 0],
            ],
            True,
            marks=[],
        ),
        pytest.param(
            [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9],
            ],
            True,
        ),
        pytest.param(
            [
                ['8', '3', '.', '.', '7', '.', '.', '.', '.'],
                ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
                ['.', '9', '8', '.', '.', '.', '6', '.', '.'],
                ['8', '.', '.', '.', '6', '.', '.', '3', '.'],
                ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
                ['7', '.', '.', '.', '2', '.', '.', '6', '.'],
                ['.', '6', '.', '.', '.', '2', '8', '.', '.'],
                ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
                ['.', '.', '.', '.', '8', '.', '7', '9', '.'],
            ],
            True,
            marks=[],
        ),
        pytest.param(
            [
                ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
                ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
                ['.', '9', '8', '.', '.', '.', '6', '.', '.'],
                ['8', '.', '.', '.', '6', '.', '.', '3', '.'],
                ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
                ['7', '.', '.', '.', '2', '.', '.', '6', '.'],
                ['.', '6', '.', '.', '.', '2', '8', '.', '.'],
                ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
                ['.', '.', '.', '.', '8', '.', '7', '9', '.'],
            ],
            True,
            marks=[],
        ),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        t0,
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(entrance) == expected
