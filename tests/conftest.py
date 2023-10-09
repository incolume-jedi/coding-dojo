"""Configure switch test."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import version_info

import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope='session')
def semver_regex() -> str:
    """Fixture para regex de validação do Versionamento Semântico."""
    return r'^\d+(\.\d+){2}((-\w+\.\d+)|(\w+\d+))?$'


collect_ignore = ['incolume/py/20220928']


if version_info < (3, 10, 0):
    collect_ignore.extend(
        (
            'incolume/py/20220720',
            'incolume/py/20220808',
            'incolume/py/20220910',
        ),
    )
