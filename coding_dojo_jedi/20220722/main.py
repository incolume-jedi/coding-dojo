from star_wars import research
import click



CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

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
@click.option('-n', '--name', type=str, help='Name for search on api')
def cli(name):
    if not name:
        with click.Context(cli) as ctx:
            click.echo(ctx.get_help())

    click.echo(f'{name}')


if __name__ == '__main__':
    cli()

