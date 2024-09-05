from pydantic import field_serializer
from shapely import Polygon, to_geojson, from_geojson as shape_from_geojson
from .base import BaseObject
from .generics import GenericReference
from ..utils import reference_link
from ..exceptions import ShapeException


class RiskAreaReference(GenericReference):
    id: int


@reference_link(RiskAreaReference, 'id')
class RiskArea(BaseObject):
    id: int
    name: str
    polygon: Polygon

    @classmethod
    def from_geojson(cls, id: int, name: str, geojson: dict):
        if not isinstance(polygon := shape_from_geojson(geojson), Polygon):
            raise ShapeException(f'Expecting Polygon got {type(polygon)}')
        return cls(id=id, name=name, polygon=polygon)

    @field_serializer('polygon')
    def serialize_dt(self, polygon: Polygon, _info):
        return to_geojson(polygon)