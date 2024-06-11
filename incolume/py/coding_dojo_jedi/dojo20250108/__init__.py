"""dojo module."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import NoReturn

import pandas as pd
import psycopg2
from icecream import ic
from incolume.py.coding_dojo_jedi.dojo20240514 import gen_data_file

diroutput = Path(__file__).parent

postgre_host: str = '127.0.0.1'
postgre_user: str = 'admin'
postgre_pw: str = 'admin1234'
postgre_db: str = 'voltagem'

filename = Path(__file__).parent.joinpath('voltagem.json')


def connect(
    host: str = '',
    port: str = '',
    database: str = '',
    user: str = '',
    password: str = '',
) -> psycopg2._T_conn:
    """Get  postgresql connect."""
    conn = None

    host = host or postgre_host or 'localhost'
    port = port or '5432'
    database = database or postgre_db
    user = user or postgre_user
    password = password or postgre_pw
    conn = psycopg2.connect(
        host=host,
        database=database,
        port=port,
        user=user,
        password=password,
    )
    # try:
    #     conn = psycopg2.connect(
    #         host=host,
    #         database=database,
    #         port=port,
    #         user=user,
    #         password=password,
    #     )
    # except psycopg2.DatabaseError:
    #     sys.exit(1)

    return conn


contents: list[str] = [
    f"""# File: docker-compose.yml
# Access via "http://localhost:8081"
#
# Call example:
# $ docker compose -f incolume/py/coding_dojo_jedi/dojo20240608/compose.yml up -d --build

version: "3.9"

services:
    postgresql_database:
        image: postgres:14-alpine3.19
        environment:
            - POSTGRES_USER={postgre_user}
            - POSTGRES_PASSWORD={postgre_pw}
            - POSTGRES_DB={postgre_db}
        ports:
            - "5432:5432"
        restart: always
        volumes:
            - pgsql-database:/var/lib/postgresql/data/

    pgadmin:
        image: dpage/pgadmin4
        environment:
            - PGADMIN_DEFAULT_EMAIL=pgadmin4@pgadmin.org
            - PGADMIN_DEFAULT_PASSWORD=admin1234
        ports:
            - "5050:80"
        restart: always
        volumes:
            - pgadmin:/root/.pgadmin
volumes:
    pgsql-database:
    pgadmin:
""",
]


def set_compose_file(fout: Path | None = None) -> bool:
    """Set compose file."""
    fout = fout or diroutput / 'compose.yml'
    fout.write_bytes(bytes(contents[0], encoding='utf-8'))
    ic(fout)
    return fout.is_file()


def load_db(filein: Path, conn: psycopg2.connect) -> NoReturn:
    """Load data on Database."""
    tipo = {
        'json': pd.read_json,
        'csv': pd.read_csv,
        'xlsx': pd.read_excel,
    }
    dataframe = tipo.get(filein.suffix.strip('.'))(filein)
    dataframe.to_sql('codigo_voltagem', conn)


if __name__ == '__main__':
    gen_data_file()
