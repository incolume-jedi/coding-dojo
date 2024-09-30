"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20240919 as pkg
import pytest


class TestCase:
    """Test case class."""

    t0: ClassVar = [
        (([1], 1), []),
        (([1, 2], 1), [1]),
        (([1, 2, 3, 4, 5], 2), [1, 2, 4, 5]),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        t0,
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(*entrance) == expected

    def test_nodo_push(self) -> NoReturn:
        """Test this."""
        entrance = 11
        expected = entrance
        lista = pkg.LinkedList()
        lista.push(entrance)
        assert lista.head.data == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        t0,
    )
    def test_nodo_index(self, entrance, expected) -> NoReturn:
        """Test this."""
        lista = pkg.LinkedList()
        [lista.push(x) for x in entrance[0]]
        print(lista.head)
        assert lista.head.next == entrance[1]

    @pytest.mark.skip
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        t0,
    )
    def test_delete(self, entrance, expected) -> NoReturn:
        """Unittest."""
        lista = pkg.LinkedList()
        [lista.push(x) for x in entrance[0]]
        lista.pop(entrance[1])
        assert lista.display() == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ([1, 2, 3], '3\n2\n1\n'),
            ([1], '1\n'),
        ],
    )
    def test_display(self, entrance, expected, capsys) -> NoReturn:
        """Unittest."""
        lista = pkg.LinkedList()
        [lista.push(x) for x in entrance]
        lista.display()
        result = capsys.readouterr()
        assert result.out == expected
