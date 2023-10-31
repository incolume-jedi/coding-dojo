"""CLI Module."""
from pathlib import Path

import click

from incolume.py.coding_dojo_jedi.utils import generator_sumary


@click.command()
@click.option(
    '--file',
    '-f',
    default='incolume/py/coding_dojo_jedi/README.md',
    help='Path for sumary file.',
)
def sumary(file: str = '') -> bool:
    """Interface CLI para gerador de sumário.

    :param file full filename for sumary;
    :return: bool: True if success
    """
    fout: Path = Path(file)
    click.echo('ok')
    generator_sumary(fout)
    return fout.is_file()
