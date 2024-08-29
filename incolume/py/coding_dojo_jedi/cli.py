"""CLI Module."""

import datetime
import os
from pathlib import Path
from typing import NoReturn

import click
import pytz
from icecream import ic
from incolume.py.coding_dojo_jedi.utils import TZ, dojo_init, generator_sumary

ic.disable()
if os.getenv('DEBUG_MODE'):
    ic.enable()


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
def init(ctx: click.Context, path: str, date: str, tz: str) -> NoReturn:
    """Initiate a dojo boilerplate."""
    ic(type(ctx))
    ic()
    date = datetime.datetime.strptime(date, '%Y%m%d').astimezone(
        datetime.timezone.utc,
    )
    files = dojo_init(dojo_path=path, dojo_date=date, time_zone=tz)
    click.secho(
        f'Boilerplate para dojo criado com sucesso em {files[0].parent}.',
    )


@dojo.command()
@click.option(
    '--filename',
    '-f',
    default='incolume/py/coding_dojo_jedi/README.md',
    help='full filename for sumary file.',
)
@click.option('--reverse', '-r', is_flag=True)
@click.pass_context
def sumary(
    ctx: click.Context,
    filename: str = '',
    *,
    reverse: bool = False,
) -> bool:
    """Generates a summary file with solved dojos.

    :param filename: full filename for sumary file;
    :param reverse: sort reversed
    :return: bool: True if success
    """
    ic(type(ic(ctx)))
    fout: Path = Path(filename)
    click.echo(f'Sumário em {fout} .. ', nl=False)
    generator_sumary(fout=fout, reverse=reverse)
    click.echo('criado com sucesso!', color='green')
    return fout.is_file()


@dojo.command()
@click.pass_context
def show(ctx: click.Context) -> NoReturn:
    """Show configuration."""
    ic(type(ic(ctx)))
    click.secho(f'{ctx.obj}')
    click.echo('Debug is %s' % (ctx.obj['debug'] and 'on' or 'off'))
