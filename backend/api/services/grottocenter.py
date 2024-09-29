import requests

class Grottocenter:
    def __init__(self) -> None:
        self.base_url = 'https://api.grottocenter.org/api/v1'

    def get_entrance(self, id: int):
        response = requests.get(f'{self.base_url}/entrances/{id}')
        return response.json()
    
    def get_random_entrance(self):
        response = requests.get(f'{self.base_url}/entrances/findRandom')
        return response.json()