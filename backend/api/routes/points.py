from fastapi import APIRouter

from api.responses import PointOfInterest, PointTypeEnum


router = APIRouter(prefix="/points")

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
