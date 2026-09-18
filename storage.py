from models import Character, Location, Episode


class Storage:

    def __init__(self):
        self.characters = []
        self.locations = []
        self.episodes = []

    def add_character(self, character):
        if self.get_character_by_id(character.id) is None:
            self.characters.append(character)

    def add_location(self, location):
        if self.get_location_by_id(location.id) is None:
            self.locations.append(location)

    def add_episode(self, episode):
        if self.get_episode_by_id(episode.id) is None:
            self.episodes.append(episode)

    def get_character_by_id(self, character_id):
        for character in self.characters:
            if character.id == character_id:
                return character

    def get_location_by_id(self, location_id):
        for location in self.locations:
            if location.id == location_id:
                return location

    def get_episode_by_id(self, episode_id):
        for episode in self.episodes:
            if episode.id == episode_id:
                return episode

    def search_character(self, name):
        results = []

        for character in self.characters:
            if name.lower() in character.name.lower():
                results.append(character)

        return results

    def get_all_characters(self):
        return self.characters

    def get_all_locations(self):
        return self.locations

    def get_all_episodes(self):
        return self.episodes

    def remove_character(self, character_id):
        character = self.get_character_by_id(character_id)

        if character:
            self.characters.remove(character)

    def remove_location(self, location_id):
        location = self.get_location_by_id(location_id)

        if location:
            self.locations.remove(location)

    def remove_episode(self, episode_id):
        episode = self.get_episode_by_id(episode_id)

        if episode:
            self.episodes.remove(episode)

    def clear_characters(self):
        self.characters = []

    def clear_locations(self):
        self.locations = []

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
            data["location"]["name"]
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
            data["episode"],
        )
        self.add_episode(episode)

