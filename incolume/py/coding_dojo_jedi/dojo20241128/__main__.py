"""Main module.

solution adapted from https://bvanelli.github.io/2020/03/15/resolvendo-problemas-com-python/
"""

from __future__ import annotations

from typing import TypeAlias

import numpy as np
from icecream import ic

Board: TypeAlias = list[list[str]]


def is_valid(sudoku: Board, x: int, y: int, value: int) -> bool:
    """Is valid."""
    return (
        value not in sudoku[x, :]
        and value not in sudoku[:, y]
        and value not in quadrant(sudoku, x, y)
    )


def quadrant(sudoku: Board, x: int, y: int) -> Board:
    """Quadrant."""
    xx = x // 3
    yy = y // 3
    return sudoku[xx * 3 : (xx + 1) * 3, yy * 3 : (yy + 1) * 3]


def possibilities(sudoku: Board, x: int, y: int) -> Board:
    """Possibilities."""
    return [value for value in range(1, 10) if is_valid(sudoku, x, y, value)]


def solver(sudoku: Board, solutions: list[Board]) -> list[Board]:
    """Solver."""
    for (x, y), value in np.ndenumerate(sudoku):
        if value == 0:
            for possibility in possibilities(sudoku, x, y):
                sudoku[x, y] = possibility
                solver(sudoku, solutions)
                sudoku[x, y] = 0
            return
    solutions.append(sudoku.copy())


if __name__ == '__main__':
    sudoku = np.array([
        5,
        3,
        0,
        0,
        7,
        0,
        0,
        0,
        0,
        6,
        0,
        0,
        1,
        9,
        5,
        0,
        0,
        0,
        0,
        9,
        8,
        0,
        0,
        0,
        0,
        6,
        0,
        8,
        0,
        0,
        0,
        6,
        0,
        0,
        0,
        3,
        4,
        0,
        0,
        8,
        0,
        3,
        0,
        0,
        1,
        7,
        0,
        0,
        0,
        2,
        0,
        0,
        0,
        6,
        0,
        6,
        0,
        0,
        0,
        0,
        2,
        8,
        0,
        0,
        0,
        0,
        4,
        1,
        9,
        0,
        0,
        5,
        0,
        0,
        0,
        0,
        8,
        0,
        0,
        7,
        9,
    ]).reshape([9, 9])
    solutions = []
    solver(sudoku, solutions)
    for solution in solutions:
        ic(solution)
