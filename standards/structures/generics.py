from .base import BaseObject
from pydantic import Field


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
    stream: bool = Field(default_factory=lambda: False)
    max_size: int|None = Field(default_factory=lambda: None)
    ttl: str | None = Field(default_factory=lambda: None)

class RabbitMQPool(RabbitMQAddress):
    pool: GenericConnectionPool