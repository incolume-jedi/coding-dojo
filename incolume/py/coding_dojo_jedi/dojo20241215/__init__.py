"""dojo module."""

from pathlib import Path

from incolume.py.coding_dojo_jedi.dojo20231221 import dojo as v1


def dojo(url_or_path: str | Path | None = None) -> dict[str]:
    """Dojo solution."""
    return v1(url_or_path)
