"""Test module."""

import sys

import pytest

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
