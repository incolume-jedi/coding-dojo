"""Module test for principal package."""

from pathlib import Path

import pytest

from incolume.py.coding_dojo_jedi import (
    __version__,
    configfile,
    load,
    versionfile,
)

__author__ = '@britodfbr'  # pragma: no cover


@pytest.mark.fast()
class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'entrance',
        [
            configfile,
            versionfile,
        ],
    )
    def test_exists(self, entrance: Path) -> None:
        """Test if exists files."""
        assert entrance.exists(), f'{entrance=}'

    @pytest.mark.parametrize(
        'entrance',
        [
            configfile,
            versionfile,
        ],
    )
    def test_is_file(self, entrance: Path) -> None:
        """Test if are files."""
        assert entrance.is_file(), f'{entrance=}'

    @pytest.mark.parametrize(
        'entrance',
        [
            configfile,
            versionfile,
        ],
    )
    def test_same_version(self, entrance: Path) -> None:
        """Test same version."""
        try:
            version = load(entrance)['tool']['poetry']['version']
        except ValueError:
            version = entrance.read_text().strip()
        assert version == __version__
