import click
from star_wars import research

CONTEXT_SETTINGS = {'help_option_names': ['-h', '--help']}

# Example from https://stackoverflow.com/a/50442496/5132101
#
# @click.command(context_settings=CONTEXT_SETTINGS)
# @click.option('--toduhornot', is_flag=True, help='prints "duh..."')
# def duh(toduhornot):
#     if toduhornot:
#         with click.Context(duh) as ctx:

# if __name__ == '__main__':


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option(
    '-n',
    '--name',
    type=str,
    default=None,
    help='Name for search on api',
)
def cli(name):
    msg = ''
    if not name:
        with click.Context(cli) as ctx:
            click.echo(ctx.get_help())

    personagem = research(name)
    if not personagem:
        msg = f'Personagem "{name}" não encontrado'
    else:
        msg = (
            f'* Nome: {personagem.get("name")}\n'
            f'* Altura: {personagem.get("height")}cm\n'
            f'* Ano de nascimento: {personagem.get("birth_year")}\n'
            f'* Quantidade de filmes: {len(personagem.get("films"))}\n'
        )
    click.echo(msg)


if __name__ == '__main__':
    cli()
