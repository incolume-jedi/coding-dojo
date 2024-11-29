"""dojo module."""

from __future__ import annotations

from typing import TypeAlias

Board: TypeAlias = list[list[str]]


def quadrant(sudoku: Board, x: int, y: int) -> Board:
    """Find quadrant."""
    xx = x // 3
    yy = y // 3
    return sudoku[xx * 3 : (xx + 1) * 3, yy * 3 : (yy + 1) * 3]


def is_valid_sudoku(sudoku: Board) -> bool:
    """Is validate sudoku."""
    return False or sudoku


def dojo(sudoku: Board) -> dict[str]:
    """Dojo solution."""
    return is_valid_sudoku(sudoku)
