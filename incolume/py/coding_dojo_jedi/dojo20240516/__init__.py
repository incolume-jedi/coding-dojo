"""Module."""

import heapq

__author__ = '@britodfbr'  # pragma: no cover


def two_sum0(array: list, target: int) -> list[int, int]:
    """Localiza indice dos elementos que atingem o valor de target.

    implementação O(n^2)
    """
    for idm, m in enumerate(array):
        for idn, n in enumerate(array):
            if m + n == target:
                return [idm, idn]
    return []


def two_sum(array: list, target: int) -> list[int, int]:
    """Localiza indice dos elementos que atingem o valor de target.

    implementação O(n)
    """
    mhash = {}
    for idm, m in enumerate(array):
        diff = target - m
        if diff in mhash:
            return [mhash[diff], idm]
        mhash[m] = idm
    return []


def inverter_names(names_list: list) -> list[str]:
    """Iverter names."""
    return [name[::-1].capitalize() for name in names_list]


def classify(quantia: int = 1, array: list | None = None) -> tuple:
    """Classifica maior e menor."""
    array = array or []
    if quantia > len(array):
        return ()
    return heapq.nlargest(quantia, array), heapq.nsmallest(quantia, array)
