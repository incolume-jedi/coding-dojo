"""utils module."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'  # pragma: no cover

import logging
import re
from pathlib import Path

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
    except Exception as err:   # noqa: BLE001 pylint: disable=W0718
        logging.error(err)   # noqa: TRY400
    return False


def generator_sumary(fout: Path | None = None, reverse: bool = False) -> Path:
    """Gerador de sumário."""
    file = fout or Path().parent.joinpath('sumario.md')
    file.parent.mkdir(parents=True, exist_ok=True)
    regex = r'## Problema\s*\*\*((\w+\s*)+)\*\*'

    with file.open('w') as fmd:
        fmd.writelines(
            [
                '# Coding Dojo\n\n',
                '**Guilda JEDI Incolume - Grupo Python Incolume**\n\n',
                '- [Seja membro da Guilda JEDI Incolume]'
                '(https://discord.gg/eBNamXVtBW)\n\n',
                '## Sumário dos dojos\n\n',
                '---\n\n',
            ],
        )
        for filemd in sorted(
            Path(__file__).parents[1].rglob('**/*.md'),
            reverse=reverse,
        ):
            try:
                result = re.search(regex, filemd.read_text(), flags=re.I)
                title = filemd.parts[-2].capitalize()
                desc = result.group(1)  # type: ignore[union-attr]
                link = Path().joinpath(*filemd.parts[-2:])
                sout = f'1. [{title} &#8212; {desc}]({link})\n'
                fmd.write(sout)
            except AttributeError:  # noqa: PERF203
                pass
        fmd.writelines(
            [
                '\n---\n\n',
                'Copyrigth &copy; **Incolume.com.br** since 2010\n\n',
            ],
        )
    return file
