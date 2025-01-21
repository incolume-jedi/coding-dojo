"""dojo module."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import NoReturn, Self

import cv2
import numpy as np
from icecream import ic
from incolume.py.coding_dojo_jedi.utils import whoami
from matplotlib import pyplot as plt

IMG_DIR: Path = Path(__file__).parents[1] / 'generic_data' / 'text_img'


@whoami
class PreprocessImageOCR:
    """Preprocess Image."""

    def __init__(self, img_path: Path | None = None, dpi: int | None = None):
        """Initializer."""
        self._img_path: Path = None
        self.dpi: int = dpi or 80
        self._img_data: np.ndarray = None
        self.img: np.ndarray = None
        self.img_path = img_path

    @property
    def img_path(self) -> Path:
        """Imagem file."""
        return self._img_path

    @img_path.setter
    def img_path(self, value: Path) -> NoReturn:
        self._img_path = value
        try:
            self._img_data = plt.imread(self._img_path)
            self.img = plt.imread(self._img_path)
        except AttributeError:
            pass
        logging.info(ic('Image load'))
        logging.debug(ic(self.img_path))

    def save(self, fout: Path | None = None) -> Path:
        """Save current image."""
        fout = fout or (
            Path.cwd() / f'{self.img_path.stem}_latest{self.img_path.suffix}'
        )
        fout = fout.resolve()
        fout.parent.mkdir(exist_ok=True)
        cv2.imwrite(fout, self.img)
        logging.info(ic('Image saved.'))
        logging.debug(ic(fout))
        return fout

    def reset(self) -> Self:
        """Reset to original image."""
        self.img = plt.imread(self.img_path)
        logging.info(ic('Image reseted.'))
        return self

    def display(self, img_path: Path | None = None) -> bool:
        """Display image on screen.

        https://stackoverflow.com/questions/28816046/displaying-different-images-with-actual-size-in-matplotlib-subplot
        """
        if img_path:
            self.img_path = img_path

        height, width = self.img.shape[:2]

        # What size does the figure need to be in inches to fit the image?
        figsize = width / float(self.dpi), height / float(self.dpi)

        # Create a figure of the right size with
        # one axes that takes up the full figure
        fig = plt.figure(figsize=figsize)
        ax = fig.add_axes([0, 0, 1, 1])

        # Hide spines, ticks, etc.
        ax.axis('off')

        # Display the image.
        ax.imshow(self.img, cmap='gray')

        plt.show()


class PPIOCR(PreprocessImageOCR):
    """Class rescaling."""

    def inverted(self) -> Self:
        """Inverter bit image."""
        self.img = cv2.bitwise_not(self.img)
        logging.info(ic('Inverted image.'))
        return self

    def grayscale(self) -> Self:
        """Gray scale image."""
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        logging.info(ic('Gray scale image.'))
        return self

    def black_white(self) -> Self:
        """Black and white image."""
        self.reset().grayscale()
        thresh, im_bw = cv2.threshold(self.img, 210, 230, cv2.THRESH_BINARY)
        logging.debug(ic(thresh, im_bw))
        self.img = im_bw
        logging.info(ic('black and white image.'))
        return self


if __name__ == '__main__':
    img0: Path = IMG_DIR / 'letter.jpg'
    img1: Path = IMG_DIR / 'ctr-1808-08-25.png'
    obj = PPIOCR(img1)
    obj.display()
    obj.inverted().display()
    obj.reset().grayscale().display()
    obj.reset().black_white().display()
