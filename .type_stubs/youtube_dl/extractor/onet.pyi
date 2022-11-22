"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class OnetBaseIE(InfoExtractor):
    _URL_BASE_RE = ...


class OnetMVPIE(OnetBaseIE):
    _VALID_URL = ...
    _TEST = ...


class OnetIE(OnetBaseIE):
    _VALID_URL = ...
    IE_NAME = ...
    _TESTS = ...


class OnetChannelIE(OnetBaseIE):
    _VALID_URL = ...
    IE_NAME = ...
    _TESTS = ...


class OnetPlIE(InfoExtractor):
    _VALID_URL = ...
    IE_NAME = ...
    _TESTS = ...

