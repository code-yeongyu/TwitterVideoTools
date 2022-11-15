from __future__ import annotations

import multiprocessing
import multiprocessing.dummy
from typing import Any, Callable

import youtube_dl
from youtube_dl.utils import YoutubeDLError


class VideoDownloader:

    def _execute_parallel(self, func: Callable[[str], None], *args: Any, **kwargs: Any) -> None:
        pool = multiprocessing.dummy.Pool(multiprocessing.cpu_count())
        pool.map(func, *args, **kwargs)

    def download_video(self, link: str) -> None:
        ydl_opt = {
            'format': 'bestvideo/best',
            'outtmpl': 'videos/%(title)s.%(ext)s',
        }
        try:
            with youtube_dl.YoutubeDL(ydl_opt) as youtube_dl_downloader:
                youtube_dl_downloader.download([link])
        except YoutubeDLError:
            link = link.replace('\n', '')
            print(f'{link} failed')

    def download_videos(self, links: list[str]) -> None:
        self._execute_parallel(self.download_video, links)


video_downloader = VideoDownloader()
