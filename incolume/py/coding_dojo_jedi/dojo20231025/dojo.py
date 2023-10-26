from pathlib import Path

def generator_sumary(fout: Path = None) -> Path:
    """Gerador de sumário."""

    files = Path(__file__).parents[1].rglob('**/README.md')
    print(len(list(files)))
    
    # return Path(__file__).absolute().parent.parent
    file = fout or Path(__file__).parent.joinpath('sumario.md')
    # file.write_text('')
    return file