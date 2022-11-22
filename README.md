# Twitter Video Tools

[![PyPI version](https://badge.fury.io/py/twitter-video-tools.svg)](https://badge.fury.io/py/twitter-video-tools)
[![Test](https://github.com/code-yeongyu/twitter_video_tools/actions/workflows/test.yaml/badge.svg?branch=master)](https://github.com/code-yeongyu/twitter_video_tools/actions/workflows/test.yaml)
[![codecov](https://codecov.io/gh/code-yeongyu/TwitterVideoTools/branch/master/graph/badge.svg?token=97K8BBWOH7)](https://codecov.io/gh/code-yeongyu/TwitterVideoTools)

- A multi-processing supported video downloader
- supports downloading videos from twitter (or specific user from twitter) && monsnode.

## Install

### with PIP

```sh
pip install twitter-video-tools
```

### with Poetry (Recommended)

```sh
poetry add twitter-video-tools
```

## Contribution

### Prerequisites

- Python 3.9
- poetry
- code editor (vscode recommended)

### Overview of Development Environments

- Local
  - vscode ready (launching, debugging, formatting)
  - strict type checking using [mypy](https://github.com/python/mypy) & [pyright](https://github.com/microsoft/pyright)
  - amazing linters & formatters ([`yapf`](https://github.com/google/yapf), [`pylint`](https://github.com/PyCQA/pylint), [`isort`](https://github.com/PyCQA/isort))
    - `unify` for forcing single-quote
  - unit test using [`pytest`](https://github.com/myint/unify)

- GitHub Actions
  - [All PRs are statically analyzed & checked by `yapf`, `pylint`, `pyright`, `mypy`](https://github.com/code-yeongyu/TwitterVideoTools/actions/workflows/check_code.yaml)
  - [All PRs are tested with `pytest`](https://github.com/code-yeongyu/TwitterVideoTools/actions/workflows/test.yaml)
  - [Can be released with Github Action when creating GitHub Releases](https://github.com/code-yeongyu/TwitterVideoTools/actions/workflows/release.yaml)

### All-in-one

```sh
gh repo clone code-yeongyu/twitter_video_tools
python3 -m pip install poetry
poetry install # install dependencies
code --install-extension emeraldwalk.RunOnSave # to force single quote
code --install-extension tamasfe.even-better-toml # for handling toml
```

Done!

### Test

```sh
poetry shell
inv test
```
