"""Unittest for dojo."""

import pytest

from incolume.py.coding_dojo_jedi.dojo20220731.dojo20220731 import (
    show_table_ascii,
)


def test_show_table_ascii() -> None:
    """Test show table ascii."""
    assert (65, 'A') in show_table_ascii()


@pytest.mark.parametrize(
    'entrada',
    [
        (65, 'A'),
        (66, 'B'),
        (67, 'C'),
        (68, 'D'),
        (69, 'E'),
        (63, '?'),
        (4, '\x04'),
        (219, '\xdb'),
        (128, '\x80'),
    ],
)
def test_show_table_ascii_0(entrada) -> None:
    """Test show table ascii."""
    assert entrada in show_table_ascii()
