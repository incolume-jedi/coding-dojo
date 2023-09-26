# coding-dojo

Aqui é mantido um repositório com as soluções que trabalhamos no [dojo de codificação da Guilda Jedi no discord](https://discord.gg/qA8CBQHSbK)


Os códigos estão organizados em diretórios, sendo que cada diretório representa um dia do dojo, formado por `incolume/py/YYYYMMDD`, de forma que o primeiro dojo estará no topo, e o ultimo na base.

Os códigos são em python 3.8+ e tem como dependência principal o pytest. Mas para facilitar a instalação o `poetry` foi escolhido para controle de dependências, apenas execute `pip install poetry && poetry install` na raiz do diretório, no mesmo nível do arquivo pyproject.toml`

Finalmente, para rodar os testes nos códigos, mude para o diretório do Dojo, por exemplo 20220701, e digite `pytest .` ou no diretório principal digite `pytest incolume/py/20220701`.

[Mais detalhes sobre os coding-dojo](/docs/README.md)

## O que é?

A ideia de um Coding Dojo é treinar a resolução de problemas, desenvolvimento orientado a testes (TDD), programação em par, comunicação com outras pessoas e uma linguagem de programação através de exercícios práticos.

Para mais informações sobre os nossos coding dojos anteriores acesse os respectivos diretórios dos dojos e leia o REAME.md.

## Alguns detalhes

Não é competivivo, mas sim colaborativo. Vamos nos juntar para resolver o problema.

Todos os níveis são bem-vindos.

Somos encorajados a tentar novas ideias, sair da caixa. A ideia é treinar

## Quem pode participar?

Todos são convidados a participar, não existe nível inicial, a ideia é aprender com a troca de ideias e experiências.

Se você não se sentir confortável em participar programando, está convidado a participar como um membro da platéia para ver a mecânica do coding dojo e poder programar no futuro. Portanto, mesmo que você não conheça python, pode vir para aprender conceitos da linguagem.

## Como conduzir?

### Gerenciamento do tempo

- Não exceder o tempo máximo de 120' (2h);
- Finalizar o dojo entre 100' e 120';
- Com o problema finalizado o dojo pode ser encerrado a qualquer momento;
- Se o tempo for insuficiente para solução do problema proposto, fracione-o em etapas,
finalize a primeira etapa, encerre o dojo, e continue a etapa seguinte no proximo dojo;

### Uma descrição de como conduzir o dojo (no maximo 2h):

- 10 minutos para montar a estrutura e apresentar/discutir alguns problemas que podemos resolver (3 problemas é suficiente);
- 5 minutos para decidir sobre qual problema vamos resolver;
- 10 minutos para uma revisão de python (opcional);
- 40 minutos de programação;
- 5 minutos intervalo para ver o andamento da solução;
- 40 minutos de programação;
- 10 minutos de revisão sobre o que aprendemos e o que podemos melhorar no próximo dojo;

### Sobre o período de programação

- Um programador pilota;
- Um programador co-pilota;
- A platéia assite e dá dicas (importante: a platéia só pode se manifestar se os testes estiverem ok, caso contrário, apenas piloto e co-piloto);
- Após cinco minutos trocam as posições: piloto -> co-piloto, co-piloto -> platéia, platéia -> piloto;
- A ideia é que todos tenham uma chance de programar ao menos uma vez;
- Toda a comunicação entre o piloto e copiloto deve ser em voz alta para que todos escutem;

### Salvaguarda do aprendizado

- Sempre salve as soluções no fork do dojo;
- Solicite um pull request para consolidação;
