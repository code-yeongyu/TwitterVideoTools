"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class RedGifsBaseInfoExtractor(InfoExtractor):
    _FORMATS = ...
    _API_HEADERS = ...


class RedGifsIE(RedGifsBaseInfoExtractor):
    _VALID_URL = ...
    _TESTS = ...


class RedGifsSearchIE(RedGifsBaseInfoExtractor):
    IE_DESC = ...
    _VALID_URL = ...
    _PAGE_SIZE = ...
    _TESTS = ...


class RedGifsUserIE(RedGifsBaseInfoExtractor):
    IE_DESC = ...
    _VALID_URL = ...
    _PAGE_SIZE = ...
    _TESTS = ...

