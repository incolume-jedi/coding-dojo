"""Test dojo module."""

import sqlite3
from pathlib import Path
from tempfile import NamedTemporaryFile
from incolume.py.coding_dojo_jedi.dojo20240514 import (
    url,
    save_dataframe,
    scrap,
    load_db,
)


filename: Path = Path(NamedTemporaryFile(prefix='testing-').name)


def gen_data_file(ext: str = 'json') -> Path:
    """Generate data."""
    exts = ['csv', 'json', 'xlsx']
    if ext not in exts:
        excp = 'Valid type file. Only csv, json or xlsx'
        raise TypeError(excp)
    return save_dataframe(
        scrap(url),
        filename.with_suffix(f'.{ext}'),
        format_output=ext,
    )


def gen_conn() -> sqlite3.Connection:
    """Generate connection."""
    return sqlite3.connect(Path(NamedTemporaryFile(suffix='.db').name))


class CheckSQLite:
    """Check SQLite."""

    def test_query_json(self):
        """Check query."""
        file: Path = gen_data_file()
        with gen_conn() as conn:
            load_db(file, conn)
            cur = conn.cursor()
            cur.execute(
                'SELECT PAIS FROM codigo_voltagem WHERE "Pais" == "Brasil"',
            )
            result = cur.fetchone()
        assert result[0] == 'Brasil'

    def test_query_csv(self):
        """Check query."""
        file: Path = gen_data_file(ext='csv')
        with gen_conn() as conn:
            load_db(file, conn)
            cur = conn.cursor()
            cur.execute(
                'SELECT PAIS FROM codigo_voltagem WHERE "Pais" == "Brasil"',
            )
            result = cur.fetchone()
        assert result[0] == 'Brasil'

    def test_query_xlsx(self):
        """Check query."""
        file: Path = gen_data_file(ext='xlsx')
        with gen_conn() as conn:
            load_db(file, conn)
            cur = conn.cursor()
            cur.execute(
                'SELECT PAIS FROM codigo_voltagem WHERE "Pais" == "Brasil"',
            )
            result = cur.fetchone()
        assert result[0] == 'Brasil'
