# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

- _[Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)_

---

## Problema

**Fatorar código para POO**

Transforme o conteúdo da implementação [ROT13](https://gist.githubusercontent.com/ustropo/4aead578401fe57166a9ce1d45375696/raw/b81dd00c74ccaecd252678ea1353c7ef402a6866/caesar_cypher.py), em orientado a objetos.

```python
MODE_ENCRYPT = 1
MODE_DECRYPT = 0

def caesar(data, key, mode):
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
    return new_data

# Tests
key = 5
original = 'a ligeira raposa marrom saltou sobre o cachorro cansado'
print('  Original:', original)
ciphered = caesar(original, key, MODE_ENCRYPT)
print('Encriptada:', ciphered)
plain = caesar(ciphered, key, MODE_DECRYPT)
print('Decriptada:', plain)
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

- [dojo](__init__.py)
- [tests](test_20240910.py)


## Referências

- https://medium.com/vacatronics/cifra-de-c%C3%A9sar-em-python-8d02d3bc7d42
- https://gist.githubusercontent.com/ustropo/4aead578401fe57166a9ce1d45375696/raw/b81dd00c74ccaecd252678ea1353c7ef402a6866/caesar_cypher.py

N/A - Referências para o dojo, o problema ou para elicidações extras.

---

Copyright &copy; **incolume.com.br** since 2010