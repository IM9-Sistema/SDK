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
    SUNTECH_PANIC_BUTTON = 101
    SUNTECH_PARKING_LOCK = 102
    SUNTECH_MAIN_POWER_CUT = 103
    SUNTECH_ANTI_THEFT = 105
    SUNTECH_ANTI_THEFT_DOOR = 106
    SUNTECH_MOTION = 107
    SUNTECH_ANTI_THEFT_SHOCK = 108
    SUNTECH_INPUT_1_GROUNDED = 111
    SUNTECH_INPUT_1_OPEN = 112
    SUNTECH_INPUT_2_GROUNDED = 113
    SUNTECH_INPUT_2_OPEN = 114
    REGULAR_POSITION = 200

class VehicleState(Enum):
    ON = auto()
    IDLE = auto()
    OFF = auto()