"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241125 as pkg
import pytest


class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance expected exception'.split(),
        [
            pytest.param(
                'a' * 101,
                '',
                {
                    'expected_exception': SyntaxError,
                    'match': 'Tamanho da frase deve'
                    ' ser entre 1 e 100 caracteres.',
                },
                marks=[],
            ),
            pytest.param(
                'ab"fg',
                '',
                {
                    'expected_exception': SyntaxError,
                    'match': 'Caracteres inválidos: \' ou "',
                },
                marks=[],
            ),
            pytest.param(
                "ab'cd",
                '',
                {
                    'expected_exception': SyntaxError,
                    'match': 'Caracteres inválidos: \' ou "',
                },
                marks=[],
            ),
            pytest.param('ab-cd', 'dc-ba', None, marks=[]),
            pytest.param('a-bC-dEf-ghIj', 'j-Ih-gfE-dCba', None, marks=[]),
            pytest.param(
                'Test1ng-Leet=code-Q!',
                'Qedo1ct-eeLg=ntse-T!',
                None,
                marks=[],
            ),
        ],
    )
    def test_0(self, entrance, expected, exception) -> NoReturn:
        """Unittest."""
        if exception:
            with pytest.raises(**exception):
                pkg.dojo(entrance)
        else:
            assert pkg.dojo(entrance) == expected
