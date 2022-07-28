from star_wars import research
import click



CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

# Example from https://stackoverflow.com/a/50442496/5132101
#
# @click.command(context_settings=CONTEXT_SETTINGS)
# @click.option('--toduhornot', is_flag=True, help='prints "duh..."')
# def duh(toduhornot):
#     if toduhornot:
#         click.echo('duh...')
#     else:
#         with click.Context(duh) as ctx:
#             click.echo(ctx.get_help())

# if __name__ == '__main__':
#     duh()

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-n', '--name', type=str, default=None, help='Name for search on api')
def cli(name):
    msg = ''
    if not name:
        with click.Context(cli) as ctx:
            click.echo(ctx.get_help())

    # click.echo(f'{name}')
    personagens = research(name)
    if personagens:
        try:
            for personagem in personagens:
                msg = f'* Nome: {personagem.get("name")}\n'\
                   f'* Altura: {personagem.get("height")}cm\n'\
                   f'* Ano de nascimento: {personagem.get("birth_year")}\n'\
                   f'* Quantidade de filmes: {len(personagem.get("films"))}\n'
                click.echo(msg)
        except:
            encontrados = ', '.join([f'"{f}"' for f in personagens])
            click.secho(f'Nenhum personagem "{name}" encontrado, mas encontrei: {encontrados}', fg='yellow')
    else:
        click.secho(f'Personagem "{name}" não encontrado', fg='red')



if __name__ == '__main__':
    cli()

