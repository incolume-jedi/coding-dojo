# UV - Ultra Violeta

Um pacote escrito na linguagem rust para Python, extremamente rápido e gerenciador de projeto.

1. Multiplataforma: suporta macOS, Linux e Windows;
1. Instalável via curl ou pip;
1. Substitui com sucesso várias ferramentas pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv e outras;
1. Instala e gerencia Versões python e pacote de dependência dos projetos.
1. Disk-space eficiente, com um cache global para deduplicação de dependência;
1. Executa e instala Aplicações python.
1. Executa scripts, com suporte para metadados de dependência em linha.
1. Fornece gestão abrangente de projetos, com um arquivo de bloqueio universal.
1. Gerencia dependências e ambientes para scripts de arquivo único

## Instalação UV

### Unix like:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows like:
```
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Disponibilizar Python no ambiente dev

### Python 3.8

```
uv python install 3.8
```
### Python 3.9
```
uv python install 3.9
```
### Python 3.10
```
uv python install 3.10
```
### Python 3.11
```
uv python install 3.11
```
### Python 3.12
```
uv python install 3.12
```
### Python 3.13
```
uv python install 3.13
```
### Tadas as versões para o projeto
```
uv python install 3.8 3.9 3.10 3.11 3.12 3.13
```

## Fixar versão específica de Python para projeto

```
uv python pin 3.8
```

## Suporte a script

Crie um novo script e adicione metadados inline declarando suas dependências:
```
echo 'import requests; print(requests.get("https://astral.sh"))' > example.py

uv add --script example.py requests
```

Em seguida, execute o script em um ambiente virtual isolado:
```

uv run example.py

```