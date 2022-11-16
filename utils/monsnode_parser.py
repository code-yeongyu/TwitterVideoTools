from __future__ import annotations

import typing

import requests
from bs4 import BeautifulSoup


class MonsnodeParser:
    TARGET_URL = 'https://monsnode.com/'

    def get_video(self, link: str, timeout: float = 5000) -> tuple[str, str]:
        request = requests.get(link, timeout=timeout)
        soup = BeautifulSoup(request.text, 'html.parser')

        uploader_name = soup.select('body > div:nth-child(2) > div:nth-child(2) > div:nth-child(5) > b')[0].text

        title = soup.select('body > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)')[0].text
        title = title.replace('/', '_')
        title = title.replace('\n', '')
        title = f'{uploader_name} - {title}'

        video_path: str = typing.cast(
            str,
            soup.select('body > div:nth-child(2) > div:nth-child(1) > a:nth-child(2)')[0]['href'])
        video_url = self.TARGET_URL + video_path

        return title, video_url
