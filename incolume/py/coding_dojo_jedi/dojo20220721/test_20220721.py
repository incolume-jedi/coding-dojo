# !/usr/bin/env python
from os import environ

from incolume.py.coding_dojo_jedi.dojo20220721.dojo20220721 import saudacao


def test_saudacao(capsys):
    timeout = float(environ.get('TIMEOUT', 9))
    saudacao(timeout)
    output = capsys.readouterr()
    assert output.out.strip() == 'Hello, Luke Skywalker!'
