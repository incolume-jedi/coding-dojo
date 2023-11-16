# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

---

## Problema

**milissegundos**

Apresentar um horário com horas (h), minutos (m) e segundos (s) desde a meia-noite.
A tarefa é escrever uma função que retorna o tempo desde a meia-noite em milissegundos.


Constantes de entrada:

* 0 <= h <= 23
* 0 <= m <= 59
* 0 <= s <= 59

> Obs: Dentre as possíveis soluções aplique: *functools.singledispatch* e *typing.overload*


## Exemplos

```python
h = 0
m = 1
s = 1

milissegundos(h, m, s) == 61000
milissegundos(datetime(h, m, s)) == 61000
milissegundos(time(h, m, s)) == 61000

```

## Referências
- https://docs.python.org/3/library/functools.html
- [Issue#10](https://github.com/incolume-jedi/coding-dojo/issues/10)
