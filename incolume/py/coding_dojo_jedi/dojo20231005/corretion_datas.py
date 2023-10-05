"""Modulo para atender a issue #114.

que trata da reestruturação de nomes para diretórios dos dojos.
"""

from pathlib import Path

dirs = Path().absolute().parent.rglob('2022*')
for pasta in dirs:
    print(pasta.stem)    # noqa: T201
