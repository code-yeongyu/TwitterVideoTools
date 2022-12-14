"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class CrunchyrollBaseIE(InfoExtractor):
    _LOGIN_URL = ...
    _API_BASE = ...
    _NETRC_MACHINE = ...
    params = ...


class CrunchyrollBetaIE(CrunchyrollBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...


class CrunchyrollBetaShowIE(CrunchyrollBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...


