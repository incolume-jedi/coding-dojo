# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**
## Problema

**Classificação de Valores (Maiores e Menores)**

Data um lista com números naturais. Crie um programa que receba a quantia de classificação e uma lista, e faça as seguintes classificações:

1.    O maior e menor.;
2.    Os 4 maiores e os 4 menores;
3.    Os 7 maiores e os 7 menores;

## Exemplos

``` classify(1, [33, 37, 87, 87, 23]) == (87, 23)
    classify(4, [33, 37, 87, 87, 23]) == ((87, 87, 37, 33), (23, 33, 37, 87))
    classify(7, [33, 37, 87, 87, 23, 83, 29, 85, 18, 28, 82, 93, 23, 16, 9]) == ((93, 87, 87, 85, 83, 82, 37), (9, 16, 18, 23, 23, 28, 29))
```
Crie outros 10 testes diferentes.

Obs:

   - Utilize o comando random para gerar outras listas.

    random.seed(13); [random.randint(0, 100) for _ in range(50)]

   - Aplique soluções pythonicas com o comando heapq

## Artefatos

- [dojo](.//dojo20220819.py)
- [tests](./test_20220819.py)

## Referências

https://www.youtube.com/shorts/lnTPnx9O6nM
