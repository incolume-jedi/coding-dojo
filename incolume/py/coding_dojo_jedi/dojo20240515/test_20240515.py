"""Test module."""

from unittest import mock
from http import HTTPStatus
from . import (
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

    @pytest.mark.skip(reason='replaced for test_translate_deepl_api_mock')
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        tests0,
    )
    def test_translate_deepl_api(self, entrance, expected):
        """Test tranlate deepl."""
        result = translate_deepl_api('Boa Noite', entrance)
        assert result['translations'][0]['text'] == expected

    @pytest.mark.skip(reason='replaced for test_translate_deepl_mock')
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        tests0,
    )
    def test_tranlate_deepl(self, entrance, expected):
        """Test tranlate deepl."""
        assert translate_deepl('Boa Noite', entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        tests0,
    )
    def test_translate_deepl_api_mock(self, entrance, expected):
        """Test tranlate deepl."""
        obj_resp = mock.MagicMock()
        obj_resp.status_code = HTTPStatus.OK
        obj_resp.json.return_value = {
            'translations': [
                {
                    'detected_source_language': 'PT',
                    'text': expected,
                },
            ],
        }
        with mock.patch('httpx.post', side_effect=[obj_resp]):
            result = translate_deepl_api(text='Boa Noite', lang=entrance)
            assert result['translations'][0]['text'] == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        tests0,
    )
    def test_tranlate_deepl_mock(self, entrance, expected):
        """Test tranlate deepl."""
        oresp = mock.MagicMock()
        oresp.translate_text.return_value.text = expected
        with mock.patch('deepl.Translator', return_value=oresp):
            assert translate_deepl('Boa Noite', entrance) == expected
