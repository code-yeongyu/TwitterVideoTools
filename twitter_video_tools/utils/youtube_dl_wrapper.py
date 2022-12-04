from typing import Optional, Union

import yt_dlp

from .execute_parallel import execute_parallel


class YoutubeDLWrapper:    # pylint: disable=too-few-public-methods
    """A YoutubeDL wrapper class for supporting python embedded multi-processing"""

    def _youtube_dl_download_video(self, link: str, youtube_dl_option: Optional[dict[str, str]] = None) -> None:
        with yt_dlp.YoutubeDL(youtube_dl_option) as youtube_dl_downloader:
            youtube_dl_downloader: yt_dlp.YoutubeDL
            youtube_dl_downloader.download([link])

    def download(self, links: list[str], youtube_dl_option: Optional[dict[str, Union[str, int]]] = None) -> None:
        arguments = [(link, youtube_dl_option) for link in links]
        execute_parallel(self._youtube_dl_download_video, arguments)


youtube_dl_wrapper = YoutubeDLWrapper()    # singleton
