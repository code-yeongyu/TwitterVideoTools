"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class XimalayaBaseIE(InfoExtractor):
    _GEO_COUNTRIES = ...


class XimalayaIE(XimalayaBaseIE):
    IE_NAME = ...
    IE_DESC = ...
    _VALID_URL = ...
    _USER_URL_FORMAT = ...
    _TESTS = ...


class XimalayaAlbumIE(XimalayaBaseIE):
    IE_NAME = ...
    IE_DESC = ...
    _VALID_URL = ...
    _TEMPLATE_URL = ...
    _BASE_URL_TEMPL = ...
    _LIST_VIDEO_RE = ...
    _TESTS = ...

