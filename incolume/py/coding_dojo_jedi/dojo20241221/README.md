# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

- _[Seja membro da Guilda JEDI Incolume](https://discord.gg/eBNamXVtBW)_

---

## Problema

**Sum of Subarray Minimums**

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 10**9 + 7.

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


### Example 1:

Input: arr = [3,1,2,4]

Output: 17

#### Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].

Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.

Sum is 17.

### Example 2:

Input: arr = [11,81,94,43,3]
Output: 444

## Constraints:
1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 3 * 10^4


## Artefatos

- [dojo](__init__.py)
- [tests](test_20241221.py)

## Referências

N/A - Referências para o dojo, o problema ou para elicidações extras.
---

Copyright &copy; **incolume.com.br** since 2010
