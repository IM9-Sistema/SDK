from .base import BaseObject


class GenericReference(BaseObject): pass

class IDReference(GenericReference):
    id: int

class Primitive(BaseObject): pass

class HostAddress(BaseObject):
    host: str
    port: int

class GenericConnectionPool(BaseObject):
    min_size: int
    max_size: int|None


class RabbitMQAddress(HostAddress):
    queue: str
    durable: bool

class RabbitMQPool(RabbitMQAddress):
    pool: GenericConnectionPool