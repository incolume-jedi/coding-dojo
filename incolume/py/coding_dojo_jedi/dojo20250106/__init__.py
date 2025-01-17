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

from functools import wraps
from pathlib import Path
from tempfile import gettempdir
from typing import TYPE_CHECKING

import cv2
import numpy as np
from icecream import ic
from matplotlib import pyplot as plt

if TYPE_CHECKING:
    import numpy as np


class PreprocessImage:
    """Preprocess Image."""

    IMG_DIR: Path = Path(__file__).parents[1] / 'generic_data' / 'text_img'

    def __init__(self):
        """Initializer."""
        self.dpi: float = 80.0

    def display(self, img_path: Path) -> bool:
        """Display image on screen.

        https://stackoverflow.com/questions/28816046/displaying-different-images-with-actual-size-in-matplotlib-subplot
        """
        img_data = plt.imread(img_path)

        height, width = img_data.shape[:2]

        # What size does the figure need to be in inches to fit the image?
        figsize = width / self.dpi, height / self.dpi

        # Create a figure of the right size with
        # one axes that takes up the full figure
        fig = plt.figure(figsize=figsize)
        ax = fig.add_axes([0, 0, 1, 1])

        # Hide spines, ticks, etc.
        ax.axis('off')

        # Display the image.
        ax.imshow(img_data, cmap='gray')

        plt.show()


def open_plot(func: callable) -> callable:
    """Change Image Path to matrix."""

    @wraps(func)
    def inner(fimg: Path) -> np.ndarray:
        """Inner function."""
        img_data = plt.imread(fimg)
        return func(img_data)

    return inner


def write_plot(func: callable) -> callable:
    """Change Image Path to matrix."""

    @wraps(func)
    def inner(img_data: np.ndarray, foutput: Path | None = None) -> Path:
        """Inner function."""
        ic(img_data, foutput)
        cv2.imwrite(foutput, img_data)
        return func(img_data, foutput)

    return inner


@open_plot
def inverted_image(fimg: Path, foutput: Path | None = None) -> Path:
    """Inverted image."""
    foutput = foutput or Path(
        gettempdir(),
        f'{fimg.stem}_inverted{fimg.suffix}',
    )
    ic(foutput)
    ic(fimg)
    imgdata = plt.imread(fimg)
    image = cv2.bitwise_not(imgdata)
    cv2.imwrite(foutput, image)
    return foutput


if __name__ == '__main__':
    o = PreprocessImage()
    o.display(o.IMG_DIR / 'letter.png')
    o.display(o.IMG_DIR / 'ctr-1808-08-25.png')
