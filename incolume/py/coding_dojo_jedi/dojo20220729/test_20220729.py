"""Unittest for dojo."""

from incolume.py.coding_dojo_jedi.dojo20220729.dojo20220729 import dna2rna


def test_dna2rna_0() -> None:
    """Test dna2rna."""
    assert not dna2rna('')


def test_dna2rna_1() -> None:
    """Test dna2rna."""
    assert dna2rna('GCAT') == 'GCAU'


def test_dna2rna_2() -> None:
    """Test dna2rna."""
    assert dna2rna('GCATGCAT') == 'GCAUGCAU'
