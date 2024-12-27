# Script Dojo

Este script é um facilitador criado especificamente para o incolume-dojo e que gerencia atividades repetitivas não focadas ao escopo principal do projeto, com a finalidade de agilizar e maximilizar algumas das atividades corriqueiras.

Detalhes aprofundados podem ser averiguados na própria documentação `dojo --help` ou `dojo -h`, que exibirá algo como:

```
$ dojo -h

Usage: dojo [OPTIONS] COMMAND [ARGS]...

  Command Line Interface for dojo.

Options:
  --debug / --no-debug  Activate debug mode.
  -h, --help            Show this message and exit.  

Commands:
  init    Initiate a dojo boilerplate.
  show    Show configuration.
  sumary  Generates a summary file with solved dojos.
```

## dojo init

Inicializa a estrutura boilerplate para o projeto, criando o diretório e arquivos no formato apropriado.
```
incolume/py/coding_dojo_jedi
  dojo20241225/
    __init__.py
    test_20241225.py
    README.md
```

## dojo show
Exibe as configurações do script.'

## dojo sumary

Gera arquivos de sumário com os dojos resolvidos. os quais são: `docs/user_guide/dojos-resolvidos.md` com foco na documentação oficial; e `incolume/py/coding_dojo_jedi/README.md` com foco na navegação de códigos;