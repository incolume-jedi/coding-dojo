"""dojo module."""

from __future__ import annotations

def dojo(*args: str, **kwargs: str)->dict[str]:
    """Dojo solution."""
    kwargs["args"] = args
    return kwargs
