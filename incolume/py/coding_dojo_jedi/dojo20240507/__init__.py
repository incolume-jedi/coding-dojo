"""Module dojo."""

from functools import lru_cache


@lru_cache
def is_feliz(num: int) -> bool:
    """Verifica se numero é feliz."""
    num = [pow(int(n), 2) for n in str(num)]
    if (snum := sum(num)) == 1:
        return True

    try:
        return is_feliz(snum)
    except RecursionError:
        return False


def num_feliz(num: int) -> list[int]:
    """Retorna numeros felizes menores que num."""
    return [n for n in range(num + 1) if is_feliz(n)]
