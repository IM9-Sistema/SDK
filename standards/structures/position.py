from datetime import datetime
from .base import BaseObject
from .equipament import PrimitiveEquipament, Equipament, EquipamentEventType, VehicleState
from .generics import Primitive

class BatteryData(BaseObject):
    internal_wattage: float|None
    external_wattage: float|None

class ExtraInfo(BaseObject):
    io_set: list[bool]

class PrimitivePosition(Primitive):
    latitude: float
    longitude: float
    speed: float|None
    distance: float|None
    recieved_at: datetime
    generated_at: datetime
    equipament: PrimitiveEquipament
    battery: BatteryData|None
    is_stale: bool
    extras: ExtraInfo|None
    state: VehicleState
    event: EquipamentEventType|None


class Position(BaseObject):
    latitude: float
    longitude: float
    address: str
