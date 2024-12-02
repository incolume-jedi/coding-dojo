"""dojo module.

Para executar este dojo, faz-se necessário proceder
com os passos descritos no README.md,
referentes a `Exclusivo para Python 3.13`
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    """Example1."""

    name: str
    cost: float


def dojo(name: str, cost: float) -> Item:
    """Dojo solution."""
    return Item(name, cost)
