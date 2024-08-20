from json import load
from .base import BaseObject
from ..exceptions import IncompatibleConfigVersion
from ..__init__ import __config_version__
from ..utils import Singleton

class StandardConfig(BaseObject):
    _version: int
    
    @classmethod
    def from_file(cls, path):
        with open(path, 'rb') as file:
            data = load(file)
        match data:
            case {"_version": v, **_d}:
                if v != __config_version__:
                    raise IncompatibleConfigVersion
        return cls(**data)

class SingletonConfig(StandardConfig, Singleton): pass