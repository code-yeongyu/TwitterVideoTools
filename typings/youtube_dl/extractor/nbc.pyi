"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor
from .theplatform import ThePlatformIE
from .adobepass import AdobePassIE

class NBCIE(AdobePassIE):
    _VALID_URL = ...
    _TESTS = ...


class NBCSportsVPlayerIE(InfoExtractor):
    _VALID_URL_BASE = ...
    _VALID_URL = ...
    _TESTS = ...


class NBCSportsIE(InfoExtractor):
    _VALID_URL = ...
    _TESTS = ...


class NBCSportsStreamIE(AdobePassIE):
    _VALID_URL = ...
    _TEST = ...


class NBCNewsIE(ThePlatformIE):
    _VALID_URL = ...
    _TESTS = ...


class NBCOlympicsIE(InfoExtractor):
    IE_NAME = ...
    _VALID_URL = ...
    _TEST = ...


class NBCOlympicsStreamIE(AdobePassIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TEST = ...
    _DATA_URL_TEMPLATE = ...


