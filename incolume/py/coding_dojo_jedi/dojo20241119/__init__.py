"""dojo module."""

import inspect
import logging
import sys
from pathlib import Path
from typing import TypeAlias

import magic

if sys.version_info >= (3, 11):
    from typing import Literal, get_args
else:
    from typing_extensions import Literal, get_args  # noqa: UP035

Method: TypeAlias = Literal['filetype', 'magic']


artefatos: dict[str, list[str]] = {
    'url': [
        r'https://www.python.org/static/community_logos/python-powered-h-50x65.png',
        r'https://www.python.org/static/community_logos/python-powered-h.svg',
        r'https://www.python.org/static/community_logos/python-logo-master-v3-TM.psd',
        r'https://www.gov.br/ana/pt-br/todos-os-documentos-do-portal/doc-modelo.pdf/@@download/file/doc-modelo.pdf',
        r'https://portal.ead.senasp.gov.br/noticias/ciclos/resultado-preliminar-2013-selecao-de-tutores-ajap-va-1/modelo-de-declaracao.docx/@@download/file/MODELO%20DE%20DECLARA%C3%87%C3%83O.docx',
    ],
    'path': [
        Path(__file__).parent / 'dojo20241118' / 'files' / 'filedocx.docx',
        Path(__file__).parent / 'dojo20241118' / 'files' / 'fileodt.odt',
        Path(__file__).parent / 'dojo20241118' / 'files' / 'filexlsx.xlsx',
        Path(__file__).parent / 'dojo20241118' / 'files' / 'filepdf.pdf',
    ],
}


def with_filetype(file: str) -> str:
    """Identify type with filetype."""
    logging.debug(inspect.stack()[0][1])


def with_magic(file: str) -> str:
    """Identify type with magic."""
    logging.debug(inspect.stack()[0][1])
    mime = magic.Magic(mime=True)
    return mime.from_file(file)


def dojo(file: str, *, method: Method = 'magic') -> str:
    """Dojo solution."""
    logging.debug(inspect.stack()[0][1])
    match method:
        case 'magic':
            return f'python-magic, {file}'
        case 'filetype':
            return f'filetype, {file}'
        case _:
            return f'Método inválido utilize: {get_args(Method)}'
