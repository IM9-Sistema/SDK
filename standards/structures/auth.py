from .base import BaseObject


class PasswordUsername(BaseObject):
    username: str
    password: str

    @property
    def user(self):
        return self.username