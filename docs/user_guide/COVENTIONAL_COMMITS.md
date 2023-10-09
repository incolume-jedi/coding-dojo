# Git commits messages

---

This project follow Conventional Commits, A specification for adding human and
machine readable meaning to commit messages.

```bash
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

The commit contains the following structural elements, to communicate intent to the consumers of your library:

+ **type**: the type of commit (feat|feature, fix|bugfix, chore, refactor, docs, style, test, perf, ci, build, revert)
    + **feat**: A commit of the type feat introduces a new feature to the codebase (this correlates with MINOR in Semantic Versioning).
    + **fix** or **bugfix**: A commit of the type fix patches a bug in your codebase (this correlates with PATCH in Semantic Versioning).
    + **chore**: Changes that do not relate to a fix or feature and don´t modify src or test files (for example updating dependencies);
    + **refactor**: refactored code that neither fixes a bug nor adds a feature;
    + **docs**: updates to documentation such as a the README or other markdown or rst files;
    + **style**: Changes that do not affect the meaning of the code, likely related to code formatting such as white-space, missing semi-colons, black style applied, and so on;
    + **test**: Including new or correcting previous tests;
    + **perf**: preformance impovements;
    + **ci**: Continuos integration related;
    + **build**: changes that affect the build system or external dependencies;
    + **revert**: reverts a previous commit;
+ **scope**: This is optional, but indicate a specific scope ;
+ **description**: show what was done in the commit;
+ **body**: Full description, if descript not enough;
+ **footer**: This is optional, but agregate additional information about commit, lake revisor, references, millistone and others (for example "close #issue-id").

## Examples
### Commit message with description and breaking change footer
```bash
feat: allow provided config object to extend other configs
BREAKING CHANGE: `extends` key in config file is now used for extending other config files
```

## Commit message with ! to draw attention to breaking change
```shell
feat!: send an email to the customer when a product is shipped
```

## Commit message with scope and ! to draw attention to breaking change
```shell
feat(api)!: send an email to the customer when a product is shipped
```

## Commit message with both ! and BREAKING CHANGE footer
```shell
chore!: drop support for Python 2.6

BREAKING CHANGE: Some features not available in Python 2.7-.
```

## Commit message with no body
```shell
docs: correct spelling of CHANGELOG
```

## Commit message with scope
```shell
feat(lang): add polish language
```

## Commit message with multi-paragraph body and multiple footers
```shell
fix: prevent racing of requests

Introduce a request id and a reference to latest request. Dismiss
incoming responses other than from latest request.

Remove timeouts which were used to mitigate the racing issue but are
obsolete now.

Reviewed-by: @britodfbr
Refs: #123
```


The full specification maybe access on [english lang](https://www.conventionalcommits.org/en/v1.0.0/#specification) or others languages about [Brazilian Portuguese](https://www.conventionalcommits.org/pt-br/v1.0.0/#specification).
