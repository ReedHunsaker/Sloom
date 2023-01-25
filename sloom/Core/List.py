import functools
from .Terminal import *

class List:
    """
    Type safe collection with custom functions
    Includes:
    - reduce, filter, map
    """
    def __init__(self, type) -> None:
        self.contents = list()
        self.type = type
        pass
    
    
    def _asList(self):
        """
        Set the contents type to be of type 'list'
        """
        self.contents = list(self.contents)

    def append(self, value):
        if isinstance(value, self.type):
            self.contents.append(value)
        else:
            Terminal.error(f"Type mismatch:{type(value)} is not {type}")

    def filter(self, fn):
        self.contents = list(filter(fn, self.contents))

    def map(self, fn):
        self.contents = list(map(fn, self.contents))

    def reduce(self, fn):
        return functools.reduce(fn, self.contents)
    
    def count(self):
        return len(self.contents)