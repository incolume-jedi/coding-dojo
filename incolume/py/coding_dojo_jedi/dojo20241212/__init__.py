"""dojo module."""

import contextlib
from typing import TypeAlias

import numpy as np
from icecream import ic

Board: TypeAlias = list[list[str | int]]


class SudokuSolver:
    """Sudoku solutions."""

    def __to_ndarray(self, sudoku: Board) -> np.ndarray:
        """ND Array."""
        sudoku = np.array(sudoku).reshape([9, 9])
        with contextlib.suppress(ValueError):
            sudoku = np.strings.replace(sudoku, '.', 0)
        sudoku = sudoku.astype(int)
        ic(sudoku)
        return sudoku

    def solver(
        self,
        sudoku: Board,
        solutions: None | list[Board] = None,
    ) -> list[Board]:
        """Solver."""
        solutions = solutions or []
        solution = self.__to_ndarray(sudoku)
        for (x, y), value in np.ndenumerate(solution):
            ic(x, y, value)
            if value == 0:
                ic(value)
                for possibility in self.possibilities(solution, x, y):
                    solution[x, y] = possibility
                    self.solver(solution, solutions)
        solutions.append(solution.copy())
        return solutions

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

    def possibilities(self, sudoku: Board, x: int, y: int) -> Board:
        """List possibilities."""
        return [
            value
            for value in range(1, 10)
            if self.is_valid(sudoku, x, y, value)
        ]
