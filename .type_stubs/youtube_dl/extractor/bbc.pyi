"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class BBCCoUkIE(InfoExtractor):
    IE_NAME = ...
    IE_DESC = ...
    _ID_REGEX = ...
    _VALID_URL = ...
    _LOGIN_URL = ...
    _NETRC_MACHINE = ...
    _MEDIA_SELECTOR_URL_TEMPL = ...
    _MEDIA_SETS = ...
    _EMP_PLAYLIST_NS = ...
    _TESTS = ...
    class MediaSelectionError(Exception):
        def __init__(self, id) -> None:
            ...
        
    
    


class BBCIE(BBCCoUkIE):
    IE_NAME = ...
    IE_DESC = ...
    _VALID_URL = ...
    _MEDIA_SETS = ...
    _TESTS = ...
    @classmethod
    def suitable(cls, url): # -> bool:
        ...
    


class BBCCoUkArticleIE(InfoExtractor):
    _VALID_URL = ...
    IE_NAME = ...
    IE_DESC = ...
    _TEST = ...


class BBCCoUkPlaylistBaseIE(InfoExtractor):
    ...


class BBCCoUkIPlayerPlaylistBaseIE(InfoExtractor):
    _VALID_URL_TMPL = ...


class BBCCoUkIPlayerEpisodesIE(BBCCoUkIPlayerPlaylistBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...
    _PAGE_SIZE = ...
    _DESCRIPTION_KEY = ...


class BBCCoUkIPlayerGroupIE(BBCCoUkIPlayerPlaylistBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...
    _PAGE_SIZE = ...
    _DESCRIPTION_KEY = ...


class BBCCoUkPlaylistIE(BBCCoUkPlaylistBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _URL_TEMPLATE = ...
    _VIDEO_ID_TEMPLATE = ...
    _TESTS = ...

