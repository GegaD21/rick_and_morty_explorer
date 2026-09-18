import json
import os

from models import Character, Location, Episode
from exception import StorageException


class Storage:

    def __init__(self):
        self.characters = []
        self.locations = []
        self.episodes = []

        self.data_folder = "data"
        self.favorites_file = os.path.join(
            self.data_folder,
            "favorites.json"
        )
        self.history_file = os.path.join(
            self.data_folder,
            "history.json"
        )

        self._create_data_folder()

    def _create_data_folder(self):
        try:
            os.makedirs(self.data_folder, exist_ok=True)

        except OSError as error:
            raise StorageException(
                "Could not create data folder."
            ) from error



    def add_character(self, character):
        if self.get_character_by_id(character.id) is None:
            self.characters.append(character)

    def get_character_by_id(self, character_id):
        for character in self.characters:
            if character.id == character_id:
                return character

        return None

    def get_all_characters(self):
        return self.characters

    def search_character(self, name):
        results = []

        for character in self.characters:
            if name.lower() in character.name.lower():
                results.append(character)

        return results

    def remove_character(self, character_id):
        character = self.get_character_by_id(character_id)

        if character:
            self.characters.remove(character)

    def clear_characters(self):
        self.characters = []


    def add_location(self, location):
        if self.get_location_by_id(location.id) is None:
            self.locations.append(location)

    def get_location_by_id(self, location_id):
        for location in self.locations:
            if location.id == location_id:
                return location

        return None

    def get_all_locations(self):
        return self.locations

    def remove_location(self, location_id):
        location = self.get_location_by_id(location_id)

        if location:
            self.locations.remove(location)

    def clear_locations(self):
        self.locations = []



    def add_episode(self, episode):
        if self.get_episode_by_id(episode.id) is None:
            self.episodes.append(episode)

    def get_episode_by_id(self, episode_id):
        for episode in self.episodes:
            if episode.id == episode_id:
                return episode

        return None

    def get_all_episodes(self):
        return self.episodes

    def remove_episode(self, episode_id):
        episode = self.get_episode_by_id(episode_id)

        if episode:
            self.episodes.remove(episode)

    def clear_episodes(self):
        self.episodes = []



    def add_character_from_data(self, data):
        character = Character(
            data["id"],
            data["name"],
            data["status"],
            data["species"],
            data["gender"],
            data["origin"]["name"],
            data["location"]["name"],
            data.get("image")
        )

        self.add_character(character)

    def add_location_from_data(self, data):
        location = Location(
            data["id"],
            data["name"],
            data["type"],
            data["dimension"]
        )

        self.add_location(location)

    def add_episode_from_data(self, data):
        episode = Episode(
            data["id"],
            data["name"],
            data["air_date"],
            data["episode"]
        )

        self.add_episode(episode)



    def _load_json(self, filename):
        try:
            if not os.path.exists(filename):
                return []

            with open(
                filename,
                "r",
                encoding="utf-8"
            ) as file:
                return json.load(file)

        except json.JSONDecodeError as error:
            raise StorageException(
                f"Invalid JSON data in {filename}."
            ) from error

        except OSError as error:
            raise StorageException(
                f"Could not read {filename}."
            ) from error

    def _save_json(self, filename, data):
        try:
            with open(
                filename,
                "w",
                encoding="utf-8"
            ) as file:
                json.dump(
                    data,
                    file,
                    indent=4,
                    ensure_ascii=False
                )

        except OSError as error:
            raise StorageException(
                f"Could not save data to {filename}."
            ) from error



    def get_favorites(self):
        return self._load_json(self.favorites_file)

    def add_favorite(self, character):
        favorites = self.get_favorites()

        for favorite in favorites:
            if favorite["id"] == character.id:
                return False

        favorites.append(character.to_dict())

        self._save_json(
            self.favorites_file,
            favorites
        )

        return True

    def remove_favorite(self, character_id):
        favorites = self.get_favorites()

        new_favorites = [
            favorite
            for favorite in favorites
            if favorite["id"] != character_id
        ]

        if len(favorites) == len(new_favorites):
            return False

        self._save_json(
            self.favorites_file,
            new_favorites
        )

        return True

    def is_favorite(self, character_id):
        favorites = self.get_favorites()

        for favorite in favorites:
            if favorite["id"] == character_id:
                return True

        return False



    def get_history(self):
        return self._load_json(self.history_file)

    def add_search_history(self, search_type, query):
        history = self.get_history()

        history.append({
            "type": search_type,
            "query": query
        })

        self._save_json(
            self.history_file,
            history
        )

    def clear_history(self):
        self._save_json(
            self.history_file,
            []
        )
