"""dojo module."""

from __future__ import annotations

from typing import TypeAlias

from icecream import ic

Board: TypeAlias = list[list[str]]


def quadrant(sudoku: Board, x: int = 0, y: int = 0) -> Board:
    """Find quadrant."""
    xx = x // 3
    yy = y // 3
    return sudoku[xx * 3 : (xx + 1) * 3, yy * 3 : (yy + 1) * 3]


def is_valid_sudoku(sudoku: Board) -> bool:
    """Is validate sudoku."""
    return False or sudoku


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
        # in the similar row , we
        # return false
        for x in range(9):
            if grid[row][x] == num:
                return False

        # Check if we find the same num in
        # the similar column , we
        # return false
        for x in range(9):
            if grid[x][col] == num:
                return False

        # Check if we find the same num in
        # the particular 3*3 matrix,
        # we return false
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + startRow][j + startCol] == num:
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
