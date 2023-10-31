# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

---

## Problema

**TDD Pytest**

Baseado no exercício [TDD para Pytest](https://bitbucket.org/incolume-dev/calculadora_pytest)

```python
# tests.py
# -*- encode: utf-8 -*-

import pytest
from dojo import calculadora

@pytest.mark.parametrize(
    ['entrance', 'expected'],
    (
        (('+',3, '4'), 7),
        (('+', 3, 4), 7),
        (('-',3.0, 4), -1.0),
        (('-','3', 4), -1),
        (('*', 3, '4'), 12),
        (('*', 3, '4.0'), 12.0),
        (('/', 3, '4'), .75),
        (('/', 4, 4.0), 1.0),
        (('/', 4, 3.0), 1.3333333333333333),
        (('%', 4, 3), 1),
        (('%', 12, 7), 5),
        (('**', 3, 4), 81),
        (('**', 81, (1/4)), 3),
    )
)
def test_calculadora(entrance, expected):
    assert calculadora(*entrance) == expected

@pytest.mark.parametrize(
    ['entrance', 'expected'],
    (
        (('^', 3, 5), {'expected_exception': ValueError,
                       'match': re.escape('Operador inválido. Use: + - * ** / // %')}),
        (('/', 3, 0), {'expected_exception': ValueError, 'match': r'.*y deve ser diferente 0.*'}),
        (('/', '3', 0), {'expected_exception': ValueError, 'match': r'.*y deve ser diferente 0.*'}),
        (('/', 3, '0'), {'expected_exception': ValueError, 'match': r'.*y deve ser diferente 0.*'}),
        (('/', '3', '0'), {'expected_exception': ValueError, 'match': r'.*y deve ser diferente 0.*'}),
        (('//', 3, 0), {'expected_exception': ValueError, 'match': r'.*y deve ser diferente 0.*'}),
        (('//', '3', 0), {'expected_exception': ValueError, 'match': r'.*y deve ser diferente 0.*'}),
        (('//', 3, '0'), {'expected_exception': ValueError, 'match': r'.*y deve ser diferente 0.*'}),
        (('//', '3', '0'), {'expected_exception': ValueError, 'match': r'.*y deve ser diferente 0.*'}),
        (('+', 'a', 'b'), {'expected_exception': ValueError,
                       'match': r".*x e y devem ser valores numéricos reais.*"}),
        (('+', '0', 'b'), {'expected_exception': ValueError,
                           'match': r".*x e y devem ser valores numéricos reais.*"}),
        (('+', 'a', '0'), {'expected_exception': ValueError,
                           'match': r".*x e y devem ser valores numéricos reais.*"}),
        (('+', (3 + 0j), (2 + 0j)), {'expected_exception': ValueError,
                           'match': r".*x e y devem ser valores numéricos reais.*"}),
    )
)
def test_calculadora_except(entrance, expected):
    with pytest.raises(**expected):
        calculadora(*entrance)

```

## Exemplos

```bash
pytest tests.py
```

## Artefatos
- [dojo](./dojo20220720.py)
- [test](./test_20220720.py)


## Referências

https://bitbucket.org/incolume-dev/calculadora_pytest
