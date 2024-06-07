"""dojo module."""

import logging
import time
from icecream import ic 
import os


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


def timeit(func: )