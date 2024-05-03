"""Dojo 20231009."""

from collections.abc import Iterable
from sys import maxsize


def max_sequence(lista: list) -> int:
    """_Soma os valores dentro de um array."""
    soma = 0
    resultado = []

    resultado.append(x for x in lista if x < 0)

    if all(resultado):
        return 0

    resultado.clear()
    resultado.append(y for y in lista if y >= 0)

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
    """Refactory max_sub_array_sum."""
    result, soma = -maxsize - 1, 0

    for value in array:
        soma += value
        result = max(result, soma)
        soma = max(0, soma)
    return max(0, result)
