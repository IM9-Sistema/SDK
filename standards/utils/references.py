from typing import Type

from pydantic import BaseModel


def reference_link(refclass: Type[BaseModel], *fields: str):
    def get_reference(self):
        return refclass(**{k: v for k,v in self.model_dump().items() if k in fields})

    def wrapper(_class):
        _class.get_reference = get_reference
        return _class
    return wrapper
