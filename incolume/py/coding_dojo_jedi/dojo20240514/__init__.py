"""dojo module."""

import sqlite3
import tempfile
from typing import NoReturn

import pandas as pd
from incolume.py.coding_dojo_jedi.dojo20240513 import (
    Path,
    save_dataframe,
    scrap,
    url,
)

conn = sqlite3.connect(Path(tempfile.gettempdir()) / 'voltagem.db')
filename = Path(__file__).parent.joinpath('fout.xlsx')


def load_db(filein: Path, conn: sqlite3.Connection | None = None) -> NoReturn:
    """Load data on Database."""
    tipo = {
        'json': pd.read_json,
        'csv': pd.read_csv,
        'xlsx': pd.read_excel,
    }
    dataframe = tipo.get(filein.suffix.strip('.'))(filein)
    dataframe.to_sql('codigo_voltagem', conn)


def run():
    """Run it."""
    save_dataframe(scrap(url), filename, format_output='xlsx')
    load_db(filename, conn=conn)


if __name__ == '__main__':
    run()
