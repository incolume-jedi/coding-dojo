"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240909 as pkg
import pytest


class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('ESSE EXERCICIO-PROGRAMA VAI SER MUITO LEGAL.', ''),
            (
                'ESSEWBRWEXERCICIOWHFWPROGRAMAWBRWVAIWBRWSERWBRWMUITOWBRWLEGALWPTW',
                '',
            ),
            (
                'GUUGYDTYGZGTEKEKQYJHYRTQITCOCYDTYXCKYDTYUGTYDTYOWKVQYDTYNGICNYRVY',
                '',
            ),
            (
                'Está função deve ser implementada, é intermediária e '
                'executada tanto na cifra quanto na decifra.',
                '',
            ),
            ('FACIL? - SIMPLES!', 'FACILWINWWBRWWHFWWBRWSIMPLESWEXW'),
            ('FACILWINWWBRWWHFWWBRWSIMPLESWEXW', 'FACIL? - SIMPLES!'),
            ('a ligeira raposa marrom saltou sobre o cachorro cansado', ''),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.caesar(entrance) == expected
