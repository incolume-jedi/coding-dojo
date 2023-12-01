# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

---

## Problema

**Remove anchor from URL**

Implemente uma função/timemstamp que retorne uma URL com qualquer conteúdo após cerquilha (#) removido.

## Exemplos

"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"

  (remove_url_anchor("www.codewars.com#about"), "www.codewars.com")
  (remove_url_anchor("www.codewars.com/katas/?page=1#about"), "www.codewars.com/katas/?page=1")
  (remove_url_anchor("www.codewars.com/katas/"), "www.codewars.com/katas/")

## Artefatos
- [dojo](dojo.py)
- [tests](test_20231109.py)

## Referências

https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/python
