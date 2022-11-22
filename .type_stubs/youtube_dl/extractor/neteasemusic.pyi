"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class NetEaseMusicBaseIE(InfoExtractor):
    _FORMATS = ...
    _NETEASE_SALT = ...
    _API_BASE = ...
    def extract_formats(self, info): # -> list[Unknown]:
        ...
    
    @classmethod
    def convert_milliseconds(cls, ms): # -> int:
        ...
    
    def query_api(self, endpoint, video_id, note): # -> Any | Literal[False] | None:
        ...
    


class NetEaseMusicIE(NetEaseMusicBaseIE):
    IE_NAME = ...
    IE_DESC = ...
    _VALID_URL = ...
    _TESTS = ...


class NetEaseMusicAlbumIE(NetEaseMusicBaseIE):
    IE_NAME = ...
    IE_DESC = ...
    _VALID_URL = ...
    _TEST = ...


class NetEaseMusicSingerIE(NetEaseMusicBaseIE):
    IE_NAME = ...
    IE_DESC = ...
    _VALID_URL = ...
    _TESTS = ...


class NetEaseMusicListIE(NetEaseMusicBaseIE):
    IE_NAME = ...
    IE_DESC = ...
    _VALID_URL = ...
    _TESTS = ...


class NetEaseMusicMvIE(NetEaseMusicBaseIE):
    IE_NAME = ...
    IE_DESC = ...
    _VALID_URL = ...
    _TEST = ...


class NetEaseMusicProgramIE(NetEaseMusicBaseIE):
    IE_NAME = ...
    IE_DESC = ...
    _VALID_URL = ...
    _TESTS = ...


class NetEaseMusicDjRadioIE(NetEaseMusicBaseIE):
    IE_NAME = ...
    IE_DESC = ...
    _VALID_URL = ...
    _TEST = ...
    _PAGE_SIZE = ...

