# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

- _[Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)_

---

## Problema

**Solucionador de Sudoku**

Escreva um programa para resolver um quebra-cabeça Sudoku preenchendo as células vazias.

Uma solução de sudoku deve satisfazer todas as seguintes regras :

1. Cada um dos dígitos 1-9, deve ocorrer exatamente uma vez em cada linha.
1. Cada um dos dígitos 1-9, deve ocorrer exatamente uma vez em cada coluna.
1. Cada um dos dígitos 1-9, deve ocorrer exatamente uma vez em cada uma dos 9 quadrantes 3x3 da grade.

O '.' caractere indica células vazias.


## Exemplos

Exemplo 1:


Entrada: placa = [["5","3",".",".","7",".",".",".",["6",". ",".","1","9","5",".",".","."],[".","9","8",".",". ",".",".","6","."],["8",".",".","6",".",". ","3"],["4",".",".","8",".","3",".","1"],["7", ".",".",".","2",".",".","6"],[".","6",".",".", ".",".","2","8","."],[".",".","4","1","9",".", ".","5"],[".",".",".",".","8",".",".","7","9"]]
 Saída: [ ["5","3","4","6","7","8","9","1","2"],["6","7","2" ,"1","9","5","3","4","8"],["1","9","8","3","4","2" ,"5","6","7"],["8","5","9","7","6","1","4","2","3" ],["4","2","6","8","5","3","7","9","1"],["7","1"," 3","9","2","4","8","5","6"],["9","6","1","5","3"," 7","2","8","4"],["2","8","7","4","1","9","6","3"," 5"],["3","4","5","2","8","6","1","7","9"]]

 Explicação:  

A placa de entrada é mostrada acima e a única solução válida é mostrada abaixo:


![Solução válida](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png "Soduku")


Restrições:

- board.length == 9
- board[i].length == 9
- board[i][j]é um dígito ou '.'.

É garantido que a placa de entrada possui apenas uma solução.


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

- [dojo](__init__.py)
- [tests](test_20241212.py)


## Referências

- [Solucionador de Sudoku](https://leetcode.com/problems/sudoku-solver/)

N/A - Referências para o dojo, o problema ou para elicidações extras.

---

Copyright &copy; **incolume.com.br** since 2010