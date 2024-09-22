"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20240910 as pkg
import pytest


class TestCase:
    """Test case class."""

    instance: ClassVar = pkg.Caesar(key=2)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (0, pkg.Mode.DECRYPT),
            (1, pkg.Mode.ENCRYPT),
            (True, pkg.Mode.ENCRYPT),
            (False, pkg.Mode.DECRYPT),
            ('a', pkg.Mode.ENCRYPT),
        ],
    )
    def test_0(self, entrance, expected):
        """Unit test."""
        assert pkg.Mode(entrance) == expected

    @pytest.mark.parametrize(
        'entrance',
        [
            0,
            17,
            1.9,
            'a',
        ],
    )
    def test_1(self, entrance):
        """Unit test."""
        assert isinstance(pkg.Caesar(key=entrance), pkg.Caesar)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                'a ligeira raposa marrom saltou sobre o cachorro cansado!',
                'aWBRWligeiraWBRWraposaWBRWmarromWBRWsaltouWBRWsobreWBRWoWBRWcachorroWBRWcansadoWEXW',
            ),
            (
                'aWBRWligeiraWBRWraposaWBRWmarromWBRWsaltouWBRWsobreWBRWoWBRWcachorroWBRWcansadoWEXW',
                'a ligeira raposa marrom saltou sobre o cachorro cansado!',
            ),
        ],
    )
    def test_2(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert self.instance.prepara_frase(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                {
                    'data': 'a ligeira raposa marrom'
                    ' saltou sobre o cachorro cansado!',
                },
                'cZDTZnkigktcZDTZtcrqucZDTZocttqoZDTZucnvqwZDTZuqdtg'
                'ZDTZqZDTZecejqttqZDTZecpucfqZGXZ',
            ),
            (
                {
                    'data': 'cZDTZnkigktcZDTZtcrqucZDTZocttqoZDTZucnvqw'
                    'ZDTZuqdtgZDTZqZDTZecejqttqZDTZecpucfqZGXZ',
                    'mode': pkg.Mode.DECRYPT,
                },
                'a ligeira raposa marrom saltou sobre o cachorro cansado!',
            ),
        ],
    )
    def test_3(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert self.instance.apply(**entrance) == expected
