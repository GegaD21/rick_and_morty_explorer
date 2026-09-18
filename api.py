import requests
import time
from decoration import handle_api_errors


class RickAndMortyAPI:
    def __init__(self):
        self.base_url = "https://rickandmortyapi.com/api"

    @handle_api_errors
    def get_character(self):
        response = requests.get(self.base_url + "/character")
        response.raise_for_status()
        return response.json()

    @handle_api_errors
    def get_all_characters(self):
        response = requests.get(self.base_url + "/character")
        response.raise_for_status()
        data = response.json()

        characters = []
        characters.extend(data["results"])

        next_url = data["info"]["next"]

        while next_url:
            time.sleep(1)

            response = requests.get(next_url)
            response.raise_for_status()
            data = response.json()

            characters.extend(data["results"])
            next_url = data["info"]["next"]

        return characters

    @handle_api_errors
    def search_character(self, name):
        response = requests.get(self.base_url + "/character/?name=" + name)
        return response.json()

    @handle_api_errors
    def get_character_by_id(self, character_id):
        response = requests.get(self.base_url + "/character/" + str(character_id))
        return response.json()

    @handle_api_errors
    def get_location(self):
        response = requests.get(self.base_url + "/location")
        return response.json()

    @handle_api_errors
    def get_location_by_id(self, location_id):
        response = requests.get(self.base_url + "/location/" + str(location_id))
        return response.json()

    @handle_api_errors
    def get_episodes(self):
        response = requests.get(self.base_url + "/episode")
        return response.json()

    @handle_api_errors
    def get_episode_by_id(self, episode_id):
        response = requests.get(self.base_url + "/episode/" + str(episode_id))
        return response.json()
