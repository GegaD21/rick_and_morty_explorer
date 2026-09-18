class BaseModel:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name


class Character(BaseModel):
    def __init__(
        self,
        id,
        name,
        status,
        species,
        gender,
        origin,
        location,
        image=None
    ):
        super().__init__(id, name)

        self._status = status
        self._species = species
        self._gender = gender
        self._origin = origin
        self._location = location
        self._image = image

    @property
    def status(self):
        return self._status

    @property
    def species(self):
        return self._species

    @property
    def gender(self):
        return self._gender

    @property
    def origin(self):
        return self._origin

    @property
    def location(self):
        return self._location

    @property
    def image(self):
        return self._image

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "species": self.species,
            "gender": self.gender,
            "origin": self.origin,
            "location": self.location,
            "image": self.image
        }


class Location(BaseModel):
    def __init__(self, id, name, type, dimension):
        super().__init__(id, name)

        self._type = type
        self._dimension = dimension

    @property
    def type(self):
        return self._type

    @property
    def dimension(self):
        return self._dimension

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "dimension": self.dimension
        }


class Episode(BaseModel):
    def __init__(self, id, name, air_date, episode):
        super().__init__(id, name)

        self._air_date = air_date
        self._episode = episode

    @property
    def air_date(self):
        return self._air_date

    @property
    def episode(self):
        return self._episode

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "air_date": self.air_date,
            "episode": self.episode
        }