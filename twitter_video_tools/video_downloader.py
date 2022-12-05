from __future__ import annotations

from typing import Optional, Union

from twitter_video_tools.utils import execute_parallel

from .monsnode_parser import MonsnodeParser
from .platform_video_downloader import PlatformVideoDownloader


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

    def download_videos(self, links: Union[str, list[str]]) -> None:
        is_parallel_downloadable = isinstance(links, list) and len(links) > 1
        if is_parallel_downloadable:
            arguments = [(link, ) for link in links]
            execute_parallel(self.download_video, arguments)
            return
        link = links if isinstance(links, str) else links[0]
        self.download_video(link)

    def download_video(self, link: str) -> None:
        if 'monsnode.com' in link:
            self.platform_video_downloader.download_monsnode_video(link)
            return
        self.platform_video_downloader.download_twitter_video(link, self.username, self.password)
