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

from pathlib import Path
from tempfile import gettempdir

import cv2
from icecream import ic
from matplotlib import pyplot as plt

IMG_DIR: Path = Path(__file__).parents[1] / 'generic_data' / 'text_img'


def display(img_path: Path) -> None:
    """Display image on screen.

    https://stackoverflow.com/questions/28816046/displaying-different-images-with-actual-size-in-matplotlib-subplot
    """
    dpi = 80
    img_data = plt.imread(img_path)

    height, width = img_data.shape[:2]

    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with
    # one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(img_data, cmap='gray')

    plt.show()


def inverted_image(fimg: Path, foutput: Path | None = None) -> Path:
    """Inverted image."""
    foutput = foutput | Path(gettempdir, f'{fimg.stem}_inverted{fimg.suffix}')
    ic(foutput)
    ic(fimg)
    img = plt.imread(fimg)
    image = cv2.bitwise_not(img)
    cv2.imwrite(foutput, image)
    return foutput


if __name__ == '__main__':
    display(IMG_DIR / 'letter.png')
    display(IMG_DIR / 'ctr-1808-08-25.png')
