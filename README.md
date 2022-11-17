# Twitter Video Tools
[![PyPI version](https://badge.fury.io/py/twitter-video-tools.svg)](https://badge.fury.io/py/twitter-video-tools)
[![Test](https://github.com/code-yeongyu/twitter_video_tools/actions/workflows/test.yaml/badge.svg?branch=master)](https://github.com/code-yeongyu/twitter_video_tools/actions/workflows/test.yaml)
[![codecov](https://codecov.io/gh/code-yeongyu/twitter_video_tools/branch/master/graph/badge.svg?token=97K8BBWOH7)](https://codecov.io/gh/code-yeongyu/twitter_video_tools)

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

### Quick Info of setups

- strict type checking using mypy
- amazing linters & formatters (`yapf`, `pylint`, `isort`)
  - `unify` for forcing single-quote
- unit test using `pytest`
- vscode launch & formatting setups

### All-in-one

```sh
gh repo clone code-yeongyu/twitter_video_tools
python3 -m pip install poetry
poetry install # install dependencies
code --install-extension emeraldwalk.RunOnSave # to force single quote
```

Done!

### Test

```sh
poetry shell
inv test
```
