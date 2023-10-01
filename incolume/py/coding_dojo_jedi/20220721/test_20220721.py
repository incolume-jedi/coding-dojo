# !/usr/bin/env python
from os import environ

from dojo20220721 import saudacao


def test_saudacao(capsys):
    timeout = float(environ.get('TIMEOUT', 9))
    saudacao(timeout)
    output = capsys.readouterr()
    assert output.out.strip() == 'Hello, Luke Skywalker!'
