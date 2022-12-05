# pylint: disable=useless-import-alias

from typing import Optional

import typer
from rich import print as rich_print

from .twitter_video_tools import TwitterVideoTools as TwitterVideoTools
from .utils import URLValidator


def _cli_main(
    link: str = typer.Argument(..., help='Video tweet link or target user\'s likes or media.'),
    username: Optional[str] = typer.Option(None, help='Your twitter credentials username.'),
    password: Optional[str] = typer.Option(None, help='Your twitter credentials password.'),
    until_link: Optional[str] = typer.Option(
        None,
        help='Keeps finding videos until this link is found. None for no limit. Only for user\'s likes or media.',
    ),
) -> None:
    url_validator = URLValidator(link)

    if not url_validator.is_valid_link():
        rich_print(f'\'[underline]{link}[/underline]\' [bold red]is an invalid link.[/bold red]')
        return
    twitter_video_tools = TwitterVideoTools(username, password)

    if url_validator.is_valid_twitter_media_link():
        target_username = link.split('/')[3]
        twitter_video_tools.download_from_user(target_username, until_link)
    elif url_validator.is_valid_twitter_liked_link():
        target_username = link.split('/')[3]
        twitter_video_tools.download_from_liked_tweets(target_username, until_link)
    else:
        twitter_video_tools.download([link])


def main() -> None:
    typer.run(_cli_main)


__all__ = [
    'main',
    'TwitterVideoTools',
]
