import requests
from api.responses import Cave, Entrance
from pydantic_core import from_json


class Grottocenter:
    def __init__(self) -> None:
        self.base_url = "https://api.grottocenter.org/api/v1"

    def get_entrance(self, id: int) -> Entrance:
        response = requests.get(f"{self.base_url}/entrances/{id}")
        entrance = Entrance.model_validate(from_json(response.content))
        return entrance

    def get_random_entrance(self) -> Entrance:
        response = requests.get(f"{self.base_url}/entrances/findRandom")
        entrance = Entrance.model_validate(from_json(response.content))
        return entrance
