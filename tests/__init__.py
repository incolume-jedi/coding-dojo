"""Test module."""

import sys

import pytest

pytestmark = pytest.mark.skip('All tests still WIP')

Py38 = pytest.mark.skipif(
    sys.version_info < (3, 8),
    reason='This run only Python 3.8 or higher',
)
Py39 = pytest.mark.skipif(
    sys.version_info < (3, 9),
    reason='This run only Python 3.9 or higher',
)
Py310 = pytest.mark.skipif(
    sys.version_info < (3, 10),
    reason='requires python3.10 or higher',
)
Py311 = pytest.mark.skipif(
    sys.version_info < (3, 11),
    reason='requires python3.11 or higher',
)
Py312 = pytest.mark.skipif(
    sys.version_info < (3, 12),
    reason='requires python3.12 or higher',
)
Py313 = pytest.mark.skipif(
    sys.version_info < (3, 13),
    reason='requires python3.13 or higher',
)
require_mac = pytest.mark.skipif(
    not sys.platform.casefold().startswith('mac'),
    reason='requires MacOS',
)
not_mac = pytest.mark.skipif(
    sys.platform.casefold().startswith('mac'),
    reason='does not run on MacOS',
)
require_lin = pytest.mark.skipif(
    not sys.platform.casefold().startswith('lin'),
    reason='requires Linux',
)
not_lin = pytest.mark.skipif(
    sys.platform.casefold().startswith('lin'),
    reason='does not run on Linux',
)
require_win = pytest.mark.skipif(
    sys.platform.casefold().startswith('win'),
    reason='requires windows',
)
not_win = pytest.mark.skipif(
    not sys.platform.casefold().startswith('win'),
    reason='does not run on windows',
)
