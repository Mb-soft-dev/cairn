import decimal
from enum import Enum
from uuid import UUID
from pydantic import BaseModel


class PointTypeEnum(str, Enum):
    cave = 'gouffre'
    gite = 'gite'
    
class PointOfInterest(BaseModel):
    id: UUID
    grottocenter_id: int
    name: str
    latitude: float
    longitude: float
    type: PointTypeEnum