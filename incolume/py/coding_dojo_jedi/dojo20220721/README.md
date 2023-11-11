# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

---

## Problema

**Exercícios do [Workshop python iniciante](https://github.com/incolume-jedi/workshop-python-iniciante/blob/master/exercicio/README.md)**

### Exercício

Nesse exercício vamos praticar alguns conceitos sobre o ambiente e a linguagem Python.

Para a prática, vamos usar a _SWAPI_ (`https://swapi.dev/`) ou _The Star Wars API_.
A ideia é que vamos fazer requisições para essa API e mostrar alguns resultados na tela.
Sem mais, vamos as atividades.

**1. Criar um diretório para o projeto (se quiser, pode iniciar um repositório git)**

**2. Crie e inicie um ambiente virtual**

Aqui você pode iniciar um ambiente virtual que desejar: `venv`, `pipenv`, `conda`, `poetry`.

**3. Instale a biblioteca `requests` no ambiente virtual**

Para instalar um pacote você usa `pip install <pacote>`

**4. Faça uma requisição de teste**

* Crie um arquivo `teste.py`
* Importe a biblioteca `requests`
* Importe a biblioteca `json` (padrão do python)
* Faça uma requisição para `https://swapi.dev/api/people/1/` usando `requests.get`
* Converta o conteúdo _JSON_ da requisição em um `dict` utilizando a biblioteca `json`
* Imprima `Hello, <name>!` no _console_
* Execute `python teste.py`
* Deve imprimir `Hello, Luke Skywalker!`

_obs_: ao invés de usar a biblioteca padrão do python para obter o _JSON_, poderíamos
usar o método `r.json()` disponível na requisição da biblioteca `requests`.

``` Obs: Atividade excedeu o tempo disponível, e foi fracionada para o proximo dojo. ```

[... Continuação dos exercícios ...](/coding_dojo_jedi/20220722/README.md)

## Artefatos
- [dojo](./dojo20220721.py)
- [tests](./test_20220721.py)


## Referências

- https://github.com/incolume-jedi/workshop-python-iniciante/blob/master/exercicio/README.md
