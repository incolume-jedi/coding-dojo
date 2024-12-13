"""dojo module."""

from typing import TypeAlias

import numpy as np
from icecream import ic


class SudokuSolver:
    """Sudoku solutions."""

    Board: TypeAlias = list[list[str]]

    def __to_ndarray(self, sudoku: Board) -> np.ndarray:
        """ND Array."""
        sudoku = np.array(sudoku).reshape([9, 9])
        sudoku = np.strings.replace(sudoku, '.', 0)
        sudoku = sudoku.astype(int)
        ic(sudoku)
        return sudoku


    def check_quadrant(self, sudoku: Board, x: int, y: int) -> Board:
        """Check quadrant."""
        sudoku = self.__to_ndarray(sudoku)
        xx = x // 3
        yy = y // 3
        return sudoku[xx * 3 : (xx + 1) * 3, yy * 3 : (yy + 1) * 3]

    def is_valid(self, sudoku: Board, x: int, y: int, value: int) -> bool:
        """Check sudoku is valid."""
        sudoku = self.__to_ndarray(sudoku)
        ic(sudoku)
        return (
            value not in sudoku[x, :]
            and value not in sudoku[:, y]
            and value not in self.check_quadrant(sudoku, x, y)
        )


def dojo(*args: str, **kwargs: str) -> dict[str]:
    """Dojo solution."""
    kwargs['args'] = args
    return kwargs
