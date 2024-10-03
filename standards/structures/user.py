from .base import BaseObject

class User(BaseObject):
    id: int
    name: str

    @classmethod
    def get_system_user(cls):
        return cls(id=1, name="Automatizações Sistema")