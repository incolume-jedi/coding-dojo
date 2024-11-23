"""Configure switch test."""

import sys
from pathlib import Path
from sys import version_info

import pytest
from dotenv import load_dotenv
from incolume.py.coding_dojo_jedi.utils import genfile

load_dotenv()


def pytestmark():
    """Mark for still WIP."""
    return pytest.mark.skip('This test still WIP')


def py38():
    """Mark for Python 3.8 or lower."""
    return pytest.mark.skipif(
        sys.version_info < (3, 8),
        reason='This run only Python 3.8 or higher',
    )


def py39():
    """Mark for Python 3.9 or lower."""
    return pytest.mark.skipif(
        sys.version_info < (3, 9),
        reason='This run only Python 3.9 or higher',
    )


def py310():
    """Mark for Python 3.10 or lower."""
    return pytest.mark.skipif(
        sys.version_info < (3, 10),
        reason='requires python3.10 or higher',
    )


def py311():
    """Mark for Python 3.11 or lower."""
    return pytest.mark.skipif(
        sys.version_info < (3, 11),
        reason='requires python3.11 or higher',
    )


def py312():
    """Mark for Python 3.12 or lower."""
    return pytest.mark.skipif(
        sys.version_info < (3, 12),
        reason='requires python3.12 or higher',
    )


def py313():
    """Mark for Python 3.13 or lower."""
    return pytest.mark.skipif(
        sys.version_info < (3, 13),
        reason='requires python3.13 or higher',
    )


def py314():
    """Mark for Python 3.14 or lower."""
    return pytest.mark.skipif(
        sys.version_info < (3, 14),
        reason='requires python3.14 or higher',
    )


def require_mac():
    """Required MacOS/IOS."""
    return pytest.mark.skipif(
        not sys.platform.casefold().startswith('mac'),
        reason='requires MacOS',
    )


def not_mac():
    """Not run on IOS."""
    return pytest.mark.skipif(
        sys.platform.casefold().startswith('mac'),
        reason='does not run on MacOS',
    )


def require_lin():
    """Required Linix."""
    return pytest.mark.skipif(
        not sys.platform.casefold().startswith('lin'),
        reason='requires Linux',
    )


def not_lin():
    """Not run on Linux."""
    return pytest.mark.skipif(
        sys.platform.casefold().startswith('lin'),
        reason='does not run on Linux',
    )


def require_win():
    """Required MS-Windows."""
    return pytest.mark.skipif(
        sys.platform.casefold().startswith('win'),
        reason='requires windows',
    )


def not_win():
    """Not run on MS-Windows."""
    return pytest.mark.skipif(
        not sys.platform.casefold().startswith('win'),
        reason='Not available on windows. Requires other Operation System.',
    )


collect_ignore = [
    'incolume/py/dojo20220928',
]


if version_info < (3, 10, 0):  # noqa: UP036
    collect_ignore.extend(
        (
            'incolume/py/dojo20220720',
            'incolume/py/dojo20220808',
            'incolume/py/dojo20220910',
        ),
    )


@pytest.fixture(scope='session')
def semver_regex() -> str:
    """Fixture para regex de validação do Versionamento Semântico."""
    return r'^\d+(\.\d+){2}((-\w+\.\d+)|(\w+\d+))?$'


@pytest.fixture
def fakefile() -> Path:
    """Return fiction file for tests."""
    return genfile(prefix='File-testing-')
