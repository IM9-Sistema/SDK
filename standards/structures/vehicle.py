from .base import BaseObject
from ..utils import reference_link


class VehicleReference(BaseObject):
    id: int

@reference_link(VehicleReference, 'id')
class Vehicle(BaseObject):
    id: int
    plate: str