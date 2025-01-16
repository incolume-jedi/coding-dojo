"""dojo module."""

from __future__ import annotations

from functools import wraps
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable


def who(cls):
    """Class name."""
    cls.class_name = cls.__name__
    return cls


def upper(func):
    """Decorator."""

    @wraps(func)
    def inner(s: str) -> str:
        """Inner function."""
        return func(s).upper()

    return inner


def capitalizer(func: Callable) -> Callable:
    """First letter capital."""

    @wraps(func)
    def inner(s: str) -> str:
        """Inner function."""
        return ' '.join(
            x.capitalize() if len(x) > 2 else x  # noqa: PLR2004
            for x in func(s).capitalize().split()
        )

    return inner


def speller(func: Callable) -> Callable:
    """Spell words."""

    @wraps(func)
    def inner(s: str) -> str:
        """Inner function."""
        return ' '.join('-'.join(list(x)) for x in func(s).split())

    return inner


@speller
@capitalizer
def dojo(s: str) -> str:
    """Dojo solution."""
    return s
