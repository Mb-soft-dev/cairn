import uuid
import requests
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


@router.get("/grottocenter/findRandom")
def randomEntrance():
    response = requests.get('https://api.grottocenter.org/api/v1/entrances/findRandom')
    return response.json()

@router.get("/grottocenter")
def randomEntrance():
    response = requests.get('https://api.grottocenter.org/api/v1/entrances/59')
    return response.json()