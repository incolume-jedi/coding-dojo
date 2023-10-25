from incolume.py.coding_dojo_jedi.dojo20231025.dojo import generator_sumary
from pathlib import Path


def test_quantia()->None:
    """Testar quantidade de links e dojos são iguais."""
    assert generator_sumary() == len(list(Path(__file__).absolute().parents[1].rglob('dojo*')))

# link correto
# escopo sumário