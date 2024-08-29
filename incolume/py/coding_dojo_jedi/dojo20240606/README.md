# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

- _[Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)_

---

## Problema

**Fatorar código - Performance pythonica**

No código a seguir aplique as melhores praticas de desenvolvimento para melhorá-lo.

```python
import time
import logging


def calc_square(l: list) -> list:
    """Quadrado de cada elemento da lista."""
    start = time.time()
    result = []
    for e in l:
        result.append(e*e)
    end = time.time()
    logging.debug('calc_square executou em %s milisegundos', start-end)
    return result


def calc_cube(l: list) -> list:
    """Cubo de cada elemento da lista."""
    start = time.time()
    result = []
    for e in l:
        result.append(e*e*e)
    end = time.time()
    logging.debug('calc_cube executou em %s milisegundos', start-end)
    return result
```

## Sugestões
- DRY;
- clousure/decoradores;
- separar a lógica da métrica no programa;

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

## Artefatos

- [dojo](./__init__.py)
- [tests](./test_20240606.py)


## Referências

N/A - Referências para o dojo, o problema ou para elucidações extras.

---

Copyright &copy; **incolume.com.br** since 2010
