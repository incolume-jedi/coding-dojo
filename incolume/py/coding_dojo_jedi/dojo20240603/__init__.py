"""dojo module."""
from itertools import count
from functools import lru_cache
from icecream import ic

counter = count(1)

@lru_cache
def dojo(num: int) -> int:
    """Raiz metodo julia."""
    raizes = {1: 1, 2: 4} 
    while 1:
        if num in raizes.values():
            return raizes.get(num)
        v = max(raizes)
        raizes[ic(v * 2 + 1) ] = v
        ic(raizes)