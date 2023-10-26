from pathlib import Path
import re


def generator_sumary(fout: Path = None) -> Path:
    """Gerador de sumário."""

    file = fout or Path(__file__).parent.joinpath('sumario.md')
    regex = r'## Problema\s*\*\*((\w+\s*)+)\*\*'

     
    with file.open('w') as fmd:
        fmd.writelines(
            [
                '# Coding Dojo\n', 
                '**Guilda JEDI Incolume - Grupo Python Incolume**\n', 
                '- [Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)\n', 
                '## Sumário dos dojos\n\n---\n'
            ]
        )
        for filemd in sorted(list(Path(__file__).parents[1].rglob('**/README.md'))):
            try:
                result = re.search(regex, filemd.read_text(), flags=re.I)
                sout = f'1. [{filemd.parts[-2].capitalize()} &#8212; {result.group(1)}]({Path("..").joinpath(*filemd.parts[-2:])})\n'
                # print(sout)
                fmd.write(sout)
            except AttributeError:
                pass
        fmd.writelines(['\n---\n\n', '&copy; Incolume.com.br\n\n'])
    return file