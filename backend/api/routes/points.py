import uuid
from typing import Annotated
from fastapi import APIRouter, Depends

from api.responses import PointOfInterest, PointTypeEnum
from api.services.grottocenter import Grottocenter


router = APIRouter(prefix="/points")
CaveDatabase = Annotated[Grottocenter, Depends(Grottocenter)]

@router.get("/")
def test() -> PointOfInterest:
    return PointOfInterest(
        id=uuid.uuid4(),
        grottocenter_id=59,
        name='Baume de la Favière',
        latitude=46.707970,
        longitude=6.091082,
        type=PointTypeEnum.cave
    )

@router.get("/cave/random")
def get_random_cave(grottocenter: CaveDatabase):
    return grottocenter.get_random_entrance()

@router.get("/cave/{id}")
def get_cave_by_id(id: int, grottocenter: CaveDatabase):
    return grottocenter.get_entrance(id)
