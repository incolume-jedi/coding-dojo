"""dojo module."""

from pathlib import Path

import pandas as pd


def dojo(url_or_path: str = '', output: Path | str = '') -> dict[str]:
    """Dojo solution."""
    url_or_path = url_or_path or Path(__file__).parent.joinpath(
        'presidentes_brasileiros_wikipedia.html',
    )
    output = output or 'dojo.json'
    output = Path(output)
    df0 = pd.read_html(url_or_path)[0]
    print(df0)  # noqa: T201
    print(type(df0.columns))  # noqa: T201
    print(df0.columns)  # noqa: T201
    df0.columns = [
        'NR',
        'PRESIDENTE',
        'FOTOGRAFIA',
        'PERÍODO DO MANDATO (DURAÇÃO DO MANDATO)',
        'PARTIDO',
        'VICE-PRESIDENTE(S)',
        'REFERÊNCIAS E NOTAS',
        'ELEIÇÃO',
    ]
    df0.to_csv('dojo.csv')
    campos = [
        'PRESIDENTE',
        'VICE-PRESIDENTE(S)',
        'PERÍODO DO MANDATO (DURAÇÃO DO MANDATO)',
        'PARTIDO',
    ]
    df0[campos].to_json(output, indent=2, orient='records')
    return output
