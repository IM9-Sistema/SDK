from typing import Callable, Iterator
from pydantic import BaseModel
from pydantic._internal._model_construction import ModelMetaclass

from standards.exceptions.instancing import TypeNotCastable
from ..structures.base import BaseObject
from ..exceptions import CastSourceDosentMeetTargetRequiredFields


def required_fields(model: type[BaseModel], recursive: bool = False) -> Iterator[str]:
    for name, field in model.model_fields.items():
        if not field.is_required():
            continue
        t = field.annotation
        if recursive and isinstance(t, type) and issubclass(t, BaseModel):
            yield from required_fields(t, recursive=True)
        else:
            yield name


class CastableMeta(ModelMetaclass):
    _cast_map: dict[type, type] = {}
    _required_fields: dict[type, str] = {}
    
    def __call__(cls, *args, **kwargs):
        cls._required_fields[cls] = list(required_fields(cls))
        return super(CastableMeta, cls).__call__(*args, **kwargs)

    @classmethod
    def add_cast[T](cls, automatic_field_detection: bool = None) -> Callable[[T], T]:
        def wrapper(_class: T|BaseModel):
            if cls._required_fields[cls] not in _class.model_fields_set:
                raise CastSourceDosentMeetTargetRequiredFields()
            if cls not in cls._cast_map:
                cls._cast_map[cls] = []
            cls._cast_map[cls].append(_class)
            return _class
        return wrapper
    
            
    

class Castable(BaseObject, metaclass=CastableMeta):
    @classmethod
    def cast_from(cls: type, source: type):
        if source not in cls._cast_map:
            raise TypeNotCastable()