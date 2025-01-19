"""dojo module."""

from __future__ import annotations
from incolume.py.coding_dojo_jedi.dojo20250106 import PreprocessImageOCR



class PPIOCR(PreprocessImageOCR):
    """Class rescaling."""

def dojo(*args: str, **kwargs: str) -> dict[str]:
    """Dojo solution."""
    kwargs['args'] = args
    return kwargs
