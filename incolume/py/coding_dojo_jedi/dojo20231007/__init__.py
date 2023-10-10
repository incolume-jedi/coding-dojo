"""Dojo 20231009."""

from collections.abc import Iterable
from sys import maxsize


def max_sequence(lista: list) -> int:  # noqa: C901
    """_Soma os valores dentro de um array."""
    soma = 0
    resultado = []

    for x in lista:
        resultado.append(x < 0)  # noqa: PERF401

    if all(resultado):
        return 0

    resultado.clear()
    for y in lista:
        resultado.append(y >= 0)  # noqa: PERF401

    if all(resultado):
        soma = 0
        for numero in lista:
            soma = soma + numero
        return soma
    # [-2, 1, -3, 4, -1, 2, 1, -5, 4]  noqa: ERA001
    # 4, -1, 2, 1,
    # [10, -11, 2, 3, 4, 5, -5,  6, 7, -50, 8,-7, 9]   noqa: ERA001
    # 2, 3, 4, 5,
    return soma


def subarray_max_sum(array: Iterable) -> int:
    """Subarray de soma maxima."""
    soma, result = 0, 0
    if all(x < 0 for x in array):
        return soma
    if all(x >= 0 for x in array):
        return sum(array)

    for value in array:
        soma += value
        soma = max(0, soma)
        if soma > result:
            result = soma
    return result


def max_sub_array_sum(a: list) -> int:
    """Python program to print largest contiguous array sum.

    Function to find the maximum contiguous subarray
    and print its starting and end index

    https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
    """
    size = len(a)
    max_so_far = -maxsize - 1
    max_ending_here = 0

    for i in range(size):
        max_ending_here += a[i]
        max_so_far = max(max_so_far, max_ending_here)
        max_ending_here = max(0, max_ending_here)
    return max(0, max_so_far)

def max_subarray_sum(array: list) -> int:
    """refactory max_sub_array_sum."""
    max_so_far, max_ending_here = -maxsize - 1, 0

    for value in array:
        max_ending_here += value
        max_so_far = max(max_so_far, max_ending_here)
        max_ending_here = max(0, max_ending_here)
    return max(0, max_so_far)
