from .data import friends

class Friend:
    """amis"""

    def __init__(self, name, film=None):
        """Initialise le nom, et un film prêté si c'est le cas."""
        self.name = name,
        self.film = film
        if film :
            film.where = self

    def __str__(self):
        return f"{self.name}"

    def __repr__(self) -> str:
        return str(self)

class FriendCleaner:
    """Génère amis"""

    def __init__(self):
        self.friends = friends

    def generate(self, friend_raw_data, library):
        """Retourne un ami depuis raw data"""
        name = friend_raw_data[0]
        if len(friend_raw_data)>1:
            film_name = friend_raw_data[1]
            film = library.find_by_name(film_name)
        else :
            film = None
        return Friend(name, film)

    def list_from_data(self, library):
        """Retourne une liste d'amis à partir des données brutes."""
        result = []
        for data in self.friends:
            friend = self.generate(data, library)
            result.append(friend)
        return result

