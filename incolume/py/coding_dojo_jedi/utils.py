"""utils module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'  # pragma: no cover

import logging
import re
from http import HTTPStatus
from inspect import stack
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Final

import requests

MD_DIR: Final[Path] = (
    Path(__file__).parents[3].joinpath('incolume', 'py', 'coding_dojo_jedi')
)


def check_connectivity(
    url: str = 'https://google.com',
    timeout: float = 1.8,
) -> bool:
    """Check web connectivity."""
    req = requests.get(url, timeout=timeout)
    try:
        if req.status_code == HTTPStatus.OK:
            return True
    except Exception:  # pylint: disable=W0718
        logging.exception()
    return False


def file_filter(file: Path, regex: str = '') -> bool:
    """Filter files."""
    logging.debug('called %s', stack()[0][3])
    with file.open('rb') as f:
        for line in f:
            if re.search(regex, line, flags=re.I):
                return True
    return False


def filesmd(dir_target: Path | None = None) -> list[Path]:
    """Get files.md on directories."""
    logging.debug('called %s', stack()[0][3])
    regex = rb'## Problema\s*'
    dir_target = dir_target or MD_DIR
    glob = dir_target.rglob('dojo*/*.md')

    files = [file for file in glob if file_filter(file, regex)]
    logging.debug(files)
    return files


def genfile(prefix: str = 'File', suffix: str = '') -> Path:
    """Return empty file."""
    return Path(NamedTemporaryFile(prefix=prefix, suffix=suffix).name)


def generator_sumary(
    fout: Path | None = None,
    *,
    reverse: bool = False,
) -> Path:
    """Gerador de sumário."""
    logging.debug('called %s', stack()[0][3])
    file = fout or Path().parent.joinpath('sumario.md')
    file.parent.mkdir(parents=True, exist_ok=True)
    regex = r'## Problema\s*\*\*((\w+\s*)+)\*\*'

    sout: list[str] = [
        '# Coding Dojo\n\n',
        '**Guilda JEDI Incolume - Grupo Python Incolume**\n\n',
        '- [Seja membro da Guilda JEDI Incolume]'
        '(https://discord.gg/eBNamXVtBW)\n\n',
        '## Sumário dos dojos\n\n',
        '---\n\n',
    ]
    count: int = 0
    temp_sout: list = []

    for count, filemd in enumerate(
        sorted(filesmd(), reverse=reverse),
        start=1,
    ):
        logging.debug('iteration %s %s', count, filemd)
        try:
            result = re.search(
                regex,
                filemd.read_text(encoding='utf-8'),
                flags=re.I,
            )
            title = filemd.parts[-2].capitalize()
            logging.debug(title)
            desc = result.group(1)  # type: ignore[union-attr]
            logging.debug(desc)
            link = Path().joinpath(*filemd.parts[-2:])
            logging.debug(link)
            temp_sout.append(f' - [{title} &#8212; {desc}]({link})\n')
        except AttributeError:
            pass

    sout.append(f'{count} dojos resolvidos\n\n---\n\n')
    sout += [
        *temp_sout,
        '\n---\n\n',
        'Copyrigth &copy; **Incolume.com.br** since 2010\n\n',
    ]
    sout = [bytes(content, encoding='utf-8') for content in sout]

    with file.open('wb') as fmd:
        fmd.writelines(sout)

    return file


def run():
    """Run it."""
    files = filesmd()
    logging.debug(len(files))
    logging.debug(files)
    generator_sumary()


if __name__ == '__main__':  # pragma: no cover
    run()
