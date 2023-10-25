from pathlib import Path

def generator_sumary(fout: Path = None) -> bool:
    """Gerador de sumário."""
    # return Path(__file__).absolute().parent.parent
    file = fout or Path(__file__).parent.joinpath('sumario.md')
    file.write_text('')
    return file