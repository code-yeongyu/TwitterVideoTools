"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class NYTimesBaseIE(InfoExtractor):
    _SECRET = ...


class NYTimesIE(NYTimesBaseIE):
    _VALID_URL = ...
    _TESTS = ...


class NYTimesArticleIE(NYTimesBaseIE):
    _VALID_URL = ...
    _TESTS = ...


class NYTimesCookingIE(NYTimesBaseIE):
    _VALID_URL = ...
    _TESTS = ...


