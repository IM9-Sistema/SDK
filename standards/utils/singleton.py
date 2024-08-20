from ..exceptions import NotInstancedException

class SingletonMeta(type):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if not cls in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__new__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(object, metaclass=SingletonMeta):
    @classmethod
    def get(cls):
        if cls in cls._instances:
            return cls._instances[cls]
        raise NotInstancedException()
