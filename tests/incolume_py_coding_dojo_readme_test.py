"""Test for dojo README.md."""

import re

import pytest

from incolume.py.coding_dojo_jedi.utils import filesmd

__author__ = '@britodfbr'  # pragma: no cover


@pytest.mark.parametrize(
    'file',
    filesmd(),
)
def test_has_artefact(file) -> None:
    """Teste se há sessão Artefatos."""
    assert b'Artefatos' in file.read_bytes(), (
        f'Existe a sessão "## Artefatos" em {file.as_posix()}?'
    )


@pytest.mark.parametrize(
    'file',
    filesmd(),
)
def test_has_dojo_link(file) -> None:
    """Teste se há link dojo na sessão Artefatos."""
    regex = rb'- \[dojo\]\(.*\.py\)'
    assert re.search(
        regex,
        file.read_bytes(),
        re.IGNORECASE,
    ), f'Falta o link: "- [dojo](./dojoYYYYMMDD.py)" em {file.as_posix()}'


@pytest.mark.parametrize(
    'file',
    filesmd(),
)
def test_has_test_link(file) -> None:
    """Teste se há link para testes do dojo na sessão Artefatos."""
    regex = rb'- \[tests\]\((\.\/)?(test_.*\.py|tests\/.*\.txt)\)'
    assert re.search(
        regex,
        file.read_bytes(),
        re.IGNORECASE,
    ), f'Falta o link: "- [tests](./test_YYYYMMDD.py)" em {file.as_posix()}'
