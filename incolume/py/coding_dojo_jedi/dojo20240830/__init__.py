"""dojo module."""

import logging
from collections import defaultdict


def view(greetting: str = '') -> str:
    """Frontend."""
    greetting = (
        greetting
        or 'Digite a string no qual quer ler quais letras'
        ' do alfabetos elas possui: '
    )
    return input(greetting)


def dojo(frase: str) -> dict:
    """Solution dojo."""
    logging.debug('%s', frase)
    result = defaultdict(int)
    for char in frase:
        result[char] += 1
    return result
