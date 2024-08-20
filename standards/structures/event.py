from .base import BaseObject
from enum import Enum, auto


class EventType(Enum):
    POSITION = auto()
    EQUIPAMENT_EVENT = auto()
    POSITION_WITH_EVENT = auto()

class Issuer(BaseObject):
    name: str


class Event[T](BaseObject):
    type: EventType
    issuer: Issuer
    data: T
