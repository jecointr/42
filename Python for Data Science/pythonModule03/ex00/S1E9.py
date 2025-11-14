# S1E9.py
from abc import ABC, abstractmethod

class Character(ABC):
    """Classe abstraite représentant un personnage."""
    
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialise un personnage avec un prénom et un état de vie."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Change l'état de vie du personnage à False."""
        self.is_alive = False


class Stark(Character):
    """Classe représentant un membre de la famille Stark."""
    
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialise un membre Stark avec un prénom et un état de vie."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Met le personnage Stark à mort."""
        self.is_alive = False

