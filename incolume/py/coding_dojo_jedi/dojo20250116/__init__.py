"""dojo module."""

from __future__ import annotations

from pathlib import Path

from icecream import ic
from incolume.py.coding_dojo_jedi.dojo20250114 import PreprocessImageOCR

IMG_DIR: Path = Path(__file__).parents[1] / 'generic_data' / 'text_img'


class PPImg(PreprocessImageOCR):
    """Class PPImg."""

    def __repr__(self) -> str:
        """Repr class."""
        return f'{self.__class__.__name__}({self.__dict__})'


def dojo(**kwargs: dict[str, Path]) -> dict[str]:
    """Dojo solution."""
    obj = PPImg(**kwargs) or kwargs.get('obj')
    ic(obj)
    return obj


if __name__ == '__main__':
    dojo()
