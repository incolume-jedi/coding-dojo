# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

---

## Problema

**Todos Números felizes menores que 100**

Um número é feliz se somando os quadrados de seus algarismos e iterando o processo seja possível chegar ao número 1.
Crie um programa que exiba todos números felizes menores ou iguais que 100.




## Exemplos

num_feliz(7) == [1, 7]
num_feliz(10) == [1, 7, 10]
num_feliz(100) == ??

7

iteração|algarismos|soma
----|---|----
1|7^2 | 49
2|4^2 + 9^2|  97
3|9^2 + 7^2|130
4|1^2 + 3^2 + 0^2| 10
5|1^2 + 0^2| 1

19

iteração|algarismos|soma
----|---|----
1|1^2 + 9^2 | 82
2|8^2 + 2^2|  68
3|6^2 + 8^2| 100
4|1^2 + 0^2 + 0^2| 1

## Artefatos

- [dojo](./__init__.py)
- [tests](./test_20240507.py)


## Referências
- #68
- https://www.youtube.com/shorts/QJ5UsV7Fr2g
- https://www.fq.math.ca/Scanned/39-5/grundman.pdf
