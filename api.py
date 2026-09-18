import requests
import random
from decoration import handle_api_errors, retry


class RickAndMortyAPI:

    def __init__(self):
        self.base_url = "https://rickandmortyapi.com/api"

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def get_character(self):
        response = requests.get(
            f"{self.base_url}/character",
            timeout=10
        )
        response.raise_for_status()
        return response.json()

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def get_all_characters(self):
        response = requests.get(
            f"{self.base_url}/character",
            timeout=10
        )
        response.raise_for_status()

        data = response.json()
        characters = data["results"]

        next_url = data["info"]["next"]

        while next_url:
            response = requests.get(
                next_url,
                timeout=10
            )
            response.raise_for_status()

            data = response.json()
            characters.extend(data["results"])

            next_url = data["info"]["next"]

        return characters

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def search_characters(
        self,
        name=None,
        status=None,
        species=None,
        gender=None
    ):
        params = {}

        if name:
            params["name"] = name

        if status:
            params["status"] = status

        if species:
            params["species"] = species

        if gender:
            params["gender"] = gender

        response = requests.get(
            f"{self.base_url}/character",
            params=params,
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def get_character_by_id(self, character_id):
        response = requests.get(
            f"{self.base_url}/character/{character_id}",
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def get_random_character(self):
        page = random.randint(1, 42)

        response = requests.get(
            f"{self.base_url}/character",
            params={"page": page},
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return random.choice(data["results"])

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def search_locations(
        self,
        name=None,
        location_type=None,
        dimension=None
    ):
        params = {}

        if name:
            params["name"] = name

        if location_type:
            params["type"] = location_type

        if dimension:
            params["dimension"] = dimension

        response = requests.get(
            f"{self.base_url}/location",
            params=params,
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def get_location(self):
        response = requests.get(
            f"{self.base_url}/location",
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def get_location_by_id(self, location_id):
        response = requests.get(
            f"{self.base_url}/location/{location_id}",
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def search_episodes(
        self,
        name=None,
        episode=None
    ):
        params = {}

        if name:
            params["name"] = name

        if episode:
            params["episode"] = episode

        response = requests.get(
            f"{self.base_url}/episode",
            params=params,
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def get_episodes(self):
        response = requests.get(
            f"{self.base_url}/episode",
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def get_episode_by_id(self, episode_id):
        response = requests.get(
            f"{self.base_url}/episode/{episode_id}",
            timeout=10
        )

        response.raise_for_status()
        return response.json()
import requests
import random
from decoration import handle_api_errors, retry


class RickAndMortyAPI:

    def __init__(self):
        self.base_url = "https://rickandmortyapi.com/api"

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def get_character(self):
        response = requests.get(
            f"{self.base_url}/character",
            timeout=10
        )
        response.raise_for_status()
        return response.json()

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def get_all_characters(self):
        response = requests.get(
            f"{self.base_url}/character",
            timeout=10
        )
        response.raise_for_status()

        data = response.json()
        characters = data["results"]

        next_url = data["info"]["next"]

        while next_url:
            response = requests.get(
                next_url,
                timeout=10
            )
            response.raise_for_status()

            data = response.json()
            characters.extend(data["results"])

            next_url = data["info"]["next"]

        return characters

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def search_characters(
        self,
        name=None,
        status=None,
        species=None,
        gender=None
    ):
        params = {}

        if name:
            params["name"] = name

        if status:
            params["status"] = status

        if species:
            params["species"] = species

        if gender:
            params["gender"] = gender

        response = requests.get(
            f"{self.base_url}/character",
            params=params,
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def get_character_by_id(self, character_id):
        response = requests.get(
            f"{self.base_url}/character/{character_id}",
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def get_random_character(self):
        page = random.randint(1, 42)

        response = requests.get(
            f"{self.base_url}/character",
            params={"page": page},
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return random.choice(data["results"])

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def search_locations(
        self,
        name=None,
        location_type=None,
        dimension=None
    ):
        params = {}

        if name:
            params["name"] = name

        if location_type:
            params["type"] = location_type

        if dimension:
            params["dimension"] = dimension

        response = requests.get(
            f"{self.base_url}/location",
            params=params,
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def get_location(self):
        response = requests.get(
            f"{self.base_url}/location",
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def get_location_by_id(self, location_id):
        response = requests.get(
            f"{self.base_url}/location/{location_id}",
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def search_episodes(
        self,
        name=None,
        episode=None
    ):
        params = {}

        if name:
            params["name"] = name

        if episode:
            params["episode"] = episode

        response = requests.get(
            f"{self.base_url}/episode",
            params=params,
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def get_episodes(self):
        response = requests.get(
            f"{self.base_url}/episode",
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    @retry(max_attempts=3, delay=1)
    @handle_api_errors
    def get_episode_by_id(self, episode_id):
        response = requests.get(
            f"{self.base_url}/episode/{episode_id}",
            timeout=10
        )

        response.raise_for_status()
        return response.json()
