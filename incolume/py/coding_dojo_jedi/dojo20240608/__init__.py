"""dojo module."""

from pathlib import Path

diroutput = Path(__file__).parent


contents: list[str] = [
    b""" # File: docker-compose.yml
# Access via "http://localhost:8081"
#
# Call example:
# $ docker compose -f incolume/py/coding_dojo_jedi/dojo20240608/compose.yml up -d --build

version: "3.9"

services:
    postgresql_database:
        image: postgres:14-alpine3.19
        environment:
            - POSTGRES_USER=admin
            - POSTGRES_PASSWORD=admin1234
            - POSTGRES_DB=records
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
    fout.write_bytes(contents[0])
    return fout.is_file()
