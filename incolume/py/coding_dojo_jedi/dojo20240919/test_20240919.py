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
        [
            ({1}, 0),
            ({1, 5, 9}, 2),
            ((1, 7, 3, 1, 5), 4),
        ],
    )
    def test_nodo_index(self, entrance, expected) -> NoReturn:
        """Test this."""
        lista = pkg.LinkedList()
        [lista.push(x) for x in entrance]
        assert lista.head.index == expected

    @pytest.mark.parametrize(
        'entrance',
        [
            [1, 2, 3],
            [11, 12, 13],
        ],
    )
    def test_get_values(self, entrance) -> NoReturn:
        """Test this."""
        lista = pkg.LinkedList()
        [lista.push(x) for x in entrance]
        assert lista.get_values() == entrance

    # @pytest.mark.skip
    @pytest.mark.parametrize(
        'entrance delete expected'.split(),
        [
            ([3, 2, 1], 2, [3, 2]),
            ([3, 2, 1], 1, [3, 1]),
        ],
    )
    def test_delete(self, entrance, delete, expected) -> NoReturn:
        """Unittest."""
        lista = pkg.LinkedList()
        [lista.push(x) for x in entrance]
        lista.pop(delete)
        assert lista.get_values() == expected

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
