class Character:
    def __init__(self, id, name, status, species, gender,origin ,location):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.gender = gender
        self.origin = origin
        self.location = location


class Location:
    def __init__(self, id, name, type, dimension):
        self.id = id
        self.name = name
        self.type = type
        self.dimension = dimension

class Episode:
    def __init__(self, id, name, air_date, episode):
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
