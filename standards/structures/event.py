from pydantic import Field

from .base import BaseObject
from enum import Enum, auto, StrEnum


class EventType(StrEnum):
    POSITION = "POSITION"
    EQUIPMENT_EVENT = "EQUIPMENT_EVENT" # Not implemented
    POSITION_WITH_EVENT = "POSITION_WITH_EVENT"

class MetadataType(StrEnum):
    POSITION_WITH_NO_TRACKABLE = "POSITION_WITH_NO_TRACKABLE"
    AGGREGATED_EVENT = "AGGREGATED_EVENT"
    ISSUER = "ISSUER"

class EventMetadata(BaseObject):
    type: MetadataType
    data: str|dict|BaseObject|None = Field(default=None)

class Event[T](BaseObject):
    type: EventType
    data: T
    metadata: list[EventMetadata] = Field(default_factory=list)
