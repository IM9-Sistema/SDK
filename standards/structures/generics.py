from .base import BaseObject


class GenericReference(BaseObject): pass

class IDReference(GenericReference):
    id: int

class Primitive(BaseObject): pass

class HostAddress(BaseObject):
    host: str
    port: int

class RabbitMQAddress(HostAddress):
    queue: str
