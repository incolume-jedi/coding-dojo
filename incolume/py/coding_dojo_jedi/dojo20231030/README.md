# Coding Dojo
**Guilda JEDI Incolume - Grupo Python Incolume**

[Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)

---

## Problema

**Exercitando TDD**

Implementar o conteúdo necessário para funcionar o teste apresentado.


```python
"""Clean Code in Python - Chapter 01: Introcution, Tools, and Formatting

Tests for annotations examples

"""
import pytest

from incolume.py.coding_dojo_jedi.dojoYYYYMMDD.dojo  import NewPoint, Point, locate


@pytest.mark.parametrize(
    "element,expected",
    (
        (Point, {"latitude": float, "longitude": float, "return": self}),
        (locate, {"latitude": float, "longitude": float, "return": Point}),
        (NewPoint, {"lat": float, "long": float}),
    ),
)
def test_annotations(element, expected):
    """test the class/functions againts its expected annotations"""
    assert getattr(element, "__annotations__") == expected

```

## Exemplos

<details> 
  <summary>Spoiler?</summary> 
   Considerar em caso de fatoração:

    > modo pythônico
    > sem condicionais 
    > estruturas performáticas
    > redução de complexidade ciclomática 
    > análise assintótica de algoritmos (big O)

</details>


N/A - Exemplos de solução e resposta do problema. Geralmente utilizado para validar os testes do TDD.

## Referências

- https://github.com/PacktPublishing/Clean-Code-in-Python/tree/master/Chapter01%2Fsrc
- N/A - Referências para o dojo, o problema ou para elicidações extras.

---

Copyright © incolume.com.br since 2010