# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

---

## Problema

**Notas e Moedas**

Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário.
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.

As notas consideradas são de 100, 50, 20, 10, 5, 2.
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
A seguir mostre a relação de notas necessárias.

**Entrada**
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

**Saída**
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

## Exemplos

Exemplo de Entrada = Exemplo de Saída

```bash
576.73 =
NOTAS:
5 nota(s) de R$ 100.00;
1 nota(s) de R$ 50.00;
1 nota(s) de R$ 20.00;
0 nota(s) de R$ 10.00;
1 nota(s) de R$ 5.00;
0 nota(s) de R$ 2.00;
MOEDAS:
1 moeda(s) de R$ 1.00;
1 moeda(s) de R$ 0.50;
0 moeda(s) de R$ 0.25;
2 moeda(s) de R$ 0.10;
0 moeda(s) de R$ 0.05;
3 moeda(s) de R$ 0.01;

4.00 =
NOTAS:
0 nota(s) de R$ 100.00;
0 nota(s) de R$ 50.00;
0 nota(s) de R$ 20.00;
0 nota(s) de R$ 10.00;
0 nota(s) de R$ 5.00;
2 nota(s) de R$ 2.00;
MOEDAS:
0 moeda(s) de R$ 1.00;
0 moeda(s) de R$ 0.50;
0 moeda(s) de R$ 0.25;
0 moeda(s) de R$ 0.10;
0 moeda(s) de R$ 0.05;
0 moeda(s) de R$ 0.01;

91.01 =
NOTAS:
0 nota(s) de R$ 100.00;
1 nota(s) de R$ 50.00;
2 nota(s) de R$ 20.00;
0 nota(s) de R$ 10.00;
0 nota(s) de R$ 5.00;
0 nota(s) de R$ 2.00;
MOEDAS:
1 moeda(s) de R$ 1.00;
0 moeda(s) de R$ 0.50;
0 moeda(s) de R$ 0.25;
0 moeda(s) de R$ 0.10;
0 moeda(s) de R$ 0.05;
1 moeda(s) de R$ 0.01;
```

## Referências

Exemplo de dojo realizado pela comunidade python de Blumenau em [20190129](https://github.com/pythonbnu/dojo/blob/master/2019_01_29/dojo.py)

[beecrowd | 1021](https://www.beecrowd.com.br/repository/UOJ_1021.html)
Por Neilor Tonin, URI  Brasil
