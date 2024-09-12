"""Test dojo module."""

from pathlib import Path
from tempfile import NamedTemporaryFile
from unittest import mock

import pytest

from incolume.py.coding_dojo_jedi.dojo20240514 import (
    load_db,
    gen_conn,
    gen_data_file,
    pd,
)
from incolume.py.coding_dojo_jedi.dojo20240513.test_20240513 import file

filename: Path = Path(NamedTemporaryFile(prefix='testing-').name)


class CheckSQLite:
    """Check SQLite."""

    dataframe = pd.read_html(file.read_bytes())

    def test_gen_dta_file(self):
        """Test gendata file."""
        with pytest.raises(TypeError):
            gen_data_file('xml')

    def test_query_json(self):
        """Check query."""
        file: Path = gen_data_file()
        with (
            mock.patch(
                'incolume.py.coding_dojo_jedi.dojo20240513.scrap',
                return_value=self.dataframe,
            ),
            gen_conn() as conn,
        ):
            load_db(file, conn)
            cur = conn.cursor()
            cur.execute(
                'SELECT PAIS FROM codigo_voltagem' ' WHERE "Pais" == "Brasil"',
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
