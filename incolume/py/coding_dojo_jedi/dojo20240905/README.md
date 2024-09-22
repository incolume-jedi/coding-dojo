# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

- _[Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)_

---

## Problema

**Luhn algorithm**

O Algoritmo luhn ou Fórmula de luhn, também conhecido como "módulo 10" ou "mod 10" algoritmo, nomeado após seu criador, IBM cientista Hans Peter Luhn, é simples verificar o dígito fórmula usada para validar uma variedade de números de identificação.

É descrito nos EUA. Patente No. 2.950.048, concedida em 23 de agosto de 1960.[1]

O algoritmo está no domínio público e está em uso amplo hoje. É especificado em ISO/IEC 7812-1.[2] Não se pretende que seja um função hash criptograficamente segura; ele foi projetado para proteger contra erros acidentais, não ataques maliciosos. A maioria dos cartões de crédito e muitos números de identificação do governo usam o algoritmo como um método simples de distinguir números válidos de números incorretos ou digitados incorretamente.

O dígito de verificação é calculado da seguinte forma:

Se o número já contiver o dígito de verificação, solte esse dígito para formar a "carga útil". O dígito de verificação é na maioria das vezes o último dígito.

Com a carga útil, comece do dígito mais à direita. Movendo-se para a esquerda, dobre o valor de cada segundo dígito (incluindo o dígito mais à direita).

Soma os valores dos dígitos resultantes.

O dígito de verificação é calculado por (10−(𝑠mod10))mod10￼, onde s é a soma do passo 3. Este é o menor número (possivelmente zero) que deve ser adicionado 𝑠￼para fazer um múltiplo de 10. Outras fórmulas válidas que dão o mesmo valor são 9−((𝑠+9)mod10)￼, (10−𝑠)mod10￼, e 10⌈𝑠/10⌉−𝑠￼. Note que a fórmula (10−𝑠)mod10￼ não funcionará em todos os ambientes devido a diferenças na forma como os números negativos são tratados pelo módulo operação.

Exemplo para calcular o dígito de verificaçãoeditar

Suponha um exemplo de um número de conta 1789372997 (apenas a "carga útil", dígito de verificação ainda não incluído):

7992739871Multiplicadores2121212121==========149182143188141Sumário de dígitos5 (1+4)99 (1+8)25 (1+4)39 (1+8)85 (1+4)1

A soma dos dígitos resultantes é 56.

O dígito de verificação é igual a (10−(56mod≈10))=4￼.

Isso faz com que o número da conta completa leia 17893729974.

Exemplo para validar o dígito de verificaçãoeditar

Solte o dígito de verificação (último dígito) do número para validar. (por exemplo. 17893729974 → 1789372997)

Calcule o dígito de verificação (veja acima)

Compare o resultado com o dígito de verificação original. Se ambos os números coincidirem, o resultado é válido. (por exemplo (givenCheckDigit = calculatedCheckDigit) ⇔ (isValidCheckDigit)).




```python 
# Python3 program to implement

# Luhn algorithm

 

# Returns true if given card

# number is valid

def checkLuhn(cardNo):

     

    nDigits = len(cardNo)

    nSum = 0

    isSecond = False

     

    for i in range(nDigits - 1, -1, -1):

        d = ord(cardNo[i]) - ord('0')

     

        if (isSecond == True):

            d = d * 2

  

        # We add two digits to handle

        # cases that make two digits after

        # doubling

        nSum += d // 10

        nSum += d % 10

  

        isSecond = not isSecond

     

    if (nSum % 10 == 0):

        return True

    else:

        return False

 

# Driver code   

if __name__=="__main__":

     

    cardNo = "79927398713"

     

    if (checkLuhn(cardNo)):

        print("This is a valid card")

    else:

        print("This is not a valid card")

 

# This code is contributed by rutvik_56


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
- [tests](test_20240905.py)


## Referências

N/A - Referências para o dojo, o problema ou para elicidações extras.

---

Copyright &copy; **incolume.com.br** since 2010