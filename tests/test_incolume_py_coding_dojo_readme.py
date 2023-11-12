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
    assert 'Artefatos' in file.read_text(encoding='utf-8')


@pytest.mark.parametrize(
    'file',
    filesmd(),
)
def test_has_dojo_link(file) -> None:
    """Teste se há link dojo na sessão Artefatos."""
    regex = r'- \[dojo\]\(.*\.py\)'
    assert re.search(regex, file.read_text(encoding='utf-8'), re.I)


@pytest.mark.parametrize(
    'file',
    filesmd(),
)
def test_has_test_dojo_link(file) -> None:
    """Teste se há link para testes do dojo na sessão Artefatos."""
    regex = r'- \[tests\]\((\.\/)?(test_.*\.py|tests\/.*\.txt)\)'
    assert re.search(regex, file.read_text(encoding='utf-8'), re.I)
