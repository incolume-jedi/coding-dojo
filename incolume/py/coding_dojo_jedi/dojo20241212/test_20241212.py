"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241212 as pkg
import pytest
import numpy as np
from icecream import ic


class TestSolucionadorSudoku:
    """Test case class."""

    obj: pkg.SudokuSolver = pkg.SudokuSolver()
    matrizes: ClassVar[list[pkg.Board]] = [
        [
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '6', '.', '.', '3', '.', '.'],
            ['4', '.', '.', '8', '.', '3', '.', '1', '.'],
            ['7', '.', '.', '.', '2', '.', '.', '6', '.'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '4', '1', '9', '.', '.', '5', '.'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
        ],
        [
            ['5', '3', '4', '6', '7', '8', '9', '1', '0'],
            ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
            ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
            ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
            ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
            ['7', '1', ' 3', '9', '2', '4', '8', '5', '6'],
            ['9', '6', '1', '5', '3', ' 7', '2', '8', '4'],
            ['2', '8', '7', '4', '1', '9', '6', '3', ' 5'],
            ['3', '4', '5', '2', '8', '6', '1', '7', '9'],
        ],
        [
            ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
            ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
            ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
            ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
            ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
            ['7', '1', ' 3', '9', '2', '4', '8', '5', '6'],
            ['9', '6', '1', '5', '3', ' 7', '2', '8', '4'],
            ['2', '8', '0', '4', '1', '9', '6', '3', ' 5'],
            ['3', '4', '5', '2', '8', '6', '1', '7', '9'],
        ],
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {
                    'sudoku': matrizes[0],
                    'x': 2,
                    'y': 5,
                },
                [
                    [0, 7, 0],
                    [1, 9, 5],
                    [0, 0, 0],
                ],
            ),
            pytest.param(
                {
                    'sudoku': matrizes[0],
                    'x': 1,
                    'y': 3,
                },
                [
                    [0, 7, 0],
                    [1, 9, 5],
                    [0, 0, 0],
                ],
            ),
            pytest.param(
                {
                    'sudoku': matrizes[0],
                    'x': 2,
                    'y': 3,
                },
                [
                    [0, 7, 0],
                    [1, 9, 5],
                    [0, 0, 0],
                ],
            ),
            pytest.param(
                {
                    'sudoku': matrizes[0],
                    'x': 0,
                    'y': 3,
                },
                [
                    [0, 7, 0],
                    [1, 9, 5],
                    [0, 0, 0],
                ],
            ),
            pytest.param(
                {
                    'sudoku': matrizes[0],
                    'x': 0,
                    'y': 0,
                },
                [
                    [5, 3, 0],
                    [6, 0, 0],
                    [0, 9, 8],
                ],
            ),
        ],
    )
    def test_quadrante(self, entrance, expected) -> NoReturn:
        """Unittest."""
        response = self.obj.check_quadrant(**entrance)
        ic(response)
        ic(expected)
        assert np.array_equal(response, expected)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {
                    'sudoku': matrizes[0],
                    'x': 0,
                    'y': 2,
                    'value': 9,
                },
                False,
                marks=[],
            ),
            pytest.param(
                {
                    'sudoku': matrizes[0],
                    'x': 0,
                    'y': 2,
                    'value': 3,
                },
                False,
            ),
            pytest.param(
                {
                    'sudoku': matrizes[0],
                    'x': 0,
                    'y': 2,
                    'value': 5,
                },
                False,
            ),
            pytest.param(
                {
                    'sudoku': matrizes[0],
                    'x': 0,
                    'y': 2,
                    'value': 7,
                },
                False,
            ),
            pytest.param(
                {
                    'sudoku': matrizes[0],
                    'x': 0,
                    'y': 2,
                    'value': 2,
                },
                True,
                marks=[],
            ),
            pytest.param(
                {
                    'sudoku': matrizes[0],
                    'x': 0,
                    'y': 2,
                    'value': 1,
                },
                True,
                marks=[],
            ),
        ],
    )
    def test_is_valid(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert self.obj.is_valid(**entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {
                    'sudoku': matrizes[0],
                    'x': 0,
                    'y': 1,
                },
                [1, 2, 4],
                marks=[],
            ),
            pytest.param(
                {
                    'sudoku': matrizes[0],
                    'x': 2,
                    'y': 1,
                },
                [1, 2, 4, 7],
                marks=[],
            ),
            pytest.param(
                {
                    'sudoku': matrizes[0],
                    'x': 1,
                    'y': 4,
                },
                [3, 4],
                marks=[],
            ),
            pytest.param(
                {
                    'sudoku': matrizes[0],
                    'x': 3,
                    'y': 3,
                },
                [4, 5, 7, 9],
                marks=[],
            ),
            pytest.param(
                {
                    'sudoku': matrizes[0],
                    'x': 5,
                    'y': 5,
                },
                [1, 4, 9],
                marks=[],
            ),
            pytest.param(
                {
                    'sudoku': matrizes[0],
                    'x': 7,
                    'y': 1,
                },
                [2, 7, 8],
                marks=[],
            ),
        ],
    )
    def test_possibilities(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert self.obj.possibilities(**entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                matrizes[1],
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9],
                ],
            ),
            pytest.param(
                matrizes[2],
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9],
                ],
            ),
        ],
    )
    def test_solver(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert np.array_equal(self.obj.solver(entrance), [expected])
