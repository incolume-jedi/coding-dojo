"""dojo module."""

# ruff: noqa: ERA001
import inspect
import logging
import sys
from pathlib import Path
from typing import TypeAlias

import filetype
import puremagic
from icecream import ic

# import magic  incompatível com MacOS

msg = sys.platform.casefold()
logging.info(msg)
ic(msg)


if sys.version_info >= (3, 11):
    from typing import Literal, get_args
else:
    from typing_extensions import Literal, get_args  # noqa: UP035

Method: TypeAlias = Literal['filetype', 'magic', 'puremagic']
Method: TypeAlias = Literal['filetype', 'puremagic']


artefatos: dict[str, list[str]] = {
    'url': [
        r'https://www.python.org/static/community_logos/python-powered-h-50x65.png',
        r'https://www.python.org/static/community_logos/python-powered-h.svg',
        r'https://www.python.org/static/community_logos/python-logo-master-v3-TM.psd',
        r'https://www.gov.br/ana/pt-br/todos-os-documentos-do-portal/doc-modelo.pdf/@@download/file/doc-modelo.pdf',
        r'https://portal.ead.senasp.gov.br/noticias/ciclos/resultado-preliminar-2013-selecao-de-tutores-ajap-va-1/modelo-de-declaracao.docx/@@download/file/MODELO%20DE%20DECLARA%C3%87%C3%83O.docx',
    ],
    'path': [
        Path(__file__).parents[1] / 'dojo20241118' / 'files' / 'filedocx.docx',
        Path(__file__).parents[1] / 'dojo20241118' / 'files' / 'fileodt.odt',
        Path(__file__).parents[1] / 'dojo20241118' / 'files' / 'filexlsx.xlsx',
        Path(__file__).parents[1] / 'dojo20241118' / 'files' / 'filepdf.pdf',
    ],
}


def with_filetype(file: str | Path) -> str:
    """Identify type with filetype."""
    logging.debug(inspect.stack()[0][1])
    kind = filetype.guess(file)
    return kind.mime


def with_magic(file: str) -> str:
    """Identify type with magic."""
    logging.debug('%s: %s', inspect.stack()[0][1], file)
    # mime = magic.Magic(mime=True)
    # return mime.from_file(file)
    return 'desativado por incompatibilidade com multiplataforma.'


def with_puremagic(file: str) -> str:
    """Identify type with magic."""
    logging.debug('%s: %s', inspect.stack()[0][1], file)
    mime = puremagic.magic_file(file)
    return mime[0].mime_type


def dojo(file: str | Path, *, method: Method = 'puremagic') -> str:
    """Dojo solution."""
    logging.debug('%s: %s', inspect.stack()[0][1], file)
    if not file.is_file():
        return f'Arquivo "{file.as_posix()}" inexistente ou inválido!'

    match method:
        case 'magic':
            result = with_magic(file)
            logging.debug('python-magic, %s: %s', result, file)
            return result
        case 'filetype':
            result = with_filetype(file)
            logging.debug('filetype, %s: %s', result, file)
            return result
        case 'puremagic':
            result = with_puremagic(file)
            logging.debug('puremagic, %s: %s', result, file)
            return result
        case _:
            return f'Método inválido utilize: {get_args(Method)}'
