"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class BandcampIE(InfoExtractor):
    _VALID_URL = ...
    _TESTS = ...


class BandcampAlbumIE(BandcampIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...
    @classmethod
    def suitable(cls, url): # -> bool:
        ...
    


class BandcampWeeklyIE(BandcampIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...


