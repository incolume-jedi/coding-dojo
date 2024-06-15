"""dojo module."""

import logging
import os
import time
from collections.abc import Callable
from functools import wraps

from icecream import ic

ic.disable()
if os.getenv('DEBUG_MODE'):
    ic.enable()


def calc_square0(l: list) -> list:  # noqa: E741
    """Quadrado de cada elemento da lista."""
    start = time.time()
    result = []
    for e in l:
        result.append(e * e)  # noqa: PERF401
    end = time.time()
    logging.debug('calc_square executou em %s milisegundos', start - end)
    return result


def calc_cube0(l: list) -> list:  # noqa: E741
    """Cubo de cada elemento da lista."""
    start = time.time()
    result = []
    for e in l:
        result.append(e * e * e)  # noqa: PERF401
    end = time.time()
    logging.debug('calc_cube executou em %s milisegundos', start - end)
    return result


def timeit(func: Callable) -> Callable:
    """Timeit."""

    @wraps(func)
    def inner(*args, **kwargs):
        """Inner function."""
        start = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end = time.perf_counter_ns()
        msg = '%s executou em %s milisegundos'
        logging.debug(msg, func.__name__, end - start)
        return result

    return inner


def calc_pow_list(lst: list, exp: int) -> list:
    """Potência de cada elemento da lista."""
    return [pow(x, exp) for x in lst]


@timeit
def calc_square(lst: list) -> list:
    """Quadrado de cada elemento da lista."""
    return calc_pow_list(lst, 2)


@timeit
def calc_cube(lst: list) -> list:
    """Cubo de cada elemento da lista."""
    return calc_pow_list(lst, 3)


if __name__ == '__main__':
    ic(calc_square(range(1, 4)))
    ic(calc_cube(range(1, 4)))
