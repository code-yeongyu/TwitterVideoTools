"""
This type stub file was generated by pyright.
"""

from .ffmpeg import FFmpegPostProcessor
from ..utils import PostProcessingError

class EmbedThumbnailPPError(PostProcessingError):
    ...


class EmbedThumbnailPP(FFmpegPostProcessor):
    def __init__(self, downloader=..., already_have_thumbnail=...) -> None:
        ...
    
    def run(self, info): # -> tuple[list[Unknown], Unknown]:
        ...
    


