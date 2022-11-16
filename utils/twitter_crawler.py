import time
from typing import Optional

from playwright.sync_api import Error, Page, Request


class TwitterCrawler:
    page: Page

    def __init__(self, page: Page):
        self.page = page

    @property
    def page_current_height(self) -> int:
        current_height: int = self.page.evaluate('(window.innerHeight + window.scrollY)')
        return current_height

    def login(self, username: str, password: str) -> None:
        self.page.goto('https://twitter.com/i/flow/login')
        self.page.wait_for_selector('label:has-text(\"Phone, email, or username\") div >> nth=1')
        self.page.get_by_label('Phone, email, or username').click()
        self.page.get_by_label('Phone, email, or username').fill(username)
        self.page.get_by_label('Phone, email, or username').press('Enter')
        self.page.get_by_label('Password').fill(password)
        self.page.get_by_label('Password').press('Enter')
        self.page.wait_for_url('https://twitter.com/home')

    def get_all_liked_tweets(self, username: str, scroll_timeout: float = 0.8) -> list[str]:
        return self.get_liked_tweets_until(username, 'nothing', scroll_timeout)

    def get_liked_tweets_until(self, username: str, until_link: str, scroll_timeout: float = 0.8) -> list[str]:
        self._open_liked_tweets(username)
        links: list[str] = []

        previous_height = self.page_current_height
        while True:
            self.page.mouse.wheel(0, 1500)
            time.sleep(scroll_timeout)    # wait for mouse cursor down
            is_page_bottom = self.page_current_height == previous_height
            if is_page_bottom:
                break
            previous_height = self.page_current_height

            new_links = self._get_article_links_in_current_screen()
            links.extend(new_links)
            links = list(set(links))

            if until_link in links:
                break

        return links

    def get_recent_liked_tweet(self, username: str) -> str:
        self._open_liked_tweets(username)
        return self._get_article_links_in_current_screen()[0]

    def get_video_of_tweet(self, link: str, timeout: Optional[float] = 5000) -> Optional[tuple[str, list[str]]]:
        links: list[str] = []

        def _request_m3u8_capture_handler(request: Request) -> None:
            if 'm3u8' in request.url:
                links.append(request.url)

        self.page.on('request', _request_m3u8_capture_handler)
        self.page.goto(link)
        try:
            self.page.wait_for_selector('video', timeout=timeout)
        except Error:
            return None

        return self._get_video_name(), links

    def _get_video_name(self) -> str:
        uploader = self.page.get_by_test_id('primaryColumn').get_by_role('link').nth(0).inner_text().strip()
        content = self.page.get_by_role('article').get_by_test_id('tweetText').nth(0).inner_text().strip()
        return f'{uploader} - {content}.mp4'

    def _open_liked_tweets(self, username: str) -> None:
        self.page.goto(f'https://twitter.com/{username}/likes')
        self.page.wait_for_selector('article')

    def _get_article_links_in_current_screen(self) -> list[str]:
        links: list[str] = []

        while True:
            articles = self.page.locator('article')
            article_length = articles.count()
            try:
                links = [
                    'https://twitter.com' +
                    (articles.nth(i).locator('div').locator('a').nth(3).get_attribute('href', timeout=500) or '')
                    for i in range(article_length)
                ]
                break
            except Error:
                self.page.mouse.wheel(0, 500)

        return links
