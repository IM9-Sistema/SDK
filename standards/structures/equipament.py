from enum import Enum, auto
from .base import BaseObject
from utils import reference_link
from .generics import IDReference, Primitive


class EquipamentReference(IDReference): pass

class PrimitiveEquipamentReference(IDReference): pass


@reference_link(PrimitiveEquipamentReference, "id")
class PrimitiveEquipament(Primitive):
    id: int

@reference_link(EquipamentReference, "id")
class Equipament(BaseObject):
    id: int
    uin: int

class EquipamentEventType(Enum):
    PANIC_BUTTON = 101
    PARKING_LOCK = 102
    MAIN_POWER_CUT = 103
    ANTI_THEFT = 105
    ANTI_THEFT_DOOR = 106
    MOTION = 107
    ANTI_THEFT_SHOCK = 108

class VehicleState(Enum):
    ON = auto()
    IDLE = auto()
    