"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20240912 as pkg
import pytest


class TestCase:
    """Test case class."""

    instance: ClassVar = ''

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (('A'), 1),
            (('AAA', 'b'), 2),
        ],
    )
    def test_0(self, entrance, expected):
        """Unit test."""
        stack = pkg.Stack()
        for item in entrance:
            stack.push(item)
        assert stack.count == expected

    def test_1(self) -> NoReturn:
        """Unittest."""
        entrance = (
            (None, None),
            {'a': 1, 'b': 2},
            'Como a pilha é genérica, podemos inserir'
            ' quaisquer elementos,\n'
            'até objetos heterogêneos',
            {'MadeIn': 'Brazil'},
            'Execute esse código para ver a pilha ser invertida',
        )
        stack = pkg.Stack()
        for item in entrance:
            stack.push(item)

        total = -1

        while stack.count > 0:
            assert stack.pop() == entrance[total]
            total -= 1
