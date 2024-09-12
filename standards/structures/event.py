from pydantic import Field

from .base import BaseObject
from enum import Enum, auto


class EventType(Enum):
    POSITION = auto()
    EQUIPMENT_EVENT = auto() # Not implemented
    POSITION_WITH_EVENT = auto()

class MetadataType(Enum):
    POSITION_WITH_NO_TRACKABLE = auto()
    AGGREGATED_EVENT = auto()
    ISSUER = auto()

class EventMetadata(BaseObject):
    type: MetadataType
    data: str|dict|BaseObject|None = Field(default=None)

class Event[T](BaseObject):
    type: EventType
    data: T
    metadata: list[EventMetadata] = Field(default_factory=list)
