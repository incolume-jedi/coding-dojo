"""dojo module."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Self

import cv2
from icecream import ic
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

    def black_white(self) -> Self:
        """Black and white image."""
        self.reset().grayscale()
        thresh, im_bw = cv2.threshold(self.img, 210, 230, cv2.THRESH_BINARY)
        logging.debug(ic(thresh, im_bw))
        self.img = im_bw
        return self
