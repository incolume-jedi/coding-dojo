"""Module."""

from __future__ import annotations

from pathlib import Path

# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from unidecode import unidecode

__author__ = '@britodfbr'  # pragma: no cover

url = 'https://www.inf.ufrgs.br/~cabral/Voltagem.Codigos.2020.10.05.html'


def scrap(url: str) -> pd.DataFrame:
    """Raspagem de codigos de voltagem."""
    dataframe = pd.read_html(url)[0]
    dataframe.columns = (
        dataframe.columns.map(unidecode)
        .str.replace(' ', '_', regex=True)
        .str.strip('.')
        .str.upper()
    )
    return dataframe.set_index('ORD')


def save_dataframe(
    df: pd.DataFrame,
    filename: Path | None = None,
    format_output: str = 'csv',
) -> Path:
    """Sava dados raspados."""
    filename = filename or Path(f'fout.{format_output}')
    output = {
        'csv': df.to_csv,
        'json': df.to_json,
        'xlsx': df.to_excel,
    }
    output.get(format_output)(filename)
    return filename


def run():
    """Run it."""


if __name__ == '__main__':  # pragma: no cover
    run()
