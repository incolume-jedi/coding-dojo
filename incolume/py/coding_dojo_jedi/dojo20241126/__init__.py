"""dojo module."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    """Example1."""

    name: str
    cost: float


def dojo(name: str, cost: float) -> Item:
    """Dojo solution."""
    return Item(name, cost)
