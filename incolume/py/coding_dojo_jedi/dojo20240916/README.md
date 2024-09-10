# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

- _[Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)_

---

## Problema

**DAC Virtual**


Em eletrônica, um conversor digital-analógico (DAC, D/A ou D-to-A) é um sistema que converte uma representação binária desse sinal em uma saída analógica. Um conversor de 8 bits pode representar um máximo de 2^8 valores diferentes, com cada valor sucessivo diferindo em 1/256 do valor da escala completa, isso se torna a resolução do sistema.

Criar uma função que leva uma representação numérica decimal de um sinal e retorna o nível de tensão analógica que seria criado por um DAC se fosse dado o mesmo número em binário.

Enquanto a faixa de valor é 0-1023, a faixa de referência é 0-5,00 volts. Valor e referência são diretamente proporcionais.

Este DAC tem 10 Bits de resolução e a referência DAC é definida em 5,00 volts.



## Exemplos

V_DAC(0) ➞ 0

V_DAC(1023) ➞ 5

V_DAC(400) ➞ 1.96


    Notas: Você deve retornar seu valor arredondado para duas casas decimais.


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
- [tests](test_20240916.py)



## Referências

- https://edabit.com/challenge/AJGqpNL2yAyhbdpvB
N/A - Referências para o dojo, o problema ou para elicidações extras.

---

Copyright &copy; **incolume.com.br** since 2010