from datetime import datetime
from enum import StrEnum

from .base import BaseObject
from .position import Position
from .user import User

class AlertType(StrEnum):
    MAIN_POWER_CUT = "MAIN_POWER_CUT"


class Alert(BaseObject):
    type: AlertType
    position: Position
    generated_at: datetime
    author: User
