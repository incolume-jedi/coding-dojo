from pathlib import Path
from markdown import markdownFromFile


def generator_sumary(fout: Path = None) -> Path:
    """Gerador de sumário."""

    files = sorted(list(Path(__file__).parents[1].rglob('**/README.md')))
    print(len(files))
    fmd = files[0]
    print(markdownFromFile(input=fmd))

    # return Path(__file__).absolute().parent.parent
    file = fout or Path(__file__).parent.joinpath('sumario.md')
    # file.write_text('')
    return file