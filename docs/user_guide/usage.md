[![Tests CI/CD](https://github.com/incolume-jedi/coding-dojo/actions/workflows/tests-gwa-ci-cd.yml/badge.svg)](https://github.com/incolume-jedi/coding-dojo/actions/workflows/tests-gwa-ci-cd.yml)

[//]: # ([![publish automatically]&#40;https://github.com/incolume-treinamentos/incolume.py.model-2023-07-05/actions/workflows/publish-automatically.yml/badge.svg&#41;]&#40;https://github.com/incolume-treinamentos/incolume.py.model-2023-07-05/actions/workflows/publish-automatically.yml&#41;)
[//]: # ([![poetry-mine-publish-automatically]&#40;https://github.com/incolume-treinamentos/incolume.py.model-2023-07-05/actions/workflows/poetry-mine-publish-automatically.yml/badge.svg&#41;]&#40;https://github.com/incolume-treinamentos/incolume.py.model-2023-07-05/actions/workflows/poetry-mine-publish-automatically.yml&#41;)
[//]: # ([![Poetry Mine Pypi Autopublish]&#40;https://github.com/incolume-treinamentos/incolume.py.model-2023-07-05/actions/workflows/poetry-mine-pypi-autopublish.yml/badge.svg&#41;]&#40;https://github.com/incolume-treinamentos/incolume.py.model-2023-07-05/actions/workflows/poetry-mine-pypi-autopublish.yml&#41;)
[//]: # ([![Poetry Test PyPI Manual Publish]&#40;https://github.com/incolume-treinamentos/incolume.py.model-2023-07-05/actions/workflows/poetry-testpypi-manual-publish.yml/badge.svg?branch=dev&#41;]&#40;https://github.com/incolume-treinamentos/incolume.py.model-2023-07-05/actions/workflows/poetry-testpypi-manual-publish.yml&#41;)
[//]: # ([![Poetry Multiprocess]&#40;https://github.com/incolume-treinamentos/incolume.py.model-2023-07-05/actions/workflows/poetry-multiprocess.yml/badge.svg&#41;]&#40;https://github.com/incolume-treinamentos/incolume.py.model-2023-07-05/actions/workflows/poetry-multiprocess.yml&#41;)
[//]: # ([![tagged-release]&#40;https://github.com/incolume-treinamentos/incolume.py.model-2023-07-05/actions/workflows/targged-release.yaml/badge.svg&#41;]&#40;https://github.com/incolume-treinamentos/incolume.py.model-2023-07-05/actions/workflows/targged-release.yaml&#41;)
[//]: # ([![Tests/Release]&#40;https://github.com/incolume-treinamentos/incolume.py.model-2023-07-05/actions/workflows/tests_new.yml/badge.svg&#41;]&#40;https://github.com/incolume-treinamentos/incolume.py.model-2023-07-05/actions/workflows/tests_new.yml&#41;)
[//]: # ([![GWA Flow]&#40;https://github.com/incolume-treinamentos/incolume.py.model-2023-07-05/actions/workflows/gwa-flow.yml/badge.svg&#41;]&#40;https://github.com/incolume-treinamentos/incolume.py.model-2023-07-05/actions/workflows/gwa-flow.yml&#41;)

# Coding Dojo


Details for [scope](../prefacio.md#escopo) and [tool](../prefacio.md#ferramentas-aplicadas).

---
## Start Use the model
1. Access https://github.com/incolume-treinamentos/incolume.py.model-2023-07-05.
1. Click on green button __Use this template__;
1. Bellow click on __Create a new repository__;
1. Fill the fields as you wish; finish the create a github project on github.com;
1. Clone the project, on local host;

1. Create the control's branches:
   ```bash
   $ git br main
   $ git br tags
   ```
1. Configure environment:
    ```shell
   $ poetry env use 3.10
   $ poetry install
   $ poetry run task setup
    ```

2. Change configuration:
   1. Set a new project name and version:
      ```bash
      $ vim pyproject.toml

      [tool.poetry]
      name = "incolume-py-model-2023-07-05"
      version = 1.111.0
      ```
      ```shell
      $ cat pyproject.toml

      [tool.poetry]
      name = "incolume.py.abc"
      version = 0.1.0

      ```

   2. rename path project:
      ```bash
      git mv incolume/py/model_2023_07_05/ incolume/py/abc
      ```
   3. Commit changes

    ```shell
   # the way wished
   $ git co -b enhancement/epoch#$(date +%s);
   $ git ci -m 'chore: #0 Atualização do projeto.'
   $ git co dev
   $ git merge --no-ff enhancement/epoch#0000000000000
   $ poetry run task preminor
   $ poetry run task patch
   ```
   ```shell
   # easy way
   git ci -m 'chore: #0 Atualização do projeto.'
   poetry run task preminor
   poetry run task patch
   ```

4. Commit changes

## Tests, Linters and Checkers
1. For run tests:
    ```shell
    $ poetry run pytest  # run all
    ```
   ```shell
   $ poetry run pytest -vv tests/test_skell.py::TestSkellCase::test_kwargs  # run one
   $ poetry run pytest -vv tests/test_skell.py::TestSkellCase  # run class
   $ poetry run pytest -vv tests/test_skell.py  # run file
   ```

1. For run linters:
    ```shell
    $ poetry run task linter
    ```

===

3. Configure pylint tool
   1. Edit _pyproject.toml_, add on end file.
   ```bash
   ...
   [tool.pylint.format]
   # Maximum number of characters on a single line.
   max-line-length = 160

   [tool.pylint.basic]
   # Allow shorter and longer variable names than the default.
   argument-rgx = "[a-z_][a-z0-9_]*$"
   attr-rgx = "[a-z_][a-z0-9_]*$"
   variable-rgx = "[a-z_][a-z0-9_]*$"

   # Ensure that orjson is analysed as a C extension by pylint.
   extension-pkg-whitelist = "orjson"

   [tool.pylint.messages_control]
   disable = [
       # Disable too many and too few checks.
       "too-many-ancestors",
       "too-many-arguments",
       "too-many-boolean-expressions",
       "too-many-branches",
       "too-many-function-args",
       "too-many-instance-attributes",
       "too-many-lines",
       "too-many-locals",
       "too-many-nested-blocks",
       "too-many-public-methods",
       "too-many-return-statements",
       "too-many-statements",
       "too-few-public-methods",

       # Similar lines in files (often the case in tests).
       "duplicate-code",

       # Many functions (e.g. callbacks) will naturally have unused arguments.
       "unused-argument",

       # Disable checking that method could be a function in classes (often used for organisation).
       "no-self-use",

       # Disable failure for TODO items in the codebase (code will always have TODOs).
       "fixme",

       # Disable docstrings checks as we don't require excessive documentation.
       "missing-docstring",

       "no-member",
       "unspecified-encoding",
   ]
   ```
   2. Commit
      ```bash
      $ git ci -m "Configure pylint tool" pyproject.toml
      ```
4. Configure mypy tool
    1. Edit _pyproject.toml_, add on end file.
    ```bash
    ...
       [tool.mypy]
       mypy_path = "incolumepy"
       check_untyped_defs = true
       disallow_any_generics = true
       ignore_missing_imports = true
       no_implicit_optional = true
       show_error_codes = true
       strict_equality = true
       warn_redundant_casts = true
       warn_return_any = true
       warn_unreachable = true
       warn_unused_configs = true
       no_implicit_reexport = true
    ```
   2. Commit
   ```bash
   $ git ci -m "Configure mypy tool" pyproject.toml
   ```
5. Configure isort tool
    1. Edit _pyproject.toml_, add on end file.
    ```bash
    ...
    [tool.isort]
    multi_line_output = 3
    line_length = 160
    include_trailing_comma = true
    ```
    2. Commit
      ```bash
      $ git ci -m "Configure isort tool" pyproject.toml
      ```
6. Configure flake8 tool
    1. Edit _pyproject.toml_, add on end file.
    ```bash
    ...
    [flake8]
    max-line-length = 160
    ```
    2. Commit
      ```bash
      $ git ci -m "Configure flake8 tool" pyproject.toml
      ```
7. Configure black tool:
    1. Edit _pyproject.toml_, add on end file.
    ```bash
    ...
    [tool.black]
    line_length = 160
    ```
    2. Commit
      ```bash
      $ git ci -m "Configure black tool" pyproject.toml
      ```
8. Configure tox tool:
    1. Edit _pyproject.toml_, add on end file.
    ```bash
    [tool.tox]
    legacy_tox_ini = """
    [tox]
    minversion = 3.3.0
    isolated_build = True
    envlist =
    black
    flake8
    isort
    mypy
    pydocstyle
    pylint
    py{36,37,38,39,310}

    ;[tox:.package]
    ;basepython = python3

    [testenv]
    whitelist_externals = poetry
    skip_install = true
    commands =
    poetry env use {envpython}
    poetry install -vv --no-root
    poetry run pytest {posargs} tests/

    [testenv:flake8]
    deps = flake8
    commands = flake8 --config pyproject.toml incolumepy/ tests/

    [testenv:mypy]
    deps =
    mypy
    types-toml
    commands = mypy incolumepy/

    [testenv:pydocstyle]
    commands = poetry run pydocstyle incolumepy/ tests/

    [testenv:isort]
    commands = poetry run isort --check --atomic --py all incolumepy/ tests/

    [testenv:pylint]
    commands = poetry run pylint incolumepy/ tests/

    [testenv:black]
    commands = poetry run black --check incolumepy/ tests/
    """
    ```
    2. Commit
      ```bash
      $ git ci -m "Configure tox tool" pyproject.toml
      ```

## Testting lint configurate
1. Test pydocstyle:
   ```bash
   $ pydocstyle incolumepy/ tests/
   ```
2. Test pylint
   ```bash
   $ pylint incolumepy/ tests/
   ```
3. Test mypy
   ```bash
   $ mypy incolumepy/ tests/
   ```
4. Test isort
   ```bash
   $ isort --check incolumepy/ tests/
   ```
5. Test flake8
   ```bash
   $ flake8 --config pyproject.toml incolumepy/ tests/
   ```
6. Test black
   ```bash
   $ black --check incolumepy/ tests/
   ```

## Testting tox configurate
6. Text tox
   ```bash
   $ tox
   ```

## Control version with poetry
Unlike bumpversion, poetry changes the version of the main file only.
To work around this situation and update the version of pyproject.toml,
__init__.py and version.txt, we will do the following procedure.

```bash
$ cat > incolumepy/gwa/__init__.py << eof
import toml
from pathlib import Path
__root__ = Path(__file__).parents[0]
version_file = __root__.joinpath('version.txt')
version_file.write_text(f"{toml.load(Path(__file__).parents[2].joinpath('pyproject.toml'))['tool']['poetry']['version']}\n")
__version__ = version_file.read_text().strip()
eof

$ v=`poetry version prerelease`; pytest tests/ && git ci -m "$v" pyproject.toml $(find -name "version.txt")  #sem tag
$ s=`poetry version patch`; pytest tests/ && git ci -m "`echo $s`" pyproject.toml `find -name "version.txt"`; git tag -f `poetry version -s` -m "$(echo $s)"  #com tag

```
## Facility with make
Use make to easy various commands.
```bash
$ curl https://pastebin.com/raw/eTHpL70G -o Makefile    # or
$ curl https://raw.githubusercontent.com/incolumepy-prospections/incolumepy.gwa/main/Makefile -o Makefile    # last version
```
### Makefile help
```bash
$ make help
```
### New prerelease with Makefile
```bash
$ git co dev
$ git merge --no-ff [branch] --autostash
$ make prerelease
```
### New release with Makefile
```bash
$ git co dev
$ make release
```
### Checking lint
```bash
$ make lint
```
### Run tox over make
```bash
$ make tox
```

# Github Workflows Actions (GWA)
First create the directory for GWA:
```bash
mkdir -pv .github/workflows
```

## This Models:
- GitHub WorkFlow with tags Running tox; Build pack; Create release; publish TestPyPI and PyPI
```bash
curl https://raw.githubusercontent.com/incolumepy-prospections/incolumepy.gwa/main/.github/workflows/gwa-flow.yml -o .github/workflows/gwa-flow.yml
```

- Run tox and  generate coverage report:
```bash
curl https://raw.githubuserconcurl https://raw.githubusercontent.com/incolumepy-prospections/incolumepy.gwa/main/.github/workflows/tests_ci_cd.yaml -o .github/workflows/tests_ci_cd.yml
```

- Publish manualy releases/prereleases into test.pypi.org with poetry:
```bash
curl https://raw.githubusercontent.com/incolumepy-prospections/incolumepy.gwa/main/.github/workflows/poetry-testpypi-manual-publish.yml -o .github/workflows/poetry-testpypi-manual-publish.yml
```

- Publish automatically releases into pypi.org and test.pypi.org with poetry, after pass on tests from tests_ci_cd:
```bash
curl https://raw.githubusercontent.com/incolumepy-prospections/incolumepy.gwa/main/.github/workflows/poetry-mine-publish-automatically.yml -o .github/workflows/poetry-mine-publish-automatically.yml
```

- Publish automatically releases into pypi.org only, after pass on tests from tests_ci_cd:
```bash
curl https://raw.githubusercontent.com/incolumepy-prospections/incolumepy.gwa/main/.github/workflows/poetry-mine-pypi-autopublish.yml -o  .github/workflows/poetry-mine-pypi-autopublish.yml
```

- Publish automatically releases into pypi.org and test.pypi.org without poetry, after pass on tests from tests_ci_cd:
```bash
curl https://raw.githubusercontent.com/incolumepy-prospections/incolumepy.gwa/main/.github/workflows/publish-automatically.yml -o .github/workflows/publish-automatically.yml
```

- Publish automatically releases into pypi.org and test.pypi.org with multiprocess poetry, after pass on tests from tests_ci_cd:
```bash
curl https://raw.githubusercontent.com/incolumepy-prospections/incolumepy.gwa/main/.github/workflows/poetry-multiprocess.yml -o .github/workflows/poetry-multiprocess.yml
```

## Git Hooks
+ create .git-hooks folder into your project root directory, at the same level you already have .git folder;
```shell
mkdir .git-hooks
```
+ create hook files into this folder: pre-commit, prepare-commit-msg and all hooks (these files don't have an extension);
+ put the correct code into each file (I will add them below these steps);
```shell
curl https://raw.githubusercontent.com/incolumepy-prospections/incolumepy.gwa/main/.git-hooks/pre-commit -o .git-hooks/pre-commit
curl https://raw.githubusercontent.com/incolumepy-prospections/incolumepy.gwa/main/.git-hooks/prepare-commit-msg -o .git-hooks/prepare-commit-msg
curl https://raw.githubusercontent.com/incolumepy-prospections/incolumepy.gwa/main/.git-hooks/commit-msg -o .git-hooks/commit-msg
curl https://raw.githubusercontent.com/incolumepy-prospections/incolumepy.gwa/main/.git-hooks/pre-push -o .git-hooks/pre-push
```
+ change to execute mode;
```shell
chmod +x .git-hooks/*
```
+ run this command in your command line, into your main folder of your project (one level up from .git-hooks):
```shell
git config core.hooksPath .git-hooks;
```

+ READY;
