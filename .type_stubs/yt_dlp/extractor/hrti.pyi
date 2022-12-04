"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class HRTiBaseIE(InfoExtractor):
    """
        Base Information Extractor for Croatian Radiotelevision
        video on demand site https://hrti.hrt.hr
        Reverse engineered from the JavaScript app in app.min.js
    """
    _NETRC_MACHINE = ...
    _APP_LANGUAGE = ...
    _APP_VERSION = ...
    _APP_PUBLICATION_ID = ...
    _API_URL = ...
    _token = ...


class HRTiIE(HRTiBaseIE):
    _VALID_URL = ...
    _TESTS = ...


class HRTiPlaylistIE(HRTiBaseIE):
    _VALID_URL = ...
    _TESTS = ...

