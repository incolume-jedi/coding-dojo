"""Test for dojo README.md."""
import logging
import re
from pathlib import Path

import pytest

__author__ = '@britodfbr'  # pragma: no cover


def filesmd() -> list[Path]:
    """Get files.md on directories."""
    regex = r'## Problema\s*\*\*((\w+\s*)+)\*\*'
    files = [
        file
        for file in Path(__file__)
        .parents[1]
        .joinpath('incolume', 'py', 'coding_dojo_jedi')
        .rglob('**/*.md')
        if re.search(regex, file.read_text(), flags=re.I)
    ]
    logging.debug(files)
    return files


@pytest.mark.parametrize(
    'file',
    filesmd(),
)
def test_has_artefact(file) -> None:
    """Teste se há sessão Artefatos."""
    assert 'Artefatos' in file.read_text()


@pytest.mark.parametrize(
    'file',
    filesmd(),
)
def test_has_dojo_link(file) -> None:
    """Teste se há link dojo na sessão Artefatos."""
    assert re.search(r'- \[dojo\]\(.*\.py\)', file.read_text(), re.I)


@pytest.mark.parametrize(
    'file',
    filesmd(),
)
def test_has_test_dojo_link(file) -> None:
    """Teste se há link para testes do dojo na sessão Artefatos."""
    regex = r'- \[tests\]\((\.\/)?(test_.*\.py|tests\/.*\.txt)\)'
    assert re.search(regex, file.read_text(), re.I)
