from datetime import datetime

from .base import BaseObject


class Anchor(BaseObject):
    latitude: float
    longitude: float
    created_on: datetime