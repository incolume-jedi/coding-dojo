"""utils module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'  # pragma: no cover

import datetime
import logging
import os
import re
from http import HTTPStatus
from inspect import stack
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Final

import pytz
import requests
from icecream import ic

ic.disable()
if os.getenv('DEBUG_MODE'):
    ic.enable()

MD_DIR: Final[Path] = (
    Path(__file__).parents[3].joinpath('incolume', 'py', 'coding_dojo_jedi')
)
TZ: Final[str] = 'America/Sao_Paulo'

sumary_regex: str = r'## Problema\s*\*\*((\w[\.\:\-,!\?\(\)\s]*\s*)+)\*\*'


def whoami(cls):
    """Its Class name decorator."""
    cls.class_name = cls.__name__
    cls.whoami = cls.__name__
    return cls


def pseudo_filename(**kwargs: str) -> Path:
    """Return a temporary filename."""
    with NamedTemporaryFile(**kwargs) as f:
        return Path(f.name)


def check_connectivity(
    url: str = 'https://google.com',
    timeout: float = 1.8,
) -> bool:
    """Check web connectivity."""
    try:
        req = requests.get(url, timeout=timeout)
        if req.status_code == HTTPStatus.OK:
            return True
    except Exception:  # pylint: disable=W0718
        msg = 'Connection offline.'
        logging.exception(msg)
    return False


def file_filter(file: Path, regex: str = '') -> bool:
    """Filter files."""
    logging.debug('called %s', stack()[0][3])
    with file.open('rb') as f:
        for line in f:
            if re.search(regex, line, flags=re.IGNORECASE):
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
    return pseudo_filename(prefix=prefix, suffix=suffix)


def sumary(
    regex: str = '',
    *,
    reverse: bool = True,
    is_doc: bool = False,
) -> tuple[int, list[str]]:
    """Get sumary content."""
    regex = regex or sumary_regex
    l_out: list[str] = []
    year: str = ''
    for count, filemd in enumerate(
        sorted(filesmd(), reverse=reverse),
        start=1,
    ):
        logging.debug('iteration %s %s', count, filemd)
        try:
            result = re.search(
                regex,
                filemd.read_text(encoding='utf-8'),
                flags=re.IGNORECASE,
            )
            title = filemd.parts[-2].capitalize()
            logging.debug(title)
            desc = result.group(1)  # type: ignore[union-attr]
            logging.debug(desc)
            link = '/'.join(filemd.parts[-2:])
            logging.debug(link)
            if is_doc and year != (
                ano := ''.join(c for c in title if c.isdigit())[:4]
            ):
                year = ano
                l_out.append(f'\n\n### {year}\n\n')
            value = (
                (
                    f' - [{title} &#8212; {desc}](https://github.com/incolume-jedi/coding-dojo/tree/dev/incolume/py/coding_dojo_jedi/{link}){chr(123)}:target="_blank"{chr(125)}\n'
                )
                if is_doc
                else f' - [{title} &#8212; {desc}]({link})\n'
            )
            l_out.append(value)
        except AttributeError:
            pass
    return count, l_out


def generator_sumary(
    fout: Path | None = None,
    *,
    regex: str = '',
    reverse: bool = False,
    is_doc: bool = False,
) -> Path:
    """Gerador de sumário."""
    logging.debug('called %s', stack()[0][3])
    file = fout or (
        Path(__file__)
        .parents[3]
        .joinpath('docs', 'user_guide', 'dojos-resolvidos.md')
        if is_doc
        else Path().parent.joinpath('sumario.md')
    )
    file.parent.mkdir(parents=True, exist_ok=True)

    sout: list[str | bytes] = [
        '# Coding Dojo\n\n',
        '**Guilda JEDI Incolume - Grupo Python Incolume**\n\n',
        '- [Seja membro da Guilda JEDI Incolume]'
        '(https://discord.gg/eBNamXVtBW)\n\n',
        '## Sumário dos dojos\n\n',
        '---\n\n',
    ]
    count, temp_sout = sumary(regex=regex, reverse=reverse, is_doc=is_doc)

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


def dojo_init(
    dojo_path: Path | str | None = None,
    dojo_date: datetime.datetime | None = None,
    time_zone: str = '',
) -> list[Path]:
    """Create dojo structure."""
    dojo_path = Path(dojo_path) or MD_DIR
    time_zone = time_zone or TZ
    timestamp = dojo_date.strftime('%Y%m%d') or datetime.datetime.now(
        tz=pytz.timezone(time_zone),
    ).strftime('%Y%m%d')
    dojo_dir = dojo_path.joinpath(f'dojo{timestamp}')
    dojo_dir.mkdir(exist_ok=True)

    boilerplate: dict[str, bytes] = {
        'README.md': (
            ''
            '# Coding Dojo\n\n'
            '**Guilda JEDI Incolume - Grupo Python Incolume**\n\n'
            '- _[Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)_\n\n'
            '---\n\n\n'
            '![Python](https://img.shields.io/badge/Python-512BD4?style=flat'
            '&logo=python&logoColor=yellow) '
            '![JEDI Incolume](https://img.shields.io/badge/incolume-JEDI-blue'
            '?style=flat) '
            '[![GitHub release](https://img.shields.io/github/v/release/incolume-jedi/'
            'coding-dojo?logo=github&logoColor=white)]'
            '(https://github.com/incolume-jedi/coding-dojo/releases/latest) '
            '![PyCharm](https://img.shields.io/badge/PyCharm-AABBCC?'
            'style=flat) '
            '![VS Code](https://img.shields.io/badge/VScode-AABBCC?'
            'style=flat&logo=visualstudiocode&logoColor=white) '
            '![VS Code](https://img.shields.io/badge/CodeSpace-AABBCC?'
            'style=flat&logo=visualstudiocode&logoColor=white)\n\n'
            '---\n\n'
            '## Problema\n\n'
            '**Título do problema**\n\n'
            'Descrição/apresentação do problema.\n\n'
            '## Exemplos\n\n'
            '<details> \n'
            '  <summary>Spoiler?</summary> \n'
            '   Considerar em caso de fatoração:\n\n'
            '    > modo pythônico\n'
            '    > sem condicionais \n'
            '    > estruturas performáticas\n'
            '    > redução de complexidade ciclomática \n'
            '    > análise assintótica de algoritmos (big O)\n\n'
            '</details>\n\n'
            'N/A - Exemplos de solução e resposta do problema.'
            ' Geralmente utilizado para validar os testes do TDD.\n\n'
            '## Artefatos\n\n'
            '- [dojo](__init__.py)\n'
            f'- [tests](test_{timestamp}.py)\n\n'
            '## Referências\n\n'
            'N/A - Referências para o dojo, '
            'o problema ou para elicidações extras.\n'
            '---\n\n'
            'Copyright &copy; **incolume.com.br** since 2010\n'
        ),
        '__init__.py': (
            '"""dojo module."""\n\n'
            'from __future__ import annotations\n\n'
            'def dojo(*args: str, **kwargs: str)->dict[str]:\n'
            '    """Dojo solution."""\n'
            '    kwargs["args"] = args\n'
            '    return kwargs\n'
        ),
        f'test_{timestamp}.py': '"""Test module."""\n\n'
        'from __future__ import annotations\n'
        'from typing import ClassVar, NoReturn\n'
        f'import {".".join(dojo_dir.parts)} as pkg\n'
        'import pytest\n\n'
        'class TestCase:\n'
        '    """Test case class."""\n\n'
        '    t0: ClassVar=None\n\n'
        '    @pytest.mark.parametrize(\n'
        "        'entrance expected'.split(),\n"
        '        [\n'
        '             pytest.param(None, None, marks=['
        'pytest.mark.xpass(reason="Implementation failing (but shoulded ran)")'
        ']),\n'
        '        ],\n'
        '    )\n'
        '    def test_0(self, entrance, expected) -> NoReturn:\n'
        '        """Unittest."""\n'
        '        assert pkg.dojo(entrance) == expected\n',
    }
    result = []
    try:
        for file, content in boilerplate.items():
            result.append(dojo_dir.joinpath(file))
            ic(ic(result[-1]).write_bytes(content.encode('utf-8')))
    except PermissionError:
        pass
    return result


def run():
    """Run it."""
    files = filesmd()
    logging.debug(len(files))
    logging.debug(files)
    generator_sumary()


if __name__ == '__main__':  # pragma: no cover
    run()
