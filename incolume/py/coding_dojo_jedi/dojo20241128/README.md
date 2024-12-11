# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

- _[Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)_

---

## Problema

**Sudoku válido**

Determine se um  9 x 9tabuleiro de Sudoku é válido. Apenas as células preenchidas precisam ser validadas  de acordo com as seguintes regras :

1. Cada linha deve conter os dígitos  1-9 sem repetição.
1. Cada coluna deve conter os dígitos  1-9 sem repetição.
1. Cada uma das nove  3 x 3 subcaixas da grelha deve conter os dígitos  1-9 sem repetição.


Observação:

- Um tabuleiro de Sudoku (parcialmente preenchido) pode ser válido, mas não é necessariamente solucionável.
- Apenas as células preenchidas precisam ser validadas de acordo com as regras mencionadas.


## Exemplos

Entrada: 
```
Exemplo 1:

placa =
[["5","3",".",".","7",".",".",".","]
,["6",".",".","1","9","5",".",".","]
,[".","9","8",".",".",".","6","."]
,["8",".",".",".","6",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".","6"]
,[".","6",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".","7","9"]]
```
Saída: verdadeiro

Exemplo 2:

Entrada: 
```
placa =
[["8","3",".",".","7",".",".",".","]
,["6",".",".","1","9","5",".",".","]
,[".","9","8",".",".",".","6","."]
,["8",".",".",".","6",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".","6"]
,[".","6",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".","7","9"]]
```
Saída: false

 Explicação: 

    Igual ao Exemplo 1, exceto com o 5 no canto superior esquerdo sendo modificado para 8 . Como há dois 8 na subcaixa 3x3 superior esquerda, é inválido.
 

Restrições:
-      
    class Solution:
        def isValidSudoku(self, board: List[List[str]]) -> bool:

- board.length == 9
- board[i].length == 9
- board[i][j]é um dígito 1-9 ou '.'


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
- [tests](test_20241128.py)


## Referências
- [Sudoku válido](https://leetcode.com/problems/valid-sudoku/)
N/A - Referências para o dojo, o problema ou para elicidações extras.

---

Copyright &copy; **incolume.com.br** since 2010