from api import RickAndMortyAPI
from storage import Storage

storage = Storage()
api = RickAndMortyAPI()
characters = api.get_all_characters()

for data in characters:
    storage.add_character_from_data(data)

print("Characters:", len(storage.get_all_characters()))


# Add one location
location_data = api.get_location_by_id(1)
storage.add_location_from_data(location_data)

# Add one episode
episode_data = api.get_episode_by_id(1)
storage.add_episode_from_data(episode_data)

# Show stored data
print(storage.characters[0].name)
print(storage.locations[0].name)
print(storage.episodes[0].air_date)

# Find by ID
found_character = storage.get_character_by_id(1)
print(found_character.name)

found_location = storage.get_location_by_id(1)
print(found_location.name)

found_episode = storage.get_episode_by_id(1)
print(found_episode.air_date)

# Search in storage
results = storage.search_character("rick sanchez")
print(results[0].name)

results = storage.search_character("Rick")
print(results[0].name)

# Count stored data
print("Characters:", len(storage.get_all_characters()))
print("Locations:", len(storage.get_all_locations()))
print("Episodes:", len(storage.get_all_episodes()))