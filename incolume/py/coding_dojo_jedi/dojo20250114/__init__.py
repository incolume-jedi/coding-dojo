"""dojo module."""

from __future__ import annotations

from pathlib import Path
from typing import Self

import cv2
from incolume.py.coding_dojo_jedi.dojo20250106 import (
    PreprocessImageOCR,
)

IMG_DIR: Path = Path(__file__).parents[1] / 'generic_data' / 'text_img'


class PPIOCR(PreprocessImageOCR):
    """Class rescaling."""

    def grayscale(self) -> Self:
        """Gray scale image."""
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        return self
