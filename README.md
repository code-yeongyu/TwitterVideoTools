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

### with Poetry

```sh
poetry add twitter-video-tools
```

## Usage

### Command line

```sh
python3 -m twitter_video_tools [link]
```

Supported link types:

- Video tweet: <https://twitter.com/twtvtOfficial/status/1599748329927499777>
- Video from [monsnode](https://monsnode.com): <https://monsnode.com/v1506575871309589251>
- Specific user's uploaded videos: <https://twitter.com/twtvtOfficial/media>
- Specific user's liked videos: <https://twitter.com/twtvtOfficial/likes>

### Python Embedding

```python
from twitter_video_tools import TwitterVideoTools

with TwitterVideoTools() as twitter_video_tools:
    twitter_video_tools.download_from_user('twtvtOfficial')
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
    - type hint generator [monkeytype](https://github.com/Instagram/MonkeyType) also included
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

## Inspirations

### [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- Inspired me to start this project. yt-dlp is a fork project of youtube-dl.
- Since the cookie option of yt-dlp's twitter extractor is not working, I decided to make my own project, using browser automation.

### [playwright](https://playwright.dev/python/)

- Microsoft's browser automation module.
- Another major project to made me to start this project. I made up my mind to make TwitterVideoTools to experience playwright.
- It would be so painful to imagine making this project with selenium, but I enjoyed a lot while writing the twitter crawler part thanks to playwright.

### [typer](https://typer.tiangolo.com/)

- Ever since I started this project, I always wanted to support CLI with typer's awesome development experience.
- TwitterVideoTools' CLI is written with typer, and it is so beautiful and easy to use at the same time.

### [pyright](https://github.com/microsoft/pyright) & [mypy](http://mypy-lang.org/) & [monkeytype](https://github.com/Instagram/MonkeyType)

- These three tools helped me to write fully-typed python code.
- I won't start my python project without these tools.

### [my python project template](https://github.com/code-yeongyu/python3.9-project-template)

- I made this template to make my python project development experience better.
  - Safe & Convient development environment
    - Strict type checking
    - Amazing linters & formatters
    - Unit test supported
- This project is also based on this template.
