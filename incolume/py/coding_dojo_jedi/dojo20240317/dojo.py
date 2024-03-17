"""Dojo realizado em 17 Mar 2024."""

__author__ = "@britodfbr"  # pragma: no cover


def perimeter(matriz: list[list, ...]) -> int:
    """Perimeter for matrix."""
    limits = 2, 100

    if len(matriz) == 0:
        return 0

    n = len(matriz)
    m = len(matriz[0])

    if n < limits[0]:
        raise ValueError

    if m > limits[-1]:
        raise ValueError

    perim = sum(matriz[0][1:-1]) + sum(matriz[-1][1:-1])

    for i in range(n):
        perim += matriz[i][0] + matriz[i][-1]

    return perim
