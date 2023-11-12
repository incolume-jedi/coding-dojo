# keep a changelog

## O que é um changelog?
Um changelog é um arquivo que contém uma lista selecionada, ordenada cronologicamente, de mudanças significativas para cada versão de um projeto.

## Por que manter um changelog?
Para facilitar que usuários e contribuidores vejam precisamente quais mudanças significativas foram realizadas entre cada versão publicada de um projeto.

## Quem precisa de um changelog?
Pessoas precisam. Seja consumidores ou desenvolvedores, os usuários finais de softwares são seres humanos que se preocupam com o que está no software. Quando o software muda, as pessoas querem saber por que e como.

## Como fazer um bom changelog?
### Princípios fundamentais
- Changelogs são para humanos, não máquinas.
- Deve haver uma entrada para cada versão.
- Alterações do mesmo tipo devem ser agrupadas.
- Versões e seções devem ser vinculáveis (com links).
- A versão mais recente vem em primeiro lugar.
- A data de lançamento de cada versão é exibida.
- Mencione se você segue o [versionamento semântico](https://semver.org/).


### Tipos de mudanças
- **Added**: (Adicionado) para novos recursos.
- **Changed**: (Modificado) para alterações em recursos existentes.
- **Deprecated**: (Obsoleto) para recursos que serão removidos nas próximas versões.
- **Removed**: (Removido) para recursos removidos nesta versão.
- **Fixed**: (Corrigido) para qualquer correção de bug.
- **Security**: (Segurança) em caso de vulnerabilidades.

## Como aplicar changelog neste projeto?
   Este projeto utiliza o pacote python incolumepy.utils, que possui a
   prerrogativa de criar um `CHANGELOG.md` automaticamente a partir das
entradas do `git tag -n`.

Exemplos:
```shell
git tag -f Unreleased -m 'added: Adicionado orientações sobre Keep a CHANGELOG.md em docs/user_guide/keep-a-chagelog.md'
git tag -f `poetry version -s` -m 'added: Adicionado orientações sobre Keep a CHANGELOG.md em docs/user_guide/keep-a-chagelog.md'
git tag -f 1.0.0 -m 'Added: (Adicionado) para novos recursos;
Changed: (Modificado) para alterações em recursos existentes;
Deprecated: (Obsoleto) para recursos que serão removidos nas próximas versões;
Removed: (Removido) para recursos removidos nesta versão;
Fixed: (Corrigido) para qualquer correção de bug;
Security: (Segurança) em caso de vulnerabilidades;'
```

### Atualizar o CHANGELOG.md
```shell
task gcl
```

## Referência
- https://keepachangelog.com/pt-BR/1.0.0/
