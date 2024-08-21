from .base import StandardException

class NotInstancedException(StandardException):
    pass



class CastSourceDosentMeetTargetRequiredFields(StandardException):
    pass


class TypeNotCastable(StandardException):
    pass
