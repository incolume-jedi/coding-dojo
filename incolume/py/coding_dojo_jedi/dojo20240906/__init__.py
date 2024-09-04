"""dojo module."""

from incolume.py.coding_dojo_jedi.dojo20240506 import is_feliz
from incolume.py.coding_dojo_jedi.dojo20240510 import is_narcisist
from incolume.py.coding_dojo_jedi.dojo20240517 import is_prime


def dojo(limit=10**3):
    """Solution números primos, felizes e narcisistas."""
    limit = limit or 10**3
    return [
        i
        for i in range(1, limit + 1)
        if is_prime(i) and is_feliz(i) and is_narcisist(i)
    ]
