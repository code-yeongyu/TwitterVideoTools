# twitter_liked_video_downloader

- A multiprocessing supported twitter video downloader

## Setup

### Settings file

Create `settings.json` at the root of the directory, and fill like below.

```json
{
  "username": "USERNAME",
  "PASSWORD": "PASSWORD",
  "recent_liked": "Your recent liked tweet link",
  "videos_path": "video output path"
}
```

### Install Requirements

```sh
poetry install
```

## Run

```sh
poetry shell
python3 main.py
```
