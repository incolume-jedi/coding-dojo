"""dojo module.

1. **Inverted Images**
2. Rescaling
3. Binarization
4. Noise Removal
5. Dilation and Erosion
6. Rotation / Deskewing
7. Removing Borders
8. Missing Borders
9. Transparency / Alpha Channel
"""

from __future__ import annotations

import logging
from copy import copy
from pathlib import Path
from typing import TYPE_CHECKING, NoReturn, Self

import cv2
from icecream import ic
from matplotlib import pyplot as plt

if TYPE_CHECKING:
    import numpy as np

IMG_DIR: Path = Path(__file__).parents[1] / 'generic_data' / 'text_img'


def who(cls):
    """Its Class name."""
    cls.class_name = cls.__name__
    return cls


@who
class PreprocessImageOCR:
    """Preprocess Image."""

    def __init__(self, img_path: Path | None = None):
        """Initializer."""
        self.dpi: float = 80.0
        self._img_path: Path = None
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
        try:  # noqa: SIM105
            self._img_data = plt.imread(self._img_path)
        except AttributeError:
            pass
        self.img = copy(self._img_data)

    def display(self, img_path: Path | None = None) -> bool:
        """Display image on screen.

        https://stackoverflow.com/questions/28816046/displaying-different-images-with-actual-size-in-matplotlib-subplot
        """
        if img_path:
            self.img_path = img_path

        height, width = self.img.shape[:2]

        # What size does the figure need to be in inches to fit the image?
        figsize = width / self.dpi, height / self.dpi

        # Create a figure of the right size with
        # one axes that takes up the full figure
        fig = plt.figure(figsize=figsize)
        ax = fig.add_axes([0, 0, 1, 1])

        # Hide spines, ticks, etc.
        ax.axis('off')

        # Display the image.
        ax.imshow(self.img, cmap='gray')

        plt.show()

    def save(self, fout: Path | None = None) -> Path:
        """Save current image."""
        fout = fout or (
            Path.cwd() / f'{self.img_path.stem}_latest{self.img_path.suffix}'
        )
        logging.debug(ic(fout))
        cv2.imwrite(fout, self.img)
        return fout

    def reset(self) -> Self:
        """Reset to original image."""
        self.img = copy(self._img_data)
        return self

    def inverted(self) -> Self:
        """Inverter bit image."""
        self.img = cv2.bitwise_not(self._img_data)
        return self


if __name__ == '__main__':
    o = PreprocessImageOCR(IMG_DIR / 'letter.png')
    o.display(o.IMG_DIR / 'ctr-1808-08-25.png')
