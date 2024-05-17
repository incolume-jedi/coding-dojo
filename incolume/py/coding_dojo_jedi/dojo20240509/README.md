# Coding Dojo
Guilda JEDI Incolume - Grupo Python Incolume

## Problema

**Romanos > Arábicos / Arábicos > Romanos**

Crie uma classe chamada numeros com 2 metodos (from_roman e to_roman), que convertam para números arábicos e romanos respectivamente.

## Exemplos
    to_roman(987) == CMLXXXVII
    to_roman(1978) == MCMLXXVIII
    to_roman(1) == I
    to_roman(2) == II
    to_roman(4) == IV
    to_roman(9) == IX
    to_roman(100) == C
    to_roman(50) == L
    to_roman(1000) == M
    to_roman(1988) == MCMLXXXVIII
    to_roman(2009) == MMIX
    to_roman(2011) == MMXI
    to_roman(500) == D
    to_roman(1500) == MD

    from_roman(CMLXXXVII) == 987
    from_roman(MCMLXXVIII) == 1978
    from_roman(I) == 1
    from_roman(II) == 2
    from_roman(IV) == 4
    from_roman(IX) == 9
    from_roman(C) == 100
    from_roman(L) == 50
    from_roman(M) == 1000
    from_roman(MCMLXXXVIII) == 1988
    from_roman(MMIX) == 2009
    from_roman(MMXI) == 2011
    from_roman(D) == 500
    from_roman(MD) == 1500

## Artefatos

- [dojo](./__init__.py)
- [tests](./test_20240509.py)


## Referências
- [new-dojo] Números Romanos para Arábicos  #40
- Números Arábicos para Romanos #39
