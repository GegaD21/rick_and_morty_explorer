from api import RickAndMortyAPI
from storage import Storage
from services import RickAndMortyService
from exception import APIException, ValidationException, StorageException


def print_character(character):
    print("\n========== CHARACTER ==========")
    print(f"ID: {character['id']}")
    print(f"Name: {character['name']}")
    print(f"Status: {character['status']}")
    print(f"Species: {character['species']}")
    print(f"Gender: {character['gender']}")
    print(f"Origin: {character['origin']['name']}")
    print(f"Location: {character['location']['name']}")
    print(f"Image: {character.get('image', 'N/A')}")
    print("===============================\n")


def print_location(location):
    print("\n========== LOCATION ==========")
    print(f"ID: {location['id']}")
    print(f"Name: {location['name']}")
    print(f"Type: {location['type']}")
    print(f"Dimension: {location['dimension']}")
    print("==============================\n")


def print_episode(episode):
    print("\n========== EPISODE ==========")
    print(f"ID: {episode['id']}")
    print(f"Name: {episode['name']}")
    print(f"Air date: {episode['air_date']}")
    print(f"Episode: {episode['episode']}")
    print("=============================\n")


def search_characters(service):
    print("\n--- Character Search ---")

    name = input("Name (Enter to skip): ").strip()
    status = input("Status (Enter to skip): ").strip()
    species = input("Species (Enter to skip): ").strip()
    gender = input("Gender (Enter to skip): ").strip()

    results = service.search_characters(
        name=name or None,
        status=status or None,
        species=species or None,
        gender=gender or None
    )

    if not results:
        print("No characters found.")
        return

    print(f"\nFound {len(results)} character(s):")

    for character in results:
        print(
            f"{character['id']}. "
            f"{character['name']} - "
            f"{character['status']} - "
            f"{character['species']}"
        )

    choice = input(
        "\nEnter character ID for details "
        "(or press Enter to return): "
    ).strip()

    if choice:
        character = service.get_character(
            service.validate_id(choice)
        )
        print_character(character)


def search_locations(service):
    print("\n--- Location Search ---")

    name = input("Name (Enter to skip): ").strip()
    location_type = input("Type (Enter to skip): ").strip()
    dimension = input("Dimension (Enter to skip): ").strip()

    results = service.search_locations(
        name=name or None,
        location_type=location_type or None,
        dimension=dimension or None
    )

    if not results:
        print("No locations found.")
        return

    print(f"\nFound {len(results)} location(s):")

    for location in results:
        print(
            f"{location['id']}. "
            f"{location['name']} - "
            f"{location['type']}"
        )

    choice = input(
        "\nEnter location ID for details "
        "(or press Enter to return): "
    ).strip()

    if choice:
        location = service.get_location(
            service.validate_id(choice)
        )
        print_location(location)


def search_episodes(service):
    print("\n--- Episode Search ---")

    name = input("Name (Enter to skip): ").strip()
    episode = input(
        "Episode code, e.g. S01E01 (Enter to skip): "
    ).strip()

    results = service.search_episodes(
        name=name or None,
        episode=episode or None
    )

    if not results:
        print("No episodes found.")
        return

    print(f"\nFound {len(results)} episode(s):")

    for item in results:
        print(
            f"{item['id']}. "
            f"{item['name']} - "
            f"{item['episode']}"
        )

    choice = input(
        "\nEnter episode ID for details "
        "(or press Enter to return): "
    ).strip()

    if choice:
        episode_data = service.get_episode(
            service.validate_id(choice)
        )
        print_episode(episode_data)


def character_details(service):
    character_id = input("Enter character ID: ").strip()

    character = service.get_character(
        service.validate_id(character_id)
    )

    print_character(character)

    favorite = input(
        "Add this character to favorites? (y/n): "
    ).strip().lower()

    if favorite == "y":
        added = service.add_favorite(
            service.validate_id(character_id)
        )

        if added:
            print("Character added to favorites.")
        else:
            print("Character is already in favorites.")


def location_details(service):
    location_id = input("Enter location ID: ").strip()

    location = service.get_location(
        service.validate_id(location_id)
    )

    print_location(location)


def episode_details(service):
    episode_id = input("Enter episode ID: ").strip()

    episode = service.get_episode(
        service.validate_id(episode_id)
    )

    print_episode(episode)


def random_character(service):
    character = service.get_random_character()
    print_character(character)


def random_episode(service):
    episode = service.get_random_episode()
    print_episode(episode)


def favorites_menu(service):
    while True:
        print("\n========== FAVORITES ==========")
        print("1. Show favorites")
        print("2. Add favorite")
        print("3. Remove favorite")
        print("0. Back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            favorites = service.get_favorites()

            if not favorites:
                print("No favorites yet.")
                continue

            for favorite in favorites:
                print(
                    f"{favorite['id']}. "
                    f"{favorite['name']} - "
                    f"{favorite['status']}"
                )

        elif choice == "2":
            character_id = input(
                "Enter character ID: "
            ).strip()

            added = service.add_favorite(
                service.validate_id(character_id)
            )

            if added:
                print("Added to favorites.")
            else:
                print("Already in favorites.")

        elif choice == "3":
            character_id = input(
                "Enter character ID: "
            ).strip()

            removed = service.remove_favorite(
                service.validate_id(character_id)
            )

            if removed:
                print("Removed from favorites.")
            else:
                print("Character is not in favorites.")

        elif choice == "0":
            break

        else:
            print("Invalid option.")


def history_menu(service):
    history = service.get_history()

    print("\n========== SEARCH HISTORY ==========")

    if not history:
        print("Search history is empty.")
        return

    for index, item in enumerate(history, start=1):
        print(
            f"{index}. "
            f"[{item['type']}] "
            f"{item['query']}"
        )


def show_menu():
    print("\n========================================")
    print("       RICK AND MORTY EXPLORER")
    print("========================================")
    print("1. Search Characters")
    print("2. Search Locations")
    print("3. Search Episodes")
    print("4. Character Details")
    print("5. Location Details")
    print("6. Episode Details")
    print("7. Random Character")
    print("8. Random Episode")
    print("9. Favorites")
    print("10. Search History")
    print("0. Exit")
    print("========================================")


def main():
    api = RickAndMortyAPI()
    storage = Storage()
    service = RickAndMortyService(api, storage)

    while True:
        show_menu()

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                search_characters(service)

            elif choice == "2":
                search_locations(service)

            elif choice == "3":
                search_episodes(service)

            elif choice == "4":
                character_details(service)

            elif choice == "5":
                location_details(service)

            elif choice == "6":
                episode_details(service)

            elif choice == "7":
                random_character(service)

            elif choice == "8":
                random_episode(service)

            elif choice == "9":
                favorites_menu(service)

            elif choice == "10":
                history_menu(service)

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please choose 0-10.")

        except APIException as error:
            print(f"\nAPI ERROR: {error}")

        except ValidationException as error:
            print(f"\nVALIDATION ERROR: {error}")

        except StorageException as error:
            print(f"\nSTORAGE ERROR: {error}")

        except Exception as error:
            print(f"\nUNEXPECTED ERROR: {error}")


if __name__ == "__main__":
    main()

