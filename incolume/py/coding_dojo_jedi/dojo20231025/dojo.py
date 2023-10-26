from pathlib import Path
import re


def generator_sumary(fout: Path = None) -> Path:
    """Gerador de sumário."""

    files = sorted(list(Path(__file__).parents[1].rglob('**/README.md')))
    print(len(files))
    regex = r'## Problema\s*\*\*((\w+\s*)+)\*\*'
    fmd = files[2]
    result = re.search(regex, fmd.read_text(), flags=re.I)
    sout = f'1. [{fmd.parts[-2]} &#8212; {result.group(1)}]({Path("..").joinpath(*fmd.parts[-2:])})'
    print(sout)



    # return Path(__file__).absolute().parent.parent
    file = fout or Path(__file__).parent.joinpath('sumario.md')
    # file.write_text('')
    return file