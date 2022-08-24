
class Film:
    """Film"""
    
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.where = None

    def display_info(self):
        print(self.name, self.date, self.where)
    
    def __str__(self):
        return f"{self.name} ({self.date})"

    def __repr__(self) -> str:
        return str(self)

class FilmVHF(Film):
    """VHF Film"""

    type="vhf"

    def __init__(self, name, date):
        super().__init__(name, date)
    
    def display_info(self):
        super().display_info()
        print("VHF")
        

class FilmDVD(Film):
    """DVD Film"""

    type="dvd"

    def __init__(self, name, date):
        super().__init__(name, date)

    def display_info(self):
        super().display_info()
        print("DVD")


class FilmCleaner:
    """Génère un film à partir de données brutes."""

    def __init__(self, film_raw_data):
        self.film_raw_data = film_raw_data

    def generate(self):
        """Génère le film."""
        name = self.generate_name()
        date = self.generate_date()
        type = self.generate_type()
        for Film in (FilmVHF, FilmDVD):
            if type == Film.type:
                return Film(name, date)
        
    def generate_name(self):
        """génère le nom"""
        name_data = self.film_raw_data[0]
        return name_data[: name_data.index("(")].strip()

    def generate_date(self):
        """génère la date"""
        name_data = self.film_raw_data[0]
        idx_1 = name_data.index("(")
        idx_2 = name_data.index(")")
        return name_data[idx_1+1 : idx_2].strip()

    def generate_type(self):
        """Génère le type."""
        return self.film_raw_data[1].lower()