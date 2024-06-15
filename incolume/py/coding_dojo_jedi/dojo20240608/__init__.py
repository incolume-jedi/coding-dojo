"""dojo module."""

from __future__ import annotations

from functools import lru_cache

from icecream import ic

raizes_dict = {0: 0}
raizes_list = [0]


@lru_cache
def dojo(num: int, cache: dict | None = None) -> int:
    """Raiz metodo julia."""
    cache = cache or raizes_dict
    while 1:
        if num in cache:
            ic(cache)
            return cache.get(num)
        k, v = max(cache.items())
        cache[k + v * 2 + 1] = v + 1
    return -1


def raiz(num: int, cache: list | None = None) -> int:
    """Raiz método Júlia."""
    cache = cache or raizes_list
    while 1:
        if num in cache:
            ic(cache)
            return cache.index(num)
        n = max(cache)
        idx = cache.index(n)
        cache.append(n + idx * 2 + 1)
    return -1
