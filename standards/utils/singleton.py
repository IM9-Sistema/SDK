from ..exceptions import NotInstancedException
from pydantic._internal._model_construction import ModelMetaclass


class SingletonMeta(ModelMetaclass):
    _instances = {}

    def __init__(cls, *args, **kwargs):
        if not cls in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__init__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    @classmethod
    def get(cls):
        if cls in cls._instances:
            return cls._instances[cls]
        raise NotInstancedException()
