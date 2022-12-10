from __future__ import annotations

from types import TracebackType
from typing import Optional, Type

from playwright.sync_api import Browser as PlaywrightBrowser
from playwright.sync_api import sync_playwright

from .platform_video_downloader import PlatformVideoDownloader
from .twitter_crawler import TwitterCrawler
from .video_downloader import VideoDownloader


class TwitterVideoTools:
    username: Optional[str] = None
    password: Optional[str] = None
    video_downloader: VideoDownloader
    twitter_crawler: TwitterCrawler
    _browser: PlaywrightBrowser
    _debug: bool = False

    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        video_output_path: str = 'videos',
        debug: bool = False,
    ) -> None:
        self.username = username
        self.password = password
        self._debug = debug
        platform_video_downloader = PlatformVideoDownloader(video_output_path)
        self.video_downloader = VideoDownloader(username, password, platform_video_downloader)

        self._browser = sync_playwright().start().webkit.launch(headless=debug)
        page = self._browser.new_page()
        self.twitter_crawler = TwitterCrawler(page)
        if self.username and self.password:
            self.twitter_crawler.login(self.username, self.password)

    def __enter__(self) -> TwitterVideoTools:
        return self

    def download(self, tweet_links: list[str]) -> None:
        self.video_downloader.download_videos(tweet_links)

    def download_from_liked_tweets(self, username: str, until_link: Optional[str] = None) -> None:
        video_links: list[str] = []
        if until_link:
            video_links = self.twitter_crawler.get_liked_video_tweets_until(username, until_link)
        else:
            video_links = self.twitter_crawler.get_all_liked_video_tweets(username)

        self.video_downloader.download_videos(video_links)

    def download_from_user(self, username: str, until_link: Optional[str] = None) -> None:
        video_links: list[str] = []
        if until_link:
            video_links = self.twitter_crawler.get_media_tweets_until(username, until_link)
        else:
            video_links = self.twitter_crawler.get_all_media_tweets(username)

        self.video_downloader.download_videos(video_links)

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        self._browser.close()
