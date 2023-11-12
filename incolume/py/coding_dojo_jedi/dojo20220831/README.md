# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

---

## Problema

**Calculo de Conceito**

Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.

A atribuição de conceitos obedece à tabela abaixo:

| Média de Aproveitamento  |Conceito|
|----|---|
|  Entre 9.0 e 10.0        |A|
|  Entre 7.5 e 9.0         |B|
|  Entre 6.0 e 7.5         |C|
|  Entre 4.0 e 6.0         |D|
|  Entre 4.0 e zero        |E|

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

Desafio: Não utilizar if.

## Exemplos

```
conceito(10, 10) == 'Média 10, "A", APROVADO'
conceito(1, 1) == 'Média 1, "E", REPROVADO'
conceito(10, 5) == 'Média 7.5, "B", APROVADO'
conceito(9, 5) == 'Média 7, "C", APROVADO'
conceito(6, 4) == 'Média 5, "D", REPROVADO'
```

## Artefatos

- [dojo](./dojo20220831.py)
- [tests](./test_20220831.py)

## Referências

Estrutura de decisão nº 14
