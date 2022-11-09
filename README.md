# Python 3.9 Project Template with poetry

- Python 3.9
- strict type checking using mypy
- amazing linters & formatters (yapf, pylint, isort)
  - `unify` for forcing single-quote
- testing (pytest)
- powerful class model (pydantic)
- vscode launch & formatting setups

## Setup

### All-in-one

```sh
gh repo clone code-yeongyu/python3.9-project-template # clone the code into your local
python3 -m pip install poetry
poetry install # install dependencies
code --install-extension emeraldwalk.RunOnSave # to force single quote
```

Done!

## Test

```sh
poetry shell
pytest .
```

```sh
python main.py
```
