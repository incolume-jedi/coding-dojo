# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

---

## Problema

**Exercícios do [Workshop python iniciante](https://github.com/incolume-jedi/workshop-python-iniciante/blob/master/exercicio/README.md)**

### Exercício

```Obs: Atividade excedeu o tempo disponível, e foi fracionada para este dojo.```

[...  exercícios Anteriores ...](/coding_dojo_jedi/20220721/README.md)

**5. Crie uma aplicação que procura os dados de um personagem**

* Crie um arquivo `main.py` e outro `star_wars.py`
* O arquivo `main.py` só deve ter a lógica de entrada e exibição de dados
* O arquivo `star_wars.py` vai ter a lógica de comunicação com o _SWAPI_
* Receba um parâmetro `nome` no `main.py` e imprima as seguintes informações:
`name`, `height`, `birth_year` e a _quantidade de filmes que ele aparece_.

``` python
exemplo

python main.py --nome "Luke Skywalker"
* Nome: Luke Skywalker
* Altura: 172cm
* Ano de nascimento: 19BBY
* Quantidade de filmes: 5

python main.py --nome "Meu nome"
* Personagem "Meu nome" não encontrado

```

_dicas_:
* Uma requisição para `https://swapi.dev/api/people/` retorna todos os personagens
    * O resultado é paginado de 10 em 10 personagens
    * Portanto, se não encontrar na página atual, tem que seguir para a página no atributo `next`
* A comparação dos nomes deve ser _case insensitive_, ou seja, `luke skywalker == LUKE SKYWALKER`


``` Obs: Atividade excedeu o tempo disponível, e foi fracionada para o proximo dojo. ```

[... Continuação dos exercícios ...](/coding_dojo_jedi/20220723/README.md)

## Referências

- https://github.com/incolume-jedi/workshop-python-iniciante/blob/master/exercicio/README.md
