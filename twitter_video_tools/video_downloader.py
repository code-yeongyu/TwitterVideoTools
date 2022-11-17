from __future__ import annotations

from typing import Optional

from twitter_video_tools.platform_video_downloader import \
    PlatformVideoDownloader
from twitter_video_tools.utils import execute_parallel

from .monsnode_parser import MonsnodeParser


class VideoDownloader:
    """YoutubeDL wrapper with extra features"""
    username: Optional[str] = None
    password: Optional[str] = None
    platform_video_downloader: PlatformVideoDownloader

    def __init__(
            self,
            username: Optional[str] = None,
            password: Optional[str] = None,
            platform_video_downloader: PlatformVideoDownloader = PlatformVideoDownloader('videos', MonsnodeParser()),
    ):
        self.username = username
        self.password = password
        self.platform_video_downloader = platform_video_downloader

    def download_videos(self, links: list[str]) -> None:
        arguments = [(link, ) for link in links]
        execute_parallel(self.download_video, arguments)

    def download_video(self, link: str) -> None:
        if 'monsnode.com' in link:
            self.platform_video_downloader.download_monsnode_video(link)
            return
        self.platform_video_downloader.download_twitter_video(link, self.username, self.password)
