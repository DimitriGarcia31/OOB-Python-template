from .data import films
from films.film import FilmCleaner
import random

class Library:
    """Bibliothèque de films."""

    def __init__(self):
        """Initialise les films."""
        self.films = []
        for raw_d_film in films:
            film = FilmCleaner(raw_d_film).generate()
            film.where = self
            self.films.append(film)
            
        self.sort_by_date_and_name()

    def sort_by_date_and_name(self):
        """Tri les films par date et par nom."""
        self.films.sort(key=lambda film: (film.date, film.name))
    
    def sort_by_type(self):
        """Tri les films par type DVD/VHF"""
        self.films.sort(key=lambda film: film.type)

    def find_by_name(self, name):
        """Retourne le film cherché si existant dans la librairie"""
        for film in self.films:
            if film.name == name:
                return film
        return None
    
    def get_random_choice(self):
        """Propose un film aléatoirement depuis la librairie"""
        return random.choice(self.films)

    def get_films_lent(self):
        """Retourne la liste des films prêtés"""
        films_lent = [film for film in self.films if film.where is not self]
        return films_lent


    def __str__(self):
        return f"{self.films}"