"""
This type stub file was generated by pyright.
"""

from .common import PostProcessor

class MetadataFromTitlePP(PostProcessor):
    def __init__(self, downloader, titleformat) -> None:
        ...
    
    def format_to_regex(self, fmt): # -> Literal['']:
        r"""
        Converts a string like
           '%(title)s - %(artist)s'
        to a regex like
           '(?P<title>.+)\ \-\ (?P<artist>.+)'
        """
        ...
    
    def run(self, info): # -> tuple[list[Unknown], Unknown]:
        ...
    

