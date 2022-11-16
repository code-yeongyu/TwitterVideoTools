from __future__ import annotations

import multiprocessing
import multiprocessing.dummy
from typing import Any, Callable, Optional

import youtube_dl
from playwright.sync_api import sync_playwright
from youtube_dl.utils import DownloadError, YoutubeDLError

from .twitter_crawler import TwitterCrawler


class VideoDownloader:
    video_output_path: str = 'videos'
    username: Optional[str] = None
    password: Optional[str] = None

    def __init__(
        self,
        video_output_path: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ):
        self.video_output_path = video_output_path or self.video_output_path
        self.username = username
        self.password = password

    def download_videos(self, links: list[str]) -> None:
        arguments = [(link, ) for link in links]
        self._execute_parallel(
            self.download_video,
            arguments,
        )

    def download_video(self, link: str) -> None:
        try:
            self._download_public_video(link)
        except DownloadError as error:
            if not self.username or not self.password:
                raise ValueError('Username and password are required for private videos') from error
            print('Failed to download video, trying to download with authentication ...')
            self._download_twitter_private_video(link, self.username, self.password)
        except YoutubeDLError:
            link = link.replace('\n', '')
            print(f'{link} failed')

    def _download_public_video(self, link: str, video_filename: Optional[str] = None) -> None:
        youtube_dl_output_template = \
            f'{self.video_output_path}/{video_filename}' \
                if video_filename else \
            f'{self.video_output_path}/%(title)s.%(ext)s'
        youtube_dl_option = {'format': 'bestvideo/best', 'outtmpl': youtube_dl_output_template}
        with youtube_dl.YoutubeDL(youtube_dl_option) as youtube_dl_downloader:
            youtube_dl_downloader.download([link])

    def _download_twitter_private_video(self, target_link: str, username: str, password: str) -> None:
        with sync_playwright() as playwright_sync:
            browser = playwright_sync.webkit.launch(headless=True)
            page = browser.new_page()
            crawler = TwitterCrawler(page)
            crawler.login(username, password)
            video_info = crawler.get_video_of_tweet(target_link)
            if video_info:    # only if video exists
                print('twitter video found, downloading ...')
                video_filename, links = video_info
                for link in links:
                    self._download_public_video(link, video_filename)
            page.close()
            browser.close()

    def _execute_parallel(self, func: Callable[[str], None], *args: Any, **kwargs: Any) -> None:
        pool = multiprocessing.dummy.Pool(multiprocessing.cpu_count())
        pool.starmap(func, *args, **kwargs)
