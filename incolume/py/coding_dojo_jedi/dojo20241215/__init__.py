"""dojo module."""

import inspect
from pathlib import Path
from typing import Final

from icecream import ic
from incolume.py.coding_dojo_jedi.dojo20231221 import dojo as v1

SOURCE: Final[Path] = (
    Path(__file__)
    .parents[1]
    .joinpath('dojo20231221', 'presidentes_brasileiros_wikipedia.html')
)


def dojo_review(
    url_or_path: str | Path = '',
    output: Path | str = '',
) -> dict[str]:
    """Dojo solution."""
    url_or_path = Path(url_or_path or SOURCE)
    ic(url_or_path)
    output = Path(output or f'{inspect.stack()[0][3]}.json')
    ic(output)
    return v1(url_or_path, output=output)
