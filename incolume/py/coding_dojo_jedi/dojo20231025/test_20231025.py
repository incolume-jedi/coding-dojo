from incolume.py.coding_dojo_jedi.dojo20231025.dojo import generator_sumary
from pathlib import Path


def test_quantia()->None:
    """Testar se a quantidade de links e dojos são iguais."""

    def count_links(arq_entrada: Path) -> int:
        """Contar os links do sumario.md."""
        contagem = 0
        with arq_entrada.open() as f:  
            for line in f:
                if line.startswith('1'):
                    contagem += 1
        return contagem


    assert count_links(generator_sumary()) == len(list(Path(__file__).absolute().parents[1].rglob('dojo*')))

# link correto
# escopo sumário