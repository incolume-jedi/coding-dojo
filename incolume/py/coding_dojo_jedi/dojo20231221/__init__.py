"""dojo module."""

from pathlib import Path

import pandas as pd


def dojo(url_or_path: str) -> dict[str]:
    """Dojo solution."""
    url_or_path = url_or_path or Path(__file__).parent.joinpath(
        'presidentes_brasileiros_wikipedia.html',
    )
    df0 = pd.read_html(url_or_path)[0]
    print(df0)  # noqa: T201
    print(df0.columns)  # noqa: T201
    return df0.columns
