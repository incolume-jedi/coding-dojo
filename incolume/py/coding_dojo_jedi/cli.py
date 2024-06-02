"""CLI Module."""

import datetime
from pathlib import Path
from typing import NoReturn

import click
import pytz
from incolume.py.coding_dojo_jedi.utils import TZ, dojo_init, generator_sumary

CONTEXT_SETTINGS = {'help_option_names': ['-h', '--help']}


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--debug/--no-debug', default=False, help='Activate debug mode.')
@click.pass_context
def dojo(ctx, **kwargs):
    """Command Line Interface for dojo."""
    ctx.ensure_object(dict)
    ctx.obj.update(**kwargs)


@dojo.command()
@click.option(
    '--path',
    '-p',
    default=Path().joinpath('incolume', 'py', 'coding_dojo_jedi').as_posix(),
    help='Path for dojos directories.',
)
@click.option(
    '--date',
    '-d',
    default=f'{datetime.datetime.now(tz=pytz.timezone(TZ)):%Y%m%d}',
    help='Date "%Y%m%d" for dojo boilerplate.',
)
@click.option(
    '--tz',
    '-t',
    default=TZ,
    help='Timezone for datetime object.',
)
@click.pass_context
def init(path: str, date: str, tz: str) -> NoReturn:
    """Initiate a dojo boilerplate."""
    date = datetime.datetime.strptime(date, '%Y%m%d').astimezone(
        datetime.timezone.utc,
    )
    dojo_init(dojo_path=path, dojo_date=date, time_zone=tz)


@dojo.command()
@click.option(
    '--file',
    '-f',
    default='incolume/py/coding_dojo_jedi/README.md',
    help='full filename for sumary file.',
)
@click.option('--reverse', '-r', is_flag=True)
@click.pass_context
def sumary(filename: str = '', *, reverse: bool = False) -> bool:
    """Generates a summary file with solved dojos.

    :param filename: full filename for sumary file;
    :param reverse: sort reversed
    :return: bool: True if success
    """
    fout: Path = Path(filename)
    click.echo(f'Sumário em {fout} .. ', nl=False)
    generator_sumary(fout=fout, reverse=reverse)
    click.echo('criado com sucesso!', color='green')
    return fout.is_file()
