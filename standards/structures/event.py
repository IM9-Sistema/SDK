from typing import Any

from pydantic import Field

from .base import BaseObject
from enum import Enum, auto


class EventType(Enum):
    POSITION = auto()
    EQUIPMENT_EVENT = auto() # Not implemented
    POSITION_WITH_EVENT = auto()

class Issuer(BaseObject):
    name: str

class EventMetadata(BaseObject):
    type: EventType
    extras: Any

class Event[T](BaseObject):
    type: EventType
    issuer: Issuer
    data: T
    metadata: list[EventMetadata] = Field(default_factory=list)
