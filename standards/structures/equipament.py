from enum import Enum, auto
from .base import BaseObject
from ..utils import reference_link
from .generics import IDReference, Primitive


class EquipamentReference(IDReference): pass

class PrimitiveEquipamentReference(IDReference): pass


@reference_link(PrimitiveEquipamentReference, "id")
class PrimitiveEquipament(Primitive):
    uin: str

@reference_link(EquipamentReference, "uin")
class Equipament(BaseObject):
    id: int
    uin: str

class EquipamentEventType(Enum):
    PANIC_BUTTON = 101
    PARKING_LOCK = 102
    MAIN_POWER_CUT = 103
    ANTI_THEFT = 105
    ANTI_THEFT_DOOR = 106
    MOTION = 107
    ANTI_THEFT_SHOCK = 108
    REGULAR_POSITION = 200

class VehicleState(Enum):
    ON = auto()
    IDLE = auto()
    OFF = auto()