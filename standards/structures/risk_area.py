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
    points: list[[float, float]]

    @classmethod
    def from_geojson(cls, id: int, name: str, geojson: dict):
        polygon: Polygon
        if not isinstance(polygon := shape_from_geojson(geojson), Polygon):
            raise ShapeException(f'Expecting Polygon got {type(polygon)}')
        x, y = polygon.coords.xy
        points = [[a, b] for a,b in zip(x,y)]

        return cls(id=id, name=name, points=points)

    @property
    def polygon(self) -> Polygon:
        return Polygon(self.points)