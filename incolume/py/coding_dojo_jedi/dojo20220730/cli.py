"""Dojo."""

import sys

import click
from incolume.py.coding_dojo_jedi.dojo20220730.dojo import research

CONTEXT_SETTINGS = {'help_option_names': ['-h', '--help']}


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option(
    '-n',
    '--name',
    type=str,
    default=None,
    help='Name for search on api',
)
def run(name: str = '') -> None:
    """Command Line Interface."""
    msg = ''
    if not name:
        with click.Context(run) as ctx:
            click.echo(ctx.get_help())
        sys.exit(0)

    personagens = research(name)
    if personagens:
        try:
            for personagem in personagens:
                msg = (
                    f'* Nome: {personagem.get("name")}\n'
                    f'* Altura: {personagem.get("height")}cm\n'
                    '* Ano de nascimento: '
                    f'{personagem.get("birth_year", "")}\n'
                    '* Quantidade de filmes: '
                    f'{len(personagem.get("films", ""))}\n'
                )
                click.echo(msg)
        except ValueError:
            encontrados = ', '.join([f'"{f}"' for f in personagens])
            click.secho(
                f'Nenhum personagem "{name}" '
                f'encontrado, mas encontrei: {encontrados}',
                fg='yellow',
            )
    else:
        click.secho(f'Personagem "{name}" não encontrado', fg='red')


if __name__ == '__main__':
    run()
