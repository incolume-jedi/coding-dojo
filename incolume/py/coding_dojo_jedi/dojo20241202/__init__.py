"""dojo module."""

from pathlib import Path

from bs4 import BeautifulSoup

directory: list[Path] = [
    Path('z:', 'acervo-legis'),
    Path(
        'castelo',
        'saj',
        'CENTRO DE ESTUDOS',
        'EQUIPE CEJ',
        'BRITO',
        'projetos',
        'acervo-legis',
    ),
]


def get_list_html(path_dir: Path | None = None) -> map:
    """Return list HTML files."""
    path_dir = path_dir or directory[0]
    return path_dir.rglob(pattern='*.htm?', case_sensitive=False)

def get_content_html(filename: Path) -> bytes:
    """Return HTML content."""
    soup = BeautifulSoup(filename.read_bytes(), 'html5lib')
    return soup.prettify()

def dojo() -> Path:
    """Dojo solution."""
    for file in get_list_html():
        return get_content_html(file)
    return None
