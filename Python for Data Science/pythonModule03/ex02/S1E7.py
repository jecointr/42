# S1E7.py
from S1E9 import Character


class Baratheon(Character):
    """Classe représentant la famille Baratheon."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialise un Baratheon avec prénom, état de vie
        et caractéristiques.
        """
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Met le personnage à mort."""
        self.is_alive = False

    def __str__(self):
        """Retourne une chaîne descriptive."""
        return f"{self.family_name} ('{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()


class Lannister(Character):
    """Classe représentant la famille Lannister."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialise un Lannister avec prénom, état de vie
        et caractéristiques.
        """
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Met le personnage à mort."""
        self.is_alive = False

    def __str__(self):
        """Retourne une chaîne descriptive."""
        return f"{self.family_name} ('{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Crée un Lannister en chaîne."""
        return cls(first_name, is_alive)
