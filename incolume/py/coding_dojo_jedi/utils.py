"""utils module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'  # pragma: no cover

import logging
import re
from pathlib import Path
from tempfile import NamedTemporaryFile

import requests


def check_connectivity(
    url: str = 'https://google.com',
    timeout: float = 1.8,
) -> bool:
    """Check web connectivity."""
    req = requests.get(url, timeout=timeout)
    http_ok: int = 200
    try:
        if req.status_code == http_ok:
            return True
    except Exception as err:  # pylint: disable=W0718
        logging.exception(err)
    return False


def filesmd() -> list[Path]:
    """Get files.md on directories."""
    regex = r'## Problema\s*\*\*(([\w\d]+\s*)+)\*\*'
    files = [
        file
        for file in Path(__file__)
        .parents[3]
        .joinpath('incolume', 'py', 'coding_dojo_jedi')
        .rglob('**/*.md')
        if re.search(regex, file.read_text(encoding='utf-8'), flags=re.I)
    ]
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
    file = fout or Path().parent.joinpath('sumario.md')
    file.parent.mkdir(parents=True, exist_ok=True)
    regex = r'## Problema\s*\*\*((\w+\s*)+)\*\*'

    sout: list[str] = []
    for filemd in sorted(filesmd(), reverse=reverse):
        try:
            result = re.search(
                regex,
                filemd.read_text(encoding='utf-8'),
                flags=re.I,
            )
            title = filemd.parts[-2].capitalize()
            desc = result.group(1)  # type: ignore[union-attr]
            link = Path().joinpath(*filemd.parts[-2:])
            sout.append(f' - [{title} &#8212; {desc}]({link})\n')
        except AttributeError:
            pass

    with file.open('w') as fmd:
        fmd.writelines(
            [
                '# Coding Dojo\n\n',
                '**Guilda JEDI Incolume - Grupo Python Incolume**\n\n',
                '- [Seja membro da Guilda JEDI Incolume]'
                '(https://discord.gg/eBNamXVtBW)\n\n',
                '## Sumário dos dojos\n\n',
                '---\n\n',
                f'{len(sout)} dojos resolvidos\n\n---\n\n',
            ],
        )
        fmd.writelines(sout)
        fmd.writelines(
            [
                '\n---\n\n',
                'Copyrigth &copy; **Incolume.com.br** since 2010\n\n',
            ],
        )
    return file
