"""Module test for principal package."""


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
        (
            configfile,
            versionfile,
        ),
    )
    def test_exists(self, entrance):
        """Test if exists files."""
        assert entrance.exists(), f'{entrance=}'

    @pytest.mark.parametrize(
        'entrance',
        (
            configfile,
            versionfile,
        ),
    )
    def test_is_file(self, entrance):
        """Test if are files."""
        assert entrance.is_file(), f'{entrance=}'

    @pytest.mark.parametrize(
        'entrance',
        (
            configfile,
            versionfile,
        ),
    )
    def test_same_version(self, entrance):
        """Test same version."""
        try:
            with entrance.open('rb') as stream:
                version = load(stream)['tool']['poetry']['version']
        except ValueError:
            version = entrance.read_text().strip()
        assert version == __version__
