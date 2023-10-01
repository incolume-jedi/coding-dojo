"""Configure switch test."""
from sys import version_info

import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope='session')
def semver_regex():
    """Fixture para regex de validação do Versionamento Semântico."""
    return r'^\d+(\.\d+){2}((-\w+\.\d+)|(\w+\d+))?$'


collect_ignore = ['incolume/py/20220928']

if version_info < (3, 8, 0):
    collect_ignore.extend(
        (
            'incolume/py/20220722',
            'incolume/py/20220902',
            'incolume/py/20220905',
        )
    )


if version_info < (3, 9, 0):
    collect_ignore.extend(('incolume/py/20220725', 'incolume/py/20220727'))


if version_info < (3, 10, 0):
    collect_ignore.extend(
        (
            'incolume/py/20220720',
            'incolume/py/20220808',
            'incolume/py/20220910',
        )
    )
