# Twitter Video Tools

- A multi-processing supported video downloader
- supports downloading videos from twitter (or specific user from twitter) && monsnode.

## Install

### PIP

```sh
pip install twitter-video-tools
```

### Poetry

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
