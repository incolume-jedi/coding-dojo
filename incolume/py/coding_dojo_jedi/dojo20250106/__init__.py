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

from copy import copy
from pathlib import Path
from typing import TYPE_CHECKING, Self

import cv2
from matplotlib import pyplot as plt

if TYPE_CHECKING:
    import numpy as np


def who(cls):
    """Its Class name."""
    cls.class_name = cls.__name__
    return cls


@who
class PreprocessImageOCR:
    """Preprocess Image."""

    IMG_DIR: Path = Path(__file__).parents[1] / 'generic_data' / 'text_img'

    def __init__(self):
        """Initializer."""
        self.dpi: float = 80.0
        self._img_path: Path = None
        self._img_data: np.ndarray = None
        self.img: np.ndarray = None

    @property
    def img_path(self):
        """Imagem file."""
        return self._img_path

    @img_path.setter
    def img_path(self, value: Path) -> Self:
        self._img_path = value
        self._img_data = plt.imread(self._img_path)
        self.img = copy(self._img_data)

    def display(self, img_path: Path) -> bool:
        """Display image on screen.

        https://stackoverflow.com/questions/28816046/displaying-different-images-with-actual-size-in-matplotlib-subplot
        """
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
            Path() / f'{self.img_path.stem}_latest{self.img_path.suffix}'
        )
        cv2.imwrite(fout, self.img)
        return fout

    def inverted(self) -> Self:
        """Inverter bit image."""
        self.img = cv2.bitwise_not(self._img_data)
        return self


if __name__ == '__main__':
    o = PreprocessImageOCR()
    o.display(o.IMG_DIR / 'letter.png')
    o.display(o.IMG_DIR / 'ctr-1808-08-25.png')
