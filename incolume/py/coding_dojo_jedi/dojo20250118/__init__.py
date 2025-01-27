"""dojo module."""

from __future__ import annotations

from icecream import ic
from incolume.py.coding_dojo_jedi.utils import filesmd


def dojo(*args: str, **kwargs: str) -> dict[str]:
    """Dojo solution."""
    kwargs['args'] = args
    kwargs['files'] = filesmd()
    ic(kwargs)
    return kwargs


if __name__ == '__main__':
    dojo()
