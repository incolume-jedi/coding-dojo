# Coding Dojo
**Guilda JEDI Incolume - Grupo Python Incolume**

<span style="color:red">**Este dojo é continuação em [dojo20231003](../dojo20231003/README.md)** </span>


## Problema
**Subarray de soma máxima**

O problema do subarray de soma máxima consiste em encontrar a soma máxima de uma subsequência contígua em um array ou lista de inteiros:

    max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    # deve ser 6: [4, -1, 2, 1]
Caso fácil é quando a lista é composta apenas de números positivos e a soma máxima é a soma de todo o array.
Se a lista for composta apenas de números negativos, retorne 0.

A lista vazia é considerada como tendo a maior soma zero.
Observe que a lista ou matriz vazia também é uma sublista/subarray válida.

## Exemplos
    max_sequence([]) == 0
    max_sequence([-1, -2, -3, -4]) == 0
    max_sequence([-10, -2, -3, -1]) == 0
    max_sequence([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
    max_sequence([10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 55
    max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) ==  6
    max_sequence([10, -11, 2, 3, 4, 5, -5,  6, 7, -50, 8,-7, 9]) == 14

## Artefatos

- [dojo](./__init__.py)
- [test](./test_20231007.py)

## Referências
  - https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
