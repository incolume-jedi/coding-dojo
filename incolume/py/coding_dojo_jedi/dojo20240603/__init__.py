"""dojo module."""

from functools import lru_cache

from icecream import ic

raizes = {1: 1}


@lru_cache
def dojo(num: int, cache: dict | None = None) -> int:
    """Raiz metodo julia."""
    cache = cache or raizes
    while 1:
        if num in cache:
            return cache.get(num)
        k, v = max(cache.items())
        cache[k + v * 2 + 1] = v + 1
        ic(cache)
    return -1
