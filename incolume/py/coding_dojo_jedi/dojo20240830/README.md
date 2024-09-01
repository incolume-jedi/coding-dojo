# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

- _[Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)_

---

## Problema

**Fatoração pythônica**

Melhore o código a seguir:
```python 
#INSERINDO TEXTO
string=input("Digite a string no qual quer ler quais letras do alfabetos elas possui:\t")

#DICIONARIO do alfabetos
alfabetos={'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0,
'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

#PERCORRENDO A STRING (caractere por caractere)
for b in string:
    if ((b=='a') or (b=='A')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='b') or (b=='B')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='c') or (b=='C')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='d') or (b=='D')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='e') or (b=='E')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='f') or (b=='F')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='g') or (b=='G')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='g') or (b=='G')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='h') or (b=='H')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='i') or (b=='I')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='j') or (b=='J')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='k') or (b=='K')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='l') or (b=='L')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='m') or (b=='M')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='n') or (b=='N')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='o') or (b=='O')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='p') or (b=='P')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='q') or (b=='Q')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='r') or (b=='R')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='s') or (b=='S')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='t') or (b=='T')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='u') or (b=='U')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='v') or (b=='V')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='w') or (b=='W')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='x') or (b=='X')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='y') or (b=='Y')):
        alfabetos[b]=alfabetos[b]+1
    elif ((b=='z') or (b=='Z')):
        alfabetos[b]=alfabetos[b]+1

#VARIAVEL QUE CONTEM A CHAVES E CONTEUDO DO DICIONARIO
lista=list(alfabetos.items())

#PRINTANDO
print(lista)
```

## Exemplos

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

- [dojo](./dojo.py)
- [tests](./test_20240830.py)


## Referências

- https://pt.stackoverflow.com/q/313982
N/A - Referências para o dojo, o problema ou para elicidações extras.

---

Copyright &copy; **incolume.com.br** since 2010