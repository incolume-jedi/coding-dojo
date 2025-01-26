# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

- _[Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)_

---
![Python](https://img.shields.io/badge/Python-512BD4?style=flat&logo=python&logoColor=yellow)
![JEDI Incolume](https://img.shields.io/badge/incolume-JEDI-blue?style=flat)
![PyCharm](https://img.shields.io/badge/PyCharm-AABBCC?style=flat)
![VS Code](https://img.shields.io/badge/VScode-AABBCC?style=flat&logo=visualstudiocode&logoColor=white)
![VS Code](https://img.shields.io/badge/CodeSpace-AABBCC?style=flat&logo=visualstudiocode&logoColor=white)
---

## Problema

**Primos em Pi**

O número pi (π) é uma das mais famosas e mais facilmente reconhecidas constantes matemáticas. Originalmente definido como o resultado da divisão da circunferência de um círculo pelo seu diâmetro, π é um número irracional e a sua representação decimal é infinita e não se repete.

- Instruções 
Este desafio consiste em encontrar a sequência mais longa de números primos (entre 2 e 9973) no primeiro 1 milhão de casas decimais de π.

- Em detalhes:

Localize a sequência mais longa (em dígitos) de números primos nas casas decimais de π no arquivo fornecido (1 milhão de casas decimais).

Em caso de mais de uma sequência do mesmo tamanho, a sequência com o início mais próximo do ponto decimal deverá ser utilizada.

Apenas números primos entre 2 e 9973 deverão ser considerados na busca (basicamente, números primos contendo de um a quatro dígitos).

- Formato de saída 
Imprima uma linha contendo a maior sequência encontrada, sem espaços. Exemplo:

4159265358979323

- Validação 
Baixe o [arquivo de dados](https://osprogramadores.com/files/d11/pi-1M.tar.gz) ou via web no [pastebin](https://pastebin.com/raw/Ak8TCbJk).

Descompacte o arquivo localmente com tar zxvf pi-1M.tar.gz.

Rode o seu programa usando o arquivo de dados como entrada (pi-1M.txt)

Dica: (Linux) Use o comando “cut” para produzir arquivos menores e testar o seu programa. Por exemplo, para produzir um arquivo chamado pi-1k.txt com as primeiras 1000 casas decimais de π, use:

$ cut -c1-1001 <pi-1M.txt >pi-1k.txt

Onde 1001 representa o número de decimais desejadas + 1.

Quanto estiver razoavelmente satisfeito com os resultados, visite a [página de validação de desafios](https://osprogramadores.com/v). Escolha o número do desafio, digite o seu usuário no Github e cole a sua solução.

Se tudo estiver OK, a página de validação emitirá um token. Crie um arquivo texto chamado .valid no diretório da sua solução contendo o token na primeira linha. Adicione esse arquivo ao commit com a solução e envie o PR.

Ao enviar o PR, clique na página do PR e verifique se todos os testes passaram. Clique no link Details na página do teste em caso de falha.

## Exemplos

Considere π com 20 decimais:

3.14159265358979323846
Neste caso, a maior sequência de números primos seria:

41 59 2 653 5 89 7 9323
Que resulta na sequência:

4159265358979323


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
- [tests](test_20250104.py)



## Referências

- https://osprogramadores.com/desafios/d11/
- https://github.com/osprogramadores/op-desafios/blob/master/desafio-11%2Fimalisoon%2Fpython%2Fmain.py


N/A - Referências para o dojo, o problema ou para elicidações extras.

---

Copyright &copy; **incolume.com.br** since 2010