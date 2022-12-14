"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class TuneInBaseIE(InfoExtractor):
    _API_BASE_URL = ...


class TuneInClipIE(TuneInBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _API_URL_QUERY = ...
    _TESTS = ...


class TuneInStationIE(TuneInBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _EMBED_REGEX = ...
    _API_URL_QUERY = ...
    @classmethod
    def suitable(cls, url): # -> bool:
        ...
    
    _TESTS = ...


class TuneInProgramIE(TuneInBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _API_URL_QUERY = ...
    _TESTS = ...


class TuneInTopicIE(TuneInBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _API_URL_QUERY = ...
    _TESTS = ...


class TuneInShortenerIE(InfoExtractor):
    IE_NAME = ...
    IE_DESC = ...
    _VALID_URL = ...
    _TEST = ...


