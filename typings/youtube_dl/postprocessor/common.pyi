"""
This type stub file was generated by pyright.
"""

from ..utils import PostProcessingError

class PostProcessor:
    """Post Processor class.

    PostProcessor objects can be added to downloaders with their
    add_post_processor() method. When the downloader has finished a
    successful download, it will take its internal chain of PostProcessors
    and start calling the run() method on each one of them, first with
    an initial argument and then with the returned value of the previous
    PostProcessor.

    The chain will be stopped if one of them ever returns None or the end
    of the chain is reached.

    PostProcessor objects follow a "mutual registration" process similar
    to InfoExtractor objects.

    Optionally PostProcessor can use a list of additional command-line arguments
    with self._configuration_args.
    """
    _downloader = ...
    def __init__(self, downloader=...) -> None:
        ...
    
    def set_downloader(self, downloader): # -> None:
        """Sets the downloader for this PP."""
        ...
    
    def run(self, information): # -> tuple[list[Unknown], Unknown]:
        """Run the PostProcessor.

        The "information" argument is a dictionary like the ones
        composed by InfoExtractors. The only difference is that this
        one has an extra field called "filepath" that points to the
        downloaded file.

        This method returns a tuple, the first element is a list of the files
        that can be deleted, and the second of which is the updated
        information.

        In addition, this method may raise a PostProcessingError
        exception if post processing fails.
        """
        ...
    
    def try_utime(self, path, atime, mtime, errnote=...): # -> None:
        ...
    


class AudioConversionError(PostProcessingError):
    ...


