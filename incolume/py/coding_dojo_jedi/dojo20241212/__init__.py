"""dojo module."""

from typing import TypeAlias

import numpy as np


class SudokuSolver:
    """Sudoku solutions."""

    Board: TypeAlias = list[list[str]]

    def __to_ndarray(self, sudoku: Board) -> np.ndarray:
        """ND Array."""
        return np.array(sudoku).reshape([9, 9])

    def check_quadrant(self, sudoku: Board, x: int, y: int) -> Board:
        """Check quadrant."""
        sudoku = self.__to_ndarray(sudoku)
        xx = x // 3
        yy = y // 3
        return sudoku[xx * 3 : (xx + 1) * 3, yy * 3 : (yy + 1) * 3]


def dojo(*args: str, **kwargs: str) -> dict[str]:
    """Dojo solution."""
    kwargs['args'] = args
    return kwargs
