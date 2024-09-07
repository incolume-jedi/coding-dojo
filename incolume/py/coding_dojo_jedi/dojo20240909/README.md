# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

- _[Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)_

---

## Problema

**Cifra de César**

Um esquema de codificação de textos usado há mais de 2000 anos é a chamada Cifra de César. Esse esquema de codificação era utilizado pelo imperador romano para se comunicar com seus generais. O esquema de codificação funciona da seguinte forma.

Numa primeira etapa, substitua as ocorrências de brancos e sinais de pontuação por uma seqüência de caracteres seguindo a seguinte tabela:

Tabela 1
Símbolo¦código 
--------¦---------
(branco)¦WBRW
,¦WVRW
.¦WPTW
;¦WPVW
:¦WDPW
!¦WEXW
?¦WINW
-¦WHFW


Depois de feita essa substituição o texto terá apenas letras do alfabeto. Então, dado um natural k substitua cada letra i pela (i+k)-ésima letra do alfabeto (após a última letra letra segue-se a primeira novamente). Observe o exemplo a seguir:

Texto original:

ESSE EXERCICIO-PROGRAMA VAI SER MUITO LEGAL.

Após substituir-se os brancos e sinais de pontuação:

ESSEWBRWEXERCICIOWHFWPROGRAMAWBRWVAIWBRWSERWBRWMUITOWBRWLEGALWPTW

Então, usando-se k = 2, obtemos o seguinte texto codificado:

GUUGYDTYGZGTEKEKQYJHYRTQITCOCYDTYXCKYDTYUGTYDTYOWKVQYDTYNGICNYRVY

Está função deve ser implementada, é intermediária e executada tanto na cifra quanto na decifra.

prepara_frase("FACIL? - SIMPLES!")=="FACILWINWWBRWWHFWWBRWSIMPLESWEXW".

prepara_frase("FACILWINWWBRWWHFWWBRWSIMPLESWEXW")=="FACIL? - SIMPLES!"


cifra(frase: str, k:int)

decifra(frase:str, k:int)


## Exemplos

- 'a ligeira raposa marrom saltou sobre o cachorro cansado'

- GUUGYDTYGZGTEKEKQYDTYGYDTYNGICNYGZY

- VJNSINZJKNSINVZENSINKVOKNSINZENSINUVLKJTYNGKNNSINVJNSINNRVIVNSINQLNSINVZEWRTYNMIN
NSINNVEENSINUVINSINKVOKNSINZENSINGFIKLXZVJZJTYNSINXVJTYIZVSVENSINNFIUVENSINNRVIVN
GKNNSINZTYNSINNVZJJNGKNNSINZTYNSINNVZJJNMINNSINVJNSINZJKNSINEZTYKNSINWRZINGKNNSIN
YVIQCZTYVENSINXCLVTBNLVEJTYVENSINQLDNSINXVNZEEVINVONNVONNVON

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
- [tests](test_20240909.py)


## Referências

- https://www.ime.usp.br/~ronaldo/mac115/ig98/eps/ep3/ep3.html
- https://gist.githubusercontent.com/ustropo/4aead578401fe57166a9ce1d45375696/raw/b81dd00c74ccaecd252678ea1353c7ef402a6866/caesar_cypher.py

N/A - Referências para o dojo, o problema ou para elicidações extras.

---

Copyright &copy; **incolume.com.br** since 2010