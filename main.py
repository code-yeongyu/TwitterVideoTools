import json
from typing import Optional

from playwright.sync_api import sync_playwright
from pydantic import BaseModel

from utils import TwitterCrawler, VideoDownloader


class Settings(BaseModel):
    username: str
    password: str
    recent_liked: str
    videos_path: Optional[str] = None


def get_settings() -> Settings:
    with open('settings.json', 'r', encoding='utf-8') as settings_file:
        settings_dict: dict[str, str] = json.load(settings_file)
    return Settings.parse_obj(settings_dict)


def is_new_video_exists(crawler: TwitterCrawler, username: str, recent_liked: str) -> bool:
    return crawler.get_recent_liked_tweet(username) != recent_liked


def get_twitter_links(crawler: TwitterCrawler, username: str, until_link: str) -> list[str]:
    return crawler.get_liked_tweets_until(
        username,
        until_link,
    )


def save_updated_recent_likes(crawler: TwitterCrawler, username: str) -> None:
    recent_liked = crawler.get_recent_liked_tweet(username)
    settings = get_settings()
    settings.recent_liked = recent_liked
    with open('settings.json', 'w', encoding='utf-8') as settings_file:
        json.dump(settings.dict(), settings_file, indent=4)


def backup_links(links: list[str]) -> None:
    with open('links.txt', 'w', encoding='utf-8') as links_file:
        links_file.write('\n'.join(links))


def main() -> None:
    settings = get_settings()

    with sync_playwright() as playwright_sync:
        browser = playwright_sync.webkit.launch(headless=True)
        page = browser.new_page()
        crawler = TwitterCrawler(page)
        crawler.login(settings.username, settings.password)

        if not is_new_video_exists(crawler, settings.username, settings.recent_liked):
            print('No new videos to download')
            return

        links = get_twitter_links(crawler, settings.username, settings.recent_liked)
        backup_links(links)
        save_updated_recent_likes(crawler, settings.username)

        browser.close()

    video_downloader = VideoDownloader(settings.videos_path, settings.username, settings.password)
    video_downloader.download_videos(links)


main()
