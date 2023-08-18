from typing import *


class x:
    def __init__(self, something:int) -> None:
        self.something:int = something
    
    def __call__(self, *args: Any, **kwds: Any) -> List:
        del self.something
        