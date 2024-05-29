# CHANGELOG


All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and [Conventional Commit](https://www.conventionalcommits.org/pt-br/v1.0.0/).

This file was automatically generated for [incolume.py.changelog](https://github.com/development-incolume/incolume.py.changelog/-/tree/0.8.0)

---


## [1.51.0]	 &#8212; 	2024-05-29:
### Added
  - Dojo 20240527 primos de 4 algarismos;
  - Dojo20240526 - Menor palindromo primo de 2 algarismos;
  - Dojo20240525 - soma de algarismos absolutos;
  - Dojo20240524 - playlist;
  - Dojo20240523 análise de notas;
  - Dojo20240522 Número Palindromo;
  - Implementado mock para testes em SWAPI dojo20220722;
  - Implementado mock para testes em SWAPI dojo 20220530;
  - Implementado mock para testes em SWAPI dojo20220725;
  - Implementado mock para testes em SWAPI dojo20220727;
### Changed
  - Otimizado execução de rotinas CI/CD;
  - Atualização do modelo para abertura de dojos;

## [1.50.0]	 &#8212; 	2024-05-23:
### Deprecated
  - Blue;
  - Isort;
  - Pydocstyle;
  - Pylint;
### Added
  - Dojo20240513 - Raspagem de dados;
  - Dojo20240514 - popular SGBD SQLite;
  - Dojo20240515 - API Translate DEEPL;
  - Adicionado pacote html5lib;
  - Adicionado pacote openpyxl;
  - Adicionado pacote httpx;
  - Adicionado pacote deepl;
  - Acrescentado variável para token deepl no ambiente github;
  - Dojo20240516 - two sum;
  - Dojo20240517 - identificar-números-primos;
  - Dojo20240517 - solução Gerador de números primos;
  - Dojo20240517 - Mesclando matrizes de inteiros ordenadas - sem duplicatas;
  - Dojo20240518 - Romeu e Julieta (FizzBuzz);
  - Dojo20240519 - Convert Age to Days;
  - Dojo20240520 - Rot13;
  - Dojo20240521 - Média de temperatura;
### Changed
  - Acrescentado em desafios: https://osprogramadores.com/desafios/;

## [1.49.0]	 &#8212; 	2024-05-14:
### Added
  - Dojo20240504 - Criar dígitos verificadores para CPF;
  - Dojo20240505 - Validação de CPF (POO);
  - Dojo20240506 - Número Feliz;
  - Dojo 20240507 - Todos Números felizes menores que 100;
  - Dojo 20040507 - Quais são os primeiros 25 números felizes?;
  - Dojo 20240508 - Quais são os dois menores números felizes consecutivos?;
  - Dojo 20240508 - Quais são os três menores números felizes consecutivos?;
  - Dojo 20240508 - Quais as alturas dos números felizes 7, 13, 19, 68 e 97?;
  - Dojo 20240509 - (POO) Romanos > Arábicos / Arábicos > Romanos;
  - Dojo 20240510 - Posição das letras;
  - Dojo 20240510 - Número narcisista;
  - Date 20240510 - Counting sheep;
### Fixed
  - Corrigido encode quebrado no Windows para arquivos markdown;
  - Corrigido geração do sumário de dojos;
  - Corrigido conflito entre ruff e isort;
  - Corrigido erro de sintaxe em string literais;

## [1.48.1]	 &#8212; 	2024-05-05:
### Fixed
  - Correção no README dojo 20240503;

## [1.48.0]	 &#8212; 	2024-05-05:
### Added
  - Dojo20240317 - Eu sou o perímetro;
  - Dojo 20240317 - quantidade de latas;
  - Dojo 20240502 - validação de cpf;
  - Dojo 20240503 - criar cpf validos;
  - Pacote pre-commit;
### Changed
  - Incolumepy.utils > incolume.py.changelog;
### Fixed
  - Correções CI/CD;
  - Configuração pytest;
  - Configuração ruff;

## [1.47.0]	 &#8212; 	2024-04-30:
### Added
  - Dojo20240317 - Eu sou o perímetro;
  - Pacote pre-commit;
### Changed
  - Incolumepy.utils > incolume.py.changelog;

## [1.46.0]	 &#8212; 	2023-12-01:
### Added
  - Dojo20231130 — boyer-moore (algoritmo de busca);
  - Dojo20231129 - Perímetro terrestre (Lógica de localizar padrão vizinho);
  - Dojo20231128 — Mock API;
  - Dojo20231127 — Get Planet name by id (condicional sem if);
  - Dojo20231115 — milissegundos (sobrecarga de função);
  - Dojo20231113 — Notas e Moedas POO;
  - Adicionado orientações sobre Keep a CHANGELOG.md em docs/user_guide/keep-a-chagelog.md;
  - Adicionado Orientações sobre versionamento semântico docs/user_guide/semver.md;
### Changed
  - Menu da documentação atualizado com keep-a-changelog;
  - Atualizado o layout coding challenge com arrow-up em SVG;
### Fixed
  - Melhoria no feedback de erro para os elementos de Artefatos no arquivo README.md dos dojos;

## [1.45.0]	 &#8212; 	2023-11-11:
### Added
  - Aplicado QA em CI/CD;
  - Dojo20231109 — Remove anchor from URL;
  - Dojo20231030 — Inteiro Reverso;
  - Dojo20231030 — Exercitando TDD;
  - Teste de compatibilidade com python 3.12;
  - Sumário de dojos resolvidos;
### Changed
  - Elementos visuais e estruturais de documentação atualizados com suite MKDocs.;
  - Correção nas mensagens de changelog para release 1.44.0;
  - Acrescentado condicional em testes unitários para Python 3.10+ a partir de dojos resolvidos no ano 2023;
  - Lint style **ruff** aplicado a 90% do código;
  - Acrescentado sessão Artefatos ao README de dojo contendo os arquivos de implementação e de testes;
  - CI/CD plenamente funcional;
  - Scripts automatizados para geração de sumário;
  - Script automatizado para atualização de sumário;
### Fixed
  - Erros de encoding em Windows;
  - Recuperado Dojo20220730 — Workshop python iniciante exercício 8;
  - Corrigido falso/positivo na leitura dos arquivo de montagem automática do sumário;

## [1.44.0]	 &#8212; 	2023-10-30:
### Added
  - Pacote markdown;
  - Redefinição do template para dojos;
  - Redefinição de template para issues;
  - Solução do Dojo20231016 — Números Romanos para Arábicos;
  - Solução do Dojo20231019 — Contando nucleotídeos de DNA;
  - Solução do Dojo20231019 — Complementando uma fita de DNA;
  - Solução do Dojo20231025 — Índice de dojos resolvidos;
### Changed
  - Elementos visuais e estruturais de documentação atualizados com suite MKDocs.;
  - Ampliação de cobertura para ruff;
  - Atualização da documentação;
### Fixed
  - Ruff:FA102 Missing from __future__ import annotations, but uses PEP 604 union;
  - Skip testes para windows devido ao não reconhecimento de encode do OS.;

## [1.40.1]	 &#8212; 	2023-10-10:
### Added
  - Solução dojo 2023-10-07 Subarray de soma máxima.;

## [1.40.0]	 &#8212; 	2023-10-10:
### Changed
  - Documentação atualizada, nova configuração e aplicado template diferenciado;

## [1.39.0]	 &#8212; 	2023-10-08:
### Added
  - Adicionado scripts RPA para MKDocs;
### Changed
  - Ampliado repertório de sites coding dojo;
  - Ampliado verificação lint com ferramenta ruff;
  - Configurado MKDocs;
  - Cobertura completa *ruff* para tests/ e incolume.py.coding_dojo_jedi.utils;
  - Cobertura completa *pylint* para tests/ e incolume.py.coding_dojo_jedi.utils;
  - Cobertura completa *blue* para tests/ e incolume.py.coding_dojo_jedi.utils;
  - Cobertura completa *isort* para tests/ e incolume.py.coding_dojo_jedi.utils;
  - Cobertura completa *pydocstyle* para tests/ e incolume.py.coding_dojo_jedi.utils;
  - Cobertura completa *mypy* para tests/ e incolume.py.coding_dojo_jedi.utils;
  - Cobertura completa *flake8* para tests/ e incolume.py.coding_dojo_jedi.utils;
### Fixed
  - Correção dos diretórios do coding-dojo que apresentavam erro durante o teste automatizado;
  - Correções ortográficas na documentação;

## [1.38.4]	 &#8212; 	2023-10-01:
### Fixed
  - Desativado webtest para releases-gwa, devido a problemas de execução em GWA;

## [1.38.3]	 &#8212; 	2023-10-01:
### Fixed
  - Corrigido estrutura do dojo 20220721, devido a problemas de execução em GWA;

## [1.38.2]	 &#8212; 	2023-10-01:
### Fixed
  - Desativado testes web para GWA.;

## [1.38.1]	 &#8212; 	2023-10-01:
### Fixed
  - Redefinido timeout em GWA;

## [1.38.0]	 &#8212; 	2023-10-01:
### Added
  - Suite MKDocs para gerenciar documentação;
  - Acrescentado estrutura de documentação;
  - Instalado piloto para lint ruff;
  - Disponibilizado documentação em GitHub Pages;
  - Criados processo de automação via GWA;
  - Acrescentados geração de artefatos automaticamente;
### Changed
  - Aplicado cobertura total para lint mypy;
  - Aplicado cobertura total para lint pylint;
  - Restruturação de script RPA em taskipy;

## [1.37.0]	 &#8212; 	2023-09-25:
### Changed
  - Ampliado aplicação de estilo com blue;
  - Ampliado amplicação de estilo com isort;
  - Aplicado ampliação de estilo com ruff;
### Fixed
  - Tratativa em corrigir a falha de validação;

## [1.36.0]	 &#8212; 	2023-09-25:
### Added
  - MKDocs para gerenciar documentação;
  - Acrescentado estrutura de documentação;
  - Instalado piloto com ruff;
### Changed
  - Ampliado aplicação de estilo com blue;
  - Ampliado amplicação de estilo com isort;
  - Aplicado ampliação de estilo com ruff;
### Removed
  - Removido suporte a Python 3.8;
  - Removido suporte a Python 3.9;

## [1.35.0]	 &#8212; 	2023-09-24:
### Added
  - Adicionado classifiers a descrição do projeto;
  - Acrescentado github workflows actions para gerar pacotes de releases e monitorar testes;

## [1.34.0]	 &#8212; 	2023-09-21:
### Deprecated
  - Remover suporte a Python 3.10 - obsoleto a partir de out/2026;
### Removed
  - Removido suporte a Python 3.8 - obsoleto a partir de out/2024;
  - Removido suporte a Python 3.9 - obsoleto a partir de out/2025;
### Added
  - Adicionado classifiers à descrição do projeto;

## [1.33.0]	 &#8212; 	2023-09-19:
### Added
  - Ferramentas Quality Assurance (QA);
  - Ferramentas Linters consolidados para projetos JEDI;
  - Adicionado prototipo do lint ruff;
### Removed
  - Removido suporte a Python 3.7;
  - Removido das dependências lint o pacote black;
### Changed
  - Melhoria e ampliação na validação de testes;
  - Acrescentado CHANGELOG.md ao projeto;
  - Editado os registros do `git tag -n` para aderência ao padrão keep-a-changelog;
### Deprecated
  - Remover Suporte a Python 3.8;
  - Remover Suporte a Python 3.9;

## [1.32.0]	 &#8212; 	2023-09-16:
### Deprecated
  - Remover Suporte a Python 3.7;
### Added
  - Instalado ferramenta para gerir CHANGELOG.md;
  - Aderido conformidades com os padrões: keep-a-changelog, Semantic Version, Conventional Commit;

## [1.31.0]	 &#8212; 	2023-04-03:
### Added
  - Atualizações na estrutura do projeto;

## [1.30.0]	 &#8212; 	2022-09-26:
### Changed
  - Até dojo 26-09-2022;

## [1.29.0]	 &#8212; 	2022-09-21:
### Changed
  - Até dojo 21-09-2022;

## [1.28.0]	 &#8212; 	2022-09-19:
### Changed
  - Até dojo 19-09-2022;

## [1.27.0]	 &#8212; 	2022-09-14:
### Changed
  - Até dojo 14-09-2022;

## [1.25.0]	 &#8212; 	2022-09-10:
### Changed
  - Até dojo 10-09-2022;

## [1.24.0]	 &#8212; 	2022-09-09:
### Changed
  - Até dojo 09-09-2022;

## [1.23.0]	 &#8212; 	2022-09-07:
### Changed
  - Até dojo 07-09-2022;

## [1.22.0]	 &#8212; 	2022-09-06:
### Changed
  - Até dojo 05-09-2022;

## [1.21.0]	 &#8212; 	2022-09-01:
### Changed
  - Até dojo 31-08-2022;

## [1.20.0]	 &#8212; 	2022-08-31:
### Changed
  - Até dojo 26-08-2022;

## [1.19.0]	 &#8212; 	2022-08-24:
### Changed
  - Até dojo 24-08-2022;

## [1.18.0]	 &#8212; 	2022-08-22:
### Changed
  - Até dojo 22-08-2022;

## [1.17.0]	 &#8212; 	2022-08-19:
### Changed
  - Até dojo 19-08-2022;

## [1.16.0]	 &#8212; 	2022-08-19:
### Changed
  - Até dojo 17-08-2022;

## [1.15.1]	 &#8212; 	2022-08-15:
### Changed
  - Até dojo 15-08-2022;

## [1.14.0]	 &#8212; 	2022-08-12:
### Changed
  - Até dojo 12-08-2022;

## [1.13.5]	 &#8212; 	2022-08-12:
### Changed
  - Atualizado README de dojos;

## [1.13.4]	 &#8212; 	2022-08-12:
### Fixed
  - Recuperado dojos anteriores;

## [1.13.3]	 &#8212; 	2022-08-12:
### Fixed
  - Recuperado dojos anteriores;

## [1.13.0]	 &#8212; 	2022-08-12:
### Changed
  - Acrescentado site para Desafio de codificação;

## [1.12.0]	 &#8212; 	2022-08-10:
### Changed
  - Até dojo 10-08-2022;

## [1.11.0]	 &#8212; 	2022-08-09:
### Changed
  - Até dojo 09-08-2022;

## [1.10.1]	 &#8212; 	2022-08-08:
### Changed
  - Até dojo 08-08-2022;

## [1.10.0]	 &#8212; 	2022-08-03:
### Changed
  - Até dojo 05-08-2022;

## [1.9.0]	 &#8212; 	2022-08-01:
### Changed
  - Até dojo 01-08-2022;

## [1.8.2]	 &#8212; 	2022-08-01:
### Changed
  - Até dojo 31-07-2022;

## [1.7.0]	 &#8212; 	2022-07-23:
### Changed
  - Até dojo 23-07-2022;

## [1.0.0]	 &#8212; 	2022-07-22:
### Changed
  - Dojos fase restruturação finalizada;

## 0.1.0	 &#8212; 	2022-07-22:
### Added
  - Dojos anteriores a estruturação;

---

[1.0.0]: https://github.com/incolume-jedi/coding-dojo/compare/0.1.0...1.0.0
[1.7.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.0.0...1.7.0
[1.8.2]: https://github.com/incolume-jedi/coding-dojo/compare/1.7.0...1.8.2
[1.9.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.8.2...1.9.0
[1.10.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.9.0...1.10.0
[1.10.1]: https://github.com/incolume-jedi/coding-dojo/compare/1.10.0...1.10.1
[1.11.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.10.1...1.11.0
[1.12.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.11.0...1.12.0
[1.13.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.12.0...1.13.0
[1.13.3]: https://github.com/incolume-jedi/coding-dojo/compare/1.13.0...1.13.3
[1.13.4]: https://github.com/incolume-jedi/coding-dojo/compare/1.13.3...1.13.4
[1.13.5]: https://github.com/incolume-jedi/coding-dojo/compare/1.13.4...1.13.5
[1.14.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.13.5...1.14.0
[1.15.1]: https://github.com/incolume-jedi/coding-dojo/compare/1.14.0...1.15.1
[1.16.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.15.1...1.16.0
[1.17.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.16.0...1.17.0
[1.18.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.17.0...1.18.0
[1.19.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.18.0...1.19.0
[1.20.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.19.0...1.20.0
[1.21.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.20.0...1.21.0
[1.22.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.21.0...1.22.0
[1.23.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.22.0...1.23.0
[1.24.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.23.0...1.24.0
[1.25.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.24.0...1.25.0
[1.27.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.25.0...1.27.0
[1.28.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.27.0...1.28.0
[1.29.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.28.0...1.29.0
[1.30.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.29.0...1.30.0
[1.31.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.30.0...1.31.0
[1.32.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.31.0...1.32.0
[1.33.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.32.0...1.33.0
[1.34.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.33.0...1.34.0
[1.35.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.34.0...1.35.0
[1.36.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.35.0...1.36.0
[1.37.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.36.0...1.37.0
[1.38.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.37.0...1.38.0
[1.38.1]: https://github.com/incolume-jedi/coding-dojo/compare/1.38.0...1.38.1
[1.38.2]: https://github.com/incolume-jedi/coding-dojo/compare/1.38.1...1.38.2
[1.38.3]: https://github.com/incolume-jedi/coding-dojo/compare/1.38.2...1.38.3
[1.38.4]: https://github.com/incolume-jedi/coding-dojo/compare/1.38.3...1.38.4
[1.39.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.38.4...1.39.0
[1.40.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.39.0...1.40.0
[1.40.1]: https://github.com/incolume-jedi/coding-dojo/compare/1.40.0...1.40.1
[1.44.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.40.1...1.44.0
[1.45.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.44.0...1.45.0
[1.46.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.45.0...1.46.0
[1.47.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.46.0...1.47.0
[1.48.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.47.0...1.48.0
[1.48.1]: https://github.com/incolume-jedi/coding-dojo/compare/1.48.0...1.48.1
[1.49.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.48.1...1.49.0
[1.50.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.49.0...1.50.0
[1.51.0]: https://github.com/incolume-jedi/coding-dojo/compare/1.50.0...1.51.0
