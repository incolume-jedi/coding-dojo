from dojo20220729 import dna2rna


def test_dna2rna_0():
    assert dna2rna('') == ''


def test_dna2rna_1():
    assert dna2rna('GCAT') == 'GCAU'


def test_dna2rna_2():
    assert dna2rna('GCATGCAT') == 'GCAUGCAU'
