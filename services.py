import random

from exception import APIException, ValidationException, NotFoundException


class RickAndMortyService:

    def __init__(self, api, storage):
        self.api = api
        self.storage = storage



    def search_characters(
        self,
        name=None,
        status=None,
        species=None,
        gender=None
    ):
        if not any([name, status, species, gender]):
            raise ValidationException(
                "Please enter at least one search parameter."
            )

        data = self.api.search_characters(
            name=name,
            status=status,
            species=species,
            gender=gender
        )

        results = data.get("results", [])

        for character in results:
            self.storage.add_character_from_data(character)

        query_parts = []

        if name:
            query_parts.append(f"name={name}")

        if status:
            query_parts.append(f"status={status}")

        if species:
            query_parts.append(f"species={species}")

        if gender:
            query_parts.append(f"gender={gender}")

        self.storage.add_search_history(
            "character",
            ", ".join(query_parts)
        )

        return results

    def get_character(self, character_id):
        self.validate_id(character_id)

        data = self.api.get_character_by_id(character_id)

        self.storage.add_character_from_data(data)

        return data

    def get_random_character(self):
        character = self.api.get_random_character()

        if not character:
            raise NotFoundException(
                "No random character found."
            )

        self.storage.add_character_from_data(character)

        return character

    def search_locations(
        self,
        name=None,
        location_type=None,
        dimension=None
    ):
        if not any([name, location_type, dimension]):
            raise ValidationException(
                "Please enter at least one search parameter."
            )

        data = self.api.search_locations(
            name=name,
            location_type=location_type,
            dimension=dimension
        )

        results = data.get("results", [])

        for location in results:
            self.storage.add_location_from_data(location)

        query_parts = []

        if name:
            query_parts.append(f"name={name}")

        if location_type:
            query_parts.append(f"type={location_type}")

        if dimension:
            query_parts.append(f"dimension={dimension}")

        self.storage.add_search_history(
            "location",
            ", ".join(query_parts)
        )

        return results

    def get_location(self, location_id):
        self.validate_id(location_id)

        data = self.api.get_location_by_id(location_id)

        self.storage.add_location_from_data(data)

        return data



    def search_episodes(
        self,
        name=None,
        episode=None
    ):
        if not any([name, episode]):
            raise ValidationException(
                "Please enter at least one search parameter."
            )

        data = self.api.search_episodes(
            name=name,
            episode=episode
        )

        results = data.get("results", [])

        for item in results:
            self.storage.add_episode_from_data(item)

        query_parts = []

        if name:
            query_parts.append(f"name={name}")

        if episode:
            query_parts.append(f"episode={episode}")

        self.storage.add_search_history(
            "episode",
            ", ".join(query_parts)
        )

        return results

    def get_episode(self, episode_id):
        self.validate_id(episode_id)

        data = self.api.get_episode_by_id(episode_id)

        self.storage.add_episode_from_data(data)

        return data

    def get_random_episode(self):
        episodes = self.api.get_episodes()
        results = episodes.get("results", [])

        if not results:
            raise NotFoundException(
                "No episodes found."
            )

        episode = random.choice(results)

        self.storage.add_episode_from_data(episode)

        return episode


    def add_favorite(self, character_id):
        self.validate_id(character_id)

        character = self.storage.get_character_by_id(
            character_id
        )

        if character is None:
            data = self.api.get_character_by_id(
                character_id
            )

            self.storage.add_character_from_data(data)

            character = self.storage.get_character_by_id(
                character_id
            )

        return self.storage.add_favorite(character)

    def remove_favorite(self, character_id):
        self.validate_id(character_id)

        return self.storage.remove_favorite(
            character_id
        )

    def get_favorites(self):
        return self.storage.get_favorites()


    def get_history(self):
        return self.storage.get_history()

    def clear_history(self):
        self.storage.clear_history()


    @staticmethod
    def validate_id(value):
        try:
            value = int(value)
        except (ValueError, TypeError) as error:
            raise ValidationException(
                "ID must be a number."
            ) from error

        if value <= 0:
            raise ValidationException(
                "ID must be greater than 0."
            )

        return value