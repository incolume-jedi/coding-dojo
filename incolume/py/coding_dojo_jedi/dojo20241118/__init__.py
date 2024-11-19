"""dojo module."""

import base64
from pathlib import Path


def dojo(file: Path | None = None) -> dict[str]:
    """Dojo solution."""
    return base64.b64encode(file.read_bytes())
