"""dojo module."""

from incolume.py.coding_dojo_jedi.dojo20240510 import is_narcisist


def dojo(digits: int) -> list[int]:
    """Dojo implementation."""
    return [n for n in range(10**digits) if is_narcisist(n)]
