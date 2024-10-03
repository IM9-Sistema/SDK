from pydantic import Field

from .base import BaseObject
from .equipment import Equipment
from .vehicle import VehicleReference


class Trackable(BaseObject):
    id: int
    equipment: Equipment
    vehicle: VehicleReference
    event_groups: list[int]|None = Field(default_factory=lambda: None)