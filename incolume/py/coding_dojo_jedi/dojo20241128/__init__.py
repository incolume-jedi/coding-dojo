"""dojo module."""

from __future__ import annotations

from typing import TypeAlias

import numpy as np
from icecream import ic

Board: TypeAlias = list[list[str | int]]


def is_valid_sudoku(sudoku: Board) -> bool:
    """Is validate sudoku."""
    return False or sudoku


class Solution1:
    """Tratativa 2."""

    def to_ndarray(self, sudoku: Board) -> np.ndarray:
        """ND Array."""
        return np.array(sudoku).reshape([9, 9])

    def is_valid(self, sudoku: Board, x: int, y: int, value: int) -> bool:
        """Is valid."""
        sudoku = self.to_ndarray(sudoku)
        ic(sudoku[x, :])
        ic(sudoku[:, y])
        return (
            value not in sudoku[x, :]
            and value not in sudoku[:, y]
            and value not in self.quadrant(sudoku, x, y)
        )

    def quadrant(self, sudoku: Board, x: int, y: int) -> Board:
        """Quadrant."""
        sudoku = self.to_ndarray(sudoku)
        xx = x // 3
        yy = y // 3
        result = sudoku[xx * 3 : (xx + 1) * 3, yy * 3 : (yy + 1) * 3]
        ic(result, type(result))
        return result

    def possibilities(self, sudoku: Board, x: int, y: int) -> Board:
        """Possibilities."""
        sudoku = self.to_ndarray(sudoku)
        return [
            value
            for value in range(1, 10)
            if self.is_valid(sudoku, x, y, value)
        ]

    def solver(self, sudoku: Board, solutions: list[Board]) -> list[Board]:
        """Solver."""
        sudoku = self.to_ndarray(sudoku)
        for (x, y), value in np.ndenumerate(sudoku):
            if value == 0:
                for possibility in self.possibilities(sudoku, x, y):
                    sudoku[x, y] = possibility
                    self.solver(sudoku, solutions)
                    sudoku[x, y] = 0
                return
        solutions.append(sudoku.copy())


class Solution0:
    """Tratativa 1."""

    # N is the size of the 2D matrix   N*N
    N = 9

    # A utility function to print grid
    def printing(self, arr):
        """Printing."""
        for i in range(self.N):
            for j in range(self.N):
                ic(f'{arr[i][j]} ')
            ic()

    def is_safe(self, grid, row, col, num):  # noqa: C901
        """Checks whether it will be.

        legal to assign num to the
        given row, col
        """
        # Check if we find the same num
        # in the similar row , will return false
        for x in range(9):
            if grid[row][x] == num:
                return False

        # Check if we find the same num in
        # the similar column , will return false
        for x in range(9):
            if grid[x][col] == num:
                return False

        # Check if we find the same num in
        # the particular 3*3 matrix, will return false
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve_sudoku(self, grid, row, col):  # noqa: C901
        """Solver sudoku.

        Takes a partially filled-in grid and attempts
        to assign values to all unassigned locations in
        such a way to meet the requirements for
        Sudoku solution (non-duplication across rows,
        columns, and boxes) */.
        """
        # Check if we have reached the 8th
        # row and 9th column (0
        # indexed matrix) , we are
        # returning true to avoid
        # further backtracking
        if row == self.N - 1 and col == self.N:
            return True

        # Check if column value  becomes 9 ,
        # we move to next row and
        # column start from 0
        if col == self.N:
            row += 1
            col = 0

        # Check if the current position of
        # the grid already contains
        # value >0, we iterate for next column
        if grid[row][col] > 0:
            return self.solve_sudoku(grid, row, col + 1)
        for num in range(1, self.N + 1, 1):
            # Check if it is safe to place
            # the num (1-9)  in the
            # given row ,col  ->we
            # move to next column
            if self.is_safe(grid, row, col, num):
                # Assigning the num in
                # the current (row,col)
                # position of the grid
                # and assuming our assigned
                # num in the position
                # is correct
                grid[row][col] = num

                # Checking for next possibility with next
                # column
                if self.solve_sudoku(grid, row, col + 1):
                    return True

            # Removing the assigned num ,
            # since our assumption
            # was wrong , and we go for
            # next assumption with
            # diff num value
            grid[row][col] = 0
        return False

    def run(self):
        """Run it."""
        # Driver Code

        # 0 means unassigned cells
        grid = [
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

        if self.solve_sudoku(grid, 0, 0):
            self.printing(grid)
        else:
            ic('no solution  exists ')

            # This code is contributed by sudhanshgupta2019a


def dojo(sudoku: Board) -> dict[str]:
    """Dojo solution."""
    return is_valid_sudoku(sudoku)
