"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor, SearchInfoExtractor

def parse_qs(url): # -> dict[str, list[str]]:
    ...

class YoutubeBaseInfoExtractor(InfoExtractor):
    """Provide base functions for Youtube extractors"""
    _LOGIN_URL = ...
    _TWOFACTOR_URL = ...
    _LOOKUP_URL = ...
    _CHALLENGE_URL = ...
    _TFA_URL = ...
    _NETRC_MACHINE = ...
    _LOGIN_REQUIRED = ...
    _PLAYLIST_ID_RE = ...
    _DEFAULT_API_DATA = ...
    _YT_INITIAL_DATA_RE = ...
    _YT_INITIAL_PLAYER_RESPONSE_RE = ...
    _YT_INITIAL_BOUNDARY_RE = ...


class YoutubeIE(YoutubeBaseInfoExtractor):
    IE_DESC = ...
    _INVIDIOUS_SITES = ...
    _VALID_URL = ...
    _PLAYER_INFO_RE = ...
    _SUBTITLE_FORMATS = ...
    _GEO_BYPASS = ...
    IE_NAME = ...
    _TESTS = ...
    _formats = ...
    @classmethod
    def suitable(cls, url): # -> bool:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def extract_id(cls, url): # -> str | Any:
        ...
    


class YoutubeTabIE(YoutubeBaseInfoExtractor):
    IE_DESC = ...
    _VALID_URL = ...
    IE_NAME = ...
    _TESTS = ...
    @classmethod
    def suitable(cls, url): # -> bool:
        ...
    


class YoutubePlaylistIE(InfoExtractor):
    IE_DESC = ...
    _VALID_URL = ...
    IE_NAME = ...
    _TESTS = ...
    @classmethod
    def suitable(cls, url): # -> bool:
        ...
    


class YoutubeYtBeIE(InfoExtractor):
    _VALID_URL = ...
    _TESTS = ...


class YoutubeYtUserIE(InfoExtractor):
    _VALID_URL = ...
    _TESTS = ...


class YoutubeFavouritesIE(YoutubeBaseInfoExtractor):
    IE_NAME = ...
    IE_DESC = ...
    _VALID_URL = ...
    _LOGIN_REQUIRED = ...
    _TESTS = ...


class YoutubeSearchIE(SearchInfoExtractor, YoutubeBaseInfoExtractor):
    IE_DESC = ...
    _MAX_RESULTS = ...
    IE_NAME = ...
    _SEARCH_KEY = ...
    _SEARCH_PARAMS = ...
    _TESTS = ...


class YoutubeSearchDateIE(YoutubeSearchIE):
    IE_NAME = ...
    _SEARCH_KEY = ...
    IE_DESC = ...
    _SEARCH_PARAMS = ...


class YoutubeFeedsInfoExtractor(YoutubeTabIE):
    """
    Base class for feed extractors
    Subclasses must define the _FEED_NAME property.
    """
    _LOGIN_REQUIRED = ...
    @property
    def IE_NAME(self):
        ...
    


class YoutubeWatchLaterIE(InfoExtractor):
    IE_NAME = ...
    IE_DESC = ...
    _VALID_URL = ...
    _TESTS = ...


class YoutubeRecommendedIE(YoutubeFeedsInfoExtractor):
    IE_DESC = ...
    _VALID_URL = ...
    _FEED_NAME = ...
    _TESTS = ...


class YoutubeSubscriptionsIE(YoutubeFeedsInfoExtractor):
    IE_DESC = ...
    _VALID_URL = ...
    _FEED_NAME = ...
    _TESTS = ...


class YoutubeHistoryIE(YoutubeFeedsInfoExtractor):
    IE_DESC = ...
    _VALID_URL = ...
    _FEED_NAME = ...
    _TESTS = ...


class YoutubeTruncatedURLIE(InfoExtractor):
    IE_NAME = ...
    IE_DESC = ...
    _VALID_URL = ...
    _TESTS = ...


class YoutubeTruncatedIDIE(InfoExtractor):
    IE_NAME = ...
    IE_DESC = ...
    _VALID_URL = ...
    _TESTS = ...

