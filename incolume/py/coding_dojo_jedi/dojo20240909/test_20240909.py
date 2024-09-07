"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20240909 as pkg
import pytest


class TestCase:
    """Test case class."""

    test_case0: ClassVar = [
        pytest.param(
            {
                'data': 'ESSE EXERCICIO-PROGRAMA VAI SER MUITO LEGAL.',
                'key': -2,
                'mode': 0,
            },
            'GUUGZDTZGXGTEKEKQZJHZRTQITCOCZDTZYCKZDTZUGTZDTZOWKVQZDTZNGICNZRVZ',
        ),
    ]
    test_case1: ClassVar = [
        pytest.param(
            {'frase': 'FACIL? - SIMPLES!'},
            'FACILWINWWBRWWHFWWBRWSIMPLESWEXW',
            marks=[],
        ),
        pytest.param(
            {
                'frase': 'FACILWINWWBRWWHFWWBRWSIMPLESWEXW',
            },
            'FACIL? - SIMPLES!',
            marks=[],
        ),
        pytest.param(
            {
                'frase': 'ESSEWBRWEXERCICIOWHFWPROGRAMAWBRWV'
                'AIWBRWSERWBRWMUITOWBRWLEGALWPTW',
            },
            'ESSE EXERCICIO-PROGRAMA VAI SER MUITO LEGAL.',
            marks=[],
        ),
    ]
    test_case2: ClassVar = [
        pytest.param(
            {
                'data': 'ESSE EXERCICIO-PROGRAMA VAI SER MUITO LEGAL.',
                'key': -2,
            },
            'GUUGYDTYGZGTEKEKQYJHYRTQITCOCYDTYXCKYDTYUGTYDTYOWKVQYDTYNGICNYRVY',
        ),
        pytest.param(
            {
                'data': 'GUUGYDTYGZGTEKEKQYJHYRTQITCOCYDTYXCKY'
                'DTYUGTYDTYOWKVQYDTYNGICNYRVY',
                'key': -2,
                'decrypt_mode': True,
            },
            'ESSE EXERCICIO-PROGRAMA VAI SER MUITO LEGAL.',
        ),
        pytest.param(
            {
                'data': 'Está função deve ser implementada, é '
                'intermediária e executada tanto na cifra '
                'quanto na decifra.',
            },
            'hVWázeuzIXQçãRzeuzGHYHzeuzVHUzeuzLPSOHPHQWDGDzyuzzeuzézeuzLQWHUPHGLáULDzeuzHzeuzHaHFXWDGDzeuzWDQWRzeuzQDzeuzFLIUDzeuzTXDQWRzeuzQDzeuzGHFLIUDzswz',
            marks=[],
        ),
        pytest.param(
            {
                'data': 'a ligeira raposa marrom saltou'
                ' sobre o cachorro cansado',
            },
            'DzeuzOLJHLUDzeuzUDSRVDzeuzPDUURPzeuzVDOWRXzeuzVREUHzeuzRzeuzFDFKRUURzeuzFDQVDGR',
            marks=[],
        ),
        pytest.param(
            {
                'data': 'a ligeira raposa marrom saltou'
                ' sobre o cachorro cansado',
                'key': 2,
            },
            'YUzPUjgecgpYUzPUpYnmqYUzPUkYppmkUzPUqYjrmsUzPUqmZpcUzPUmUzPUaYafmppmUzPUaYlqYbm',
            marks=[],
        ),
        pytest.param(
            {
                'data': 'a ligeira raposa marrom saltou'
                ' sobre o cachorro cansado',
                'key': -2,
            },
            'cYDTYnkigktcYDTYtcrqucYDTYocttqoYDTYucnvqwYDTYuqdtgYDTYqYDTYecejqttqYDTYecpucfq',
            marks=[],
        ),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test_case1,
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.prepara_frase(**entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test_case0,
    )
    def test_1(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.caesar(**entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(False, pkg.Mode.DECRYPT, marks=[]),
            pytest.param(True, pkg.Mode.ENCRYPT, marks=[]),
            pytest.param(None, pkg.Mode.ENCRYPT, marks=[]),
            pytest.param('', pkg.Mode.ENCRYPT, marks=[]),
        ],
    )
    def test_2(self, entrance, expected) -> NoReturn:
        """Unit test."""
        assert pkg.Mode(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test_case0,
    )
    def test_3(self, entrance, expected) -> NoReturn:
        """Unittest."""
        entrance['decrypt_mode'] = entrance.get('mode')
        del entrance['mode']
        assert pkg.cesar(**entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test_case2,
    )
    def test_4(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.cypher_cesar(**entrance) == expected
