from datetime import datetime
from enum import Enum

from pydantic import Field

from .trackable import Trackable
from .base import BaseObject
from .equipment import PrimitiveEquipment, Equipment, EquipmentEventType, VehicleState
from .generics import Primitive

class BatteryData(BaseObject):
    internal_wattage: float|None
    external_wattage: float|None

class ExtraInfo(BaseObject):
    io_set: list[bool]

class Ignition(Enum):
    OFF = 0
    ON = 1

class PrimitivePosition(Primitive):
    latitude: float
    longitude: float
    speed: float|None
    distance: float|None
    received_at: datetime
    generated_at: datetime
    equipment: PrimitiveEquipment
    battery: BatteryData|None
    is_stale: bool
    extras: ExtraInfo|None
    state: VehicleState
    event: EquipmentEventType | None


class Position(BaseObject):
    latitude: float
    longitude: float
    address: str
    received_at: datetime
    generated_at: datetime
    trackable: Trackable
    distance: float|None
    ignition: Ignition
    speed: float|None
    battery: BatteryData = Field(default_factory=BatteryData)
