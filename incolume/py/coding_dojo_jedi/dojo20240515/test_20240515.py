"""Test module."""

from incolume.py.coding_dojo_jedi.dojo20240515 import translate_deepl
import pytest


class CheckDeepl:
    """Check API de tradução."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('IT', 'Buona sera'),
            ('EN-US', 'Good evening'),
            ('DE', 'Guten Abend'),
            ('ES', 'Buenas noches'),
            ('FR', 'Bonsoir à tous'),
        ],
    )
    def test_tranlate_deepl(self, entrance, expected):
        """Test tranlate deepl."""
        assert translate_deepl('Boa Noite', entrance) == expected
