import uuid
from typing import Annotated, List
from fastapi import APIRouter, Depends

from api.responses import Entrance, PointOfInterest, PointTypeEnum
from api.services.grottocenter import Grottocenter


router = APIRouter(prefix="/points")
CaveDatabase = Annotated[Grottocenter, Depends(Grottocenter)]


@router.get("/")
def test() -> PointOfInterest:
    return PointOfInterest(
        id=uuid.uuid4(),
        grottocenter_id=59,
        name="Baume de la Favière",
        latitude=46.707970,
        longitude=6.091082,
        type=PointTypeEnum.cave,
    )


@router.get("/entrance/random")
def get_random_entrance(grottocenter: CaveDatabase) -> Entrance:
    return grottocenter.get_random_entrance()


@router.get("/entrance/{id}")
def get_entrance_by_id(id: int, grottocenter: CaveDatabase) -> Entrance:
    return grottocenter.get_entrance(id)


@router.get("/coordinates")
def get_caves_from_coordinates(
    south_west_latitude: float,
    south_west_longitude: float,
    north_east_latitude: float,
    north_east_longitude: float,
    grottocenter: CaveDatabase,
) -> List[Entrance]:
    return grottocenter.get_entrances_from_coords(
        south_west_latitude,
        south_west_longitude,
        north_east_latitude,
        north_east_longitude,
    )
