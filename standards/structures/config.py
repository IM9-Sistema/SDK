from json import load
from .base import BaseObject
from ..exceptions import IncompatibleConfigVersion
from ..utils import Singleton
from .generics import HostAddress, GenericConnectionPool
from .auth import PasswordUsername
__config_version__ = 0

# Placeholder
class ConfigSection(BaseObject): pass

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

class MSSQLConfig(PasswordUsername, HostAddress): pass

class RedisConfig(HostAddress):
    database: int
    pool: GenericConnectionPool|None
