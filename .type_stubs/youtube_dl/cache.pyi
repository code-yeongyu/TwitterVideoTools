"""
This type stub file was generated by pyright.
"""

class Cache:
    def __init__(self, ydl) -> None:
        ...
    
    @property
    def enabled(self): # -> bool:
        ...
    
    def store(self, section, key, data, dtype=...): # -> None:
        ...
    
    def load(self, section, key, dtype=..., default=...): # -> Any | None:
        ...
    
    def remove(self): # -> None:
        ...
    

