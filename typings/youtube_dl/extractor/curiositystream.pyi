"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class CuriosityStreamBaseIE(InfoExtractor):
    _NETRC_MACHINE = ...
    _auth_token = ...
    _API_BASE_URL = ...


class CuriosityStreamIE(CuriosityStreamBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TEST = ...


class CuriosityStreamCollectionIE(CuriosityStreamBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...


