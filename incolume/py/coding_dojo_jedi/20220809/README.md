# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

---

## Problema

**TDD Doctest**

Baseado no exercício TDD para doctest https://bitbucket.org/incolume-dev/calculadora_doctest/src/0.2.1/
```python
# dojo.py
def calculadora():
    """Realiza uma operação matemática.

    :param op: operador (str),
    :param x: valor numérico (float|int|str)
    :param y: valor numérico (float|int|str)
    :return: retorna um valor numérico (float)
    """
    result = 0
    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/calc.txt")
```
```python
# tests/calc.txt
The ``calc`` module
======================

Using ``calculadora``
-------------------
This is an example text file in reStructuredText format (https://docs.python.org/2/library/doctest.html).
  First import ``calculadora`` from the ``calc`` module:

    >>> from dojo import calculadora

Now use it:
    >>> calculadora('+',3, 4)
    7

    Operações com int e float retornam float
    >>> calculadora('+',3, 4.0)
    7.0
    >>> calculadora('-',3, 4)
    -1
    >>> calculadora('-',3.0, 4)
    -1.0
    >>> calculadora('-',4, 3)
    1
    >>> calculadora('*',3, 4)
    12
    >>> calculadora('*',3, 4.0)
    12.0
    >>> calculadora('/',3, 4)
    0.75
    >>> calculadora('/',4, 3)
    1.3333333333333333
    >>> calculadora('//',4, 3)
    1

    Resto inteiro de uma divisão (mod)
    >>> calculadora('%', 4, 3)
    1
    >>> calculadora('%', 12, 7)
    5

    potência
    >>> calculadora('**',3, 4)
    81

    Exceções
    >>> calculadora('/', 3, 0)
    Traceback (most recent call last):
    ...
    ValueError: y deve ser diferente de 0
    >>> calculadora('//', 3, 0)
    Traceback (most recent call last):
    ...
    ValueError: y deve ser diferente de 0
    >>> calculadora('^', 3, 5)
    Traceback (most recent call last):
    ...
    ValueError: Operador inválido. Use: +, -, *, **, //, /, %
    >>> calculadora('+', 'a', 'b')
    Traceback (most recent call last):
    ...
    ValueError: x e y devem ser valores numéricos reais.
```


## Exemplos

Para executar os testes desenvolvidos para TDD em pydocs, rode o camando abaixo:

```python
python dojo.py
```

## Referências

https://bitbucket.org/incolume-dev/calculadora_doctest
