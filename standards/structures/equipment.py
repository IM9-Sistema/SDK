from enum import Enum, auto
from .base import BaseObject
from ..utils import reference_link
from .generics import IDReference, Primitive


class EquipmentReference(IDReference): pass

class PrimitiveEquipmentReference(IDReference): pass

class Technology(BaseObject):
    id: int

@reference_link(PrimitiveEquipmentReference, "id")
class PrimitiveEquipment(Primitive):
    uin: str

@reference_link(EquipmentReference, "uin")
class Equipment(BaseObject):
    id: int
    uin: str
    technology: Technology

class EquipmentEvent(Enum):
    PANIC = auto()
    PARKING_LOCK = auto()
    MAIN_POWER_CUT = auto()
    ANTI_THEFT = auto()
    ANTI_THEFT_DOOR = auto()
    MOTION = auto()
    ANTI_THEFT_SHOCK = auto()
    GENERIC_INPUT = auto()

class PrimitiveEquipmentEventType(Enum):
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

class VehicleState(Enum):
    ON = auto()
    IDLE = auto()
    OFF = auto()