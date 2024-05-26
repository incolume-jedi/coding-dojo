"""Test module."""

from unittest import mock
from http import HTTPStatus
from incolume.py.coding_dojo_jedi.dojo20240515 import (
    translate_deepl,
    translate_deepl_api,
)
import pytest
from typing import ClassVar


class CheckDeepl:
    """Check API de tradução."""

    tests0: ClassVar = [
        ('IT', 'Buona sera'),
        ('EN-US', 'Good evening'),
        ('DE', 'Guten Abend'),
        ('ES', 'Buenas noches'),
        ('FR', 'Bonsoir à tous'),
    ]

    @pytest.mark.skip()
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        tests0,
    )
    def test_tranlate_deepl_api(self, entrance, expected):
        """Test tranlate deepl."""
        result = translate_deepl_api('Boa Noite', entrance)
        assert result['translations'][0]['text'] == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        tests0,
    )
    def test_tranlate_deepl_api_mock(self, entrance, expected):
        """Test tranlate deepl."""
        with mock.patch('httpx.post', return_value=mock.MagicMock()) as m_resp:
            m_resp.status_code = HTTPStatus.OK
            m_resp.json.return_value = {
                'translations': [
                    {
                        'detected_source_language': 'PT',
                        'text': expected,
                    },
                ],
            }
            result = translate_deepl_api(text='Boa Noite', lang=entrance)
            assert result == ''
            assert result['translations'][0]['text'] == expected

    @pytest.mark.skip()
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        tests0,
    )
    def test_tranlate_deepl(self, entrance, expected):
        """Test tranlate deepl."""
        assert translate_deepl('Boa Noite', entrance) == expected
