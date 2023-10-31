# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

---

## Problema

**Exercícios do [Workshop python iniciante](https://github.com/incolume-jedi/workshop-python-iniciante/blob/master/exercicio/README.md)**

### Exercício

[...  exercícios 1 a 4 ...](/coding_dojo_jedi/20220721/README.md)

[...  exercício 5 ...](/coding_dojo_jedi/20220722/README.md)

[...  exercício 6 ...](/coding_dojo_jedi/20220725/README.md)

**7. Se não encontrar pelo termo pesquisado, de sugestões**

Quando recebemos entradas no formato `python main.py --nome "Skywalker"`, pode ser que
ocorra um erro de digitação, por exemplo `python main.py --nome "Skywaler"`.
Nesse caso, seria interessante mostrar para o usuário uma mensagem do tipo
_Nenhum personagem "Skywaler" encontrado, mas encontrei: "Luke Skywalker", "Anakin Skywalker"_.

Para resolver esse problema, podemos usar a biblioteca [`fuzzywuzzy`](https://github.com/seatgeek/fuzzywuzzy).
Basta instalar a biblioteca e comparar as strings com
`fuzz.partial_ratio('skywaler', 'Luke Skywalker')`.
Essa função retorna um "grau de confiança" entre 0 e 100.
Portanto, podemos assumir que, se houve comparação perfeita ou parcial (partes 5 e 6), você pode sugerir os nomes que tenham um grau de confiança maior que 75.

``` python
exemplo

python main.py --nome "skywaler"
Nenhum personagem "Skywaler" encontrado, mas encontrei: "Luke Skywalker", "Anakin Skywalker"

# nesse exemplo, não encontrou nenhum personagem com nome "skywaler"
# mas ao calcular fuzz.partial_ratio('skywaler', 'Luke Skywalker')
# temos um grau de confiança de 88, logo pode ser que o usuário quis dizer "Luke Skywalker"
# ao invés de "skywaler"
# o mesmo acontece com fuzz.partial_ratio('skywaler', 'Anakin Skywalker')
```

[... Continuação dos exercícios ...](/coding_dojo_jedi/20220727/README.md)

## Artefatos
- [main2](./main2.py)
- [star wars2](./star_wars2.py)
- [test](./test_20220717.py)


## Referências

- https://github.com/incolume-jedi/workshop-python-iniciante/blob/master/exercicio/README.md
