from typing import Optional

from playwright.sync_api import sync_playwright
from youtube_dl.utils import DownloadError, YoutubeDLError

from .monsnode_parser import MonsnodeParser
from .twitter_crawler import TwitterCrawler
from .utils.youtube_dl_wrapper import youtube_dl_wrapper


class PlatformVideoDownloader:
    monsnode_parser: MonsnodeParser
    video_output_path: str = 'videos'

    def __init__(self, video_output_path: str = 'videos', monsnode_parser: MonsnodeParser = MonsnodeParser()):
        self.video_output_path = video_output_path
        self.monsnode_parser = monsnode_parser

    def download_monsnode_video(self, link: str) -> None:
        video_filename, video_link = self.monsnode_parser.get_video(link)
        youtube_dl_option = self._make_youtube_dl_option(video_filename)
        youtube_dl_wrapper.download([video_link], youtube_dl_option)

    def download_twitter_video(
        self,
        link: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ) -> None:
        try:
            youtube_dl_option = self._make_youtube_dl_option()
            youtube_dl_wrapper.download([link], youtube_dl_option)
        except YoutubeDLError as exception:
            if not username or not password:
                raise Exception('Username and password are required to download private Twitter video') from exception

            videos_info = self._get_twitter_private_videos_info(link, username, password)
            for video_filename, video_link in videos_info:
                youtube_dl_option = self._make_youtube_dl_option(video_filename)
                youtube_dl_wrapper.download([video_link], youtube_dl_option)

    def _make_youtube_dl_option(self, video_filename: Optional[str] = None) -> dict[str, str]:
        youtube_dl_output_template = \
            f'{self.video_output_path}/{video_filename}' \
                if video_filename else \
            f'{self.video_output_path}/%(title)s.%(ext)s'
        return {'format': 'bestvideo/best', 'outtmpl': youtube_dl_output_template}

    def _get_twitter_private_videos_info(
        self,
        target_link: str,
        username: str,
        password: str,
    ) -> list[tuple[str, str]]:
        with sync_playwright() as playwright_sync:
            browser = playwright_sync.webkit.launch(headless=True)
            page = browser.new_page()
            crawler = TwitterCrawler(page)
            crawler.login(username, password)
            videos_info = crawler.get_video_of_tweet(target_link)
            page.close()
            browser.close()
        return videos_info
