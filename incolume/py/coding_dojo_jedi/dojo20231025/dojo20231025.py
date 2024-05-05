"""Modulo para dojo20231025."""

import re
from pathlib import Path


def generator_sumary(fout: Path | None = None) -> Path:
    """Gerador de sumário."""
    file = fout or Path(__file__).parent.joinpath('sumario.md')
    regex = r'## Problema\s*\*\*((\w+\s*)+)\*\*'

    with file.open('w') as fmd:
        fmd.writelines(
            [
                '# Coding Dojo\n\n',
                '**Guilda JEDI Incolume - Grupo Python Incolume**\n\n',
                '- [Seja membro da Guilda JEDI Incolume]'
                '(https://discord.gg/eBNamXVtBW)\n\n',
                '## Sumário dos dojos\n\n',
                '---\n\n',
            ],
        )
        for filemd in sorted(
            Path(__file__).parents[1].rglob('**/*.md'),
        ):
            try:
                result = re.search(regex, filemd.read_text(), flags=re.I)
                title = filemd.parts[-2].capitalize()
                desc = result.group(1)  # type: ignore[union-attr]
                link = Path('..').joinpath(*filemd.parts[-2:])
                sout = f'1. [{title} &#8212; {desc}]({link})\n'
                fmd.write(sout)
            except AttributeError:  #  noqa: PERF203
                pass
        fmd.writelines(
            [
                '\n---\n\n',
                'Copyrigth &copy; **Incolume.com.br** since 2010\n\n',
            ],
        )
    return file


if __name__ == '__main__':  # pragma: no cover
    generator_sumary()
