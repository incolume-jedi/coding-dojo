"""Modulo para atender a issue #114.

que trata da reestruturação de nomes para diretórios dos dojos.
"""

import subprocess
from pathlib import Path


def tratativa0() -> None:
    """Descobrir o nome dos diretórios afetados."""
    dirs = Path().absolute().parent.rglob('2022*')
    for pasta in dirs:
        print(pasta.name)


def tratativa1() -> None:
    """Remomear diretório de dojo que começam com numeros."""
    escopo = sorted(Path(__file__).parents[1].rglob('20*'))
    for i in escopo:
        original, novo = i, i.with_name(f'dojo{i.stem}')
        print(original, novo)
        subprocess.run(
            ['git', 'mv', original, novo],
            check=False,
        )


def run() -> None:
    """Run this."""
    tratativa1()


if __name__ == '__main__':
    run()
