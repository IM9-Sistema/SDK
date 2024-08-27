from .base import BaseObject
from .equipment import Equipment
from .vehicle import VehicleReference


class Trackable(BaseObject):
    id: int
    equipment: Equipment
    vehicle: VehicleReference
