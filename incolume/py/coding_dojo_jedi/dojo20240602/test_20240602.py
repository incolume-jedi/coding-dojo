"""Module."""

from pathlib import Path

import pytest

from . import CBF

__author__ = '@britodfbr'  # pragma: no cover


class TestCaseCBF:
    """Test case."""

    url = 'http://localhost:8000'

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                'http://localhost:8000',
                '',
                marks=pytest.mark.webtest,
            ),
            pytest.param(
                Path(__file__).parent.joinpath('index.html').as_posix(),
                '',
            ),
        ],
    )
    def test_content(self, entrance, expected):
        """Test content."""
        obj = CBF(entrance)
        assert obj.content == expected
