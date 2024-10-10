from typing import List
import requests
from api.responses import Entrance
from pydantic_core import from_json
from pydantic import TypeAdapter


class Grottocenter:
    def __init__(self) -> None:
        self.base_url = "https://api.grottocenter.org/api/v1"

    def get_entrance(self, id: int) -> Entrance:
        response = requests.get(f"{self.base_url}/entrances/{id}")
        entrance = Entrance.model_validate_json(response.content)
        return entrance

    def get_random_entrance(self) -> Entrance:
        response = requests.get(f"{self.base_url}/entrances/findRandom")
        entrance = Entrance.model_validate_json(response.content)
        return entrance

    def get_entrances_from_coords(
        self,
        south_west_latitude: float,
        south_west_longitude: float,
        north_east_latitude: float,
        north_east_longitude: float,
    ) -> List[Entrance]:
        response = requests.get(
            f"{self.base_url}/geoloc/entrances/",
            params={
                "sw_lat": south_west_latitude,
                "sw_lng": south_west_longitude,
                "ne_lat": north_east_latitude,
                "ne_lng": north_east_longitude,
            },
        )        
        entrances = TypeAdapter(List[Entrance]).validate_json(response.content)
        return entrances

    def get_points_from_coords(
        self,
        south_west_latitude: float,
        south_west_longitude: float,
        north_east_latitude: float,
        north_east_longitude: float,
    ) -> List[List[float]]:
        response = requests.get(
            f"{self.base_url}/geoloc/entrancesCoordinates/",
            params={
                "sw_lat": south_west_latitude,
                "sw_lng": south_west_longitude,
                "ne_lat": north_east_latitude,
                "ne_lng": north_east_longitude,
            },
        )
